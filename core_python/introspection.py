# introspection.py

# mypy issue 776
import sys
from typing import get_args, get_origin, get_type_hints, Generic, Protocol
from typing import _collect_type_vars, _eval_type, _strip_annotations

def _generic_mro(result, tp):
    origin = get_origin(tp)
    if origin is None:
        origin = tp
    result[origin] = tp
    if hasattr(origin, "__orig_bases__"):
        parameters = _collect_type_vars(origin.__orig_bases__)
        if origin is tp and parameters:
            result[origin] = origin[parameters]
        substitution = dict(zip(parameters, get_args(tp)))
        for base in origin.__orig_bases__:
            if get_origin(base) in result:
                continue
            base_parameters = getattr(base, "__parameters__", ())
            if base_parameters:
                base = base[tuple(substitution.get(p, p) for p in base_parameters)]
            _generic_mro(result, base)

def generic_mro(tp):
    origin = get_origin(tp)
    if origin is None and not hasattr(tp, "__orig_bases__"):
        if not isinstance(tp, type):
            raise TypeError(f"{tp!r} is not a type or a generic alias")
        return tp.__mro__
    # sentinel value to avoid to subscript Generic and Protocol
    result = {Generic: Generic, Protocol: Protocol}
    _generic_mro(result, tp)
    cls = origin if origin is not None else tp
    return tuple(result.get(sub_cls, sub_cls) for sub_cls in cls.__mro__)

def _class_annotations(cls, globalns, localns):
    hints = {}
    if globalns is None:
        base_globals = sys.modules[cls.__module__].__dict__
    else:
        base_globals = globalns
    for name, value in cls.__dict__.get("__annotations__", {}).items():
        if value is None:
            value = type(None)
        if isinstance(value, str):
            value = ForwardRef(value, is_argument=False)
        hints[name] = _eval_type(value, base_globals, localns)
    return hints


# For brevety of the example, the implementation just add the substitute_type_vars
# implementation and default to get_type_hints. Of course, it would have to be directly
# integrated into get_type_hints
def get_type_hints2(
    obj, globalns=None, localns=None, include_extras=False, substitute_type_vars=False
):
    if substitute_type_vars and (isinstance(obj, type) or isinstance(get_origin(obj), type)):
        hints = {}
        for base in reversed(generic_mro(obj)):
            origin = get_origin(base)
            if hasattr(origin, "__orig_bases__"):
                parameters = _collect_type_vars(origin.__orig_bases__)
                substitution = dict(zip(parameters, get_args(base)))
                annotations = _class_annotations(get_origin(base), globalns, localns)
                for name, tp in annotations.items():
                    if isinstance(tp, TypeVar):
                        hints[name] = substitution.get(tp, tp)
                    elif tp_params := getattr(tp, "__parameters__", ()):
                        hints[name] = tp[
                            tuple(substitution.get(p, p) for p in tp_params)
                        ]
                    else:
                        hints[name] = tp
            else:
                hints.update(_class_annotations(base, globalns, localns))
        return (
            hints
            if include_extras
            else {k: _strip_annotations(t) for k, t in hints.items()}
        )
    else:
        return get_type_hints(obj, globalns, localns, include_extras)

# Generic classes that accept at least one parameter type.
# It works also for `Protocol`s that have at least one argument.
def is_generic_class(klass):
    return hasattr(klass, '__orig_bases__') and getattr(klass, '__parameters__', None)