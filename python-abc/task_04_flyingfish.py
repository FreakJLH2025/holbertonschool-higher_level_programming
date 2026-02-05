#!/usr/bin/python3
"""
Module that demonstrates multiple inheritance with FlyingFish.
"""


class Fish:
    """Fish class with swim and habitat methods."""

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """Bird class with fly and habitat methods."""

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class inheriting from both Fish and Bird."""

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")


# Testing
if __name__ == "__main__":
    ff = FlyingFish()
    ff.fly()       # The flying fish is soaring!
    ff.swim()      # The flying fish is swimming!
    ff.habitat()   # The flying fish lives both in water and the sky!

    # Exploring Method Resolution Order
    print(FlyingFish.mro())
    # or equivalently
    print(FlyingFish.__mro__)
