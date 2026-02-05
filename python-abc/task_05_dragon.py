#!/usr/bin/python3
"""
Module that demonstrates mixins with a Dragon class.
"""


class SwimMixin:
    """Mixin that adds swimming behavior."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying behavior."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that inherits from SwimMixin and FlyMixin."""

    def roar(self):
        print("The dragon roars!")


# Testing
if __name__ == "__main__":
    draco = Dragon()
    draco.swim()   # The creature swims!
    draco.fly()    # The creature flies!
    draco.roar()   # The dragon roars!
