#!/usr/bin/python3
"""
Module that defines an abstract Animal class
and its subclasses Dog and Cat.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class Animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented
        by all subclasses.
        """
        pass


class Dog(Animal):
    """
    Dog class that inherits from Animal.
    """

    def sound(self):
        """
        Returns the sound of a dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class that inherits from Animal.
    """

    def sound(self):
        """
        Returns the sound of a cat.
        """
        return "Meow"
