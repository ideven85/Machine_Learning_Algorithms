from typing import overload


class Sexy:
    def set_name(self):
        self.name = "Deven"

    def a(self):
        print(self.a(msg=self.set_name()))

    @overload
    def a(self, msg):
        return msg

    def _overload_dummy(self, *args, **kwds):
        return self.name


s = Sexy()
s.set_name()
print(s.name)
print(s.a("Hi"))
