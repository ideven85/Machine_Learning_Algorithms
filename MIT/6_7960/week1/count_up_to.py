def count_up_to(n):
    # if n<=0:
    #     return
    #
    # yield from count_up_to(n-1)
    # yield n
    for i in range(1, n + 1):
        yield i


class SlugFromName:
    """Computes a slug from .name at access time."""

    def __get__(self, obj, owner):
        if obj is None:
            # Keep the example readable when accessed on the class:
            return "<SlugFromName descriptor>"
        name = getattr(obj, "name", "")
        return "-".join(name.lower().split()) or "<no-name>"


class EmailField:
    """Normalizes on set, then returns the stored value."""

    def __get__(self, obj, owner):
        if obj is None:
            return "<EmailField descriptor>"
        return obj.__dict__.get("_email", None)

    def __set__(self, obj, value):
        obj.__dict__["_email"] = value.strip().lower()


class User:
    slug = SlugFromName()
    email = EmailField()


u = User()
u.name = "Guido van Rossum"
u.slug = "custom-slug"
u.email = "USER@Example.COM"
print(u.slug, u.email, User.slug, User.email)


class BaseView:
    def handle(self):
        return ["base"]


class AuthMixin(BaseView):
    def handle(self):
        return ["auth"] + super().handle()


class CacheMixin(BaseView):
    def handle(self):
        return ["cache"] + super().handle()


class ReportView(AuthMixin, CacheMixin):
    def handle(self):
        return ["report"] + super().handle()


print(ReportView().handle())
print(list(count_up_to(10)))
