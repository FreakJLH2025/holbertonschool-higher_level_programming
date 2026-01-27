#!/usr/bin/python3
"""
This module defines a Square class.
The class represents a geometric square with private attributes size and position.
It validates that size is a non-negative integer and position is a tuple of 2 positive integers.
It can compute its area and print the square using the character '#'.
"""


class Square:
    """
    This class defines a square by its size and position.
    The size attribute is private to ensure control over its type and value.
    The position attribute is private to ensure proper formatting when printing.
    Getter and setter methods are provided to retrieve and update both attributes safely.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
            TypeError: If position is not a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Returns:
            tuple: The current position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square with validation.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Compute the area of the square.

        Returns:
            int: The current square area.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square using the character '#'.

        If size is 0, print an empty line.
        Position is respected: spaces are added horizontally (position[0]),
        and newlines are added vertically (position[1]).
        """
        if self.__size == 0:
            print("")
            return

        # Print vertical offset
        for _ in range(self.__position[1]):
            print("")

        # Print each line of the square with horizontal offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
#!/usr/bin/python3
"""
This module defines a Square class.
The class represents a geometric square with private attributes size and position.
It validates that size is a non-negative integer and position is a tuple of 2 positive integers.
It can compute its area and print the square using the character '#'.
"""


class Square:
    """
    This class defines a square by its size and position.
    The size attribute is private to ensure control over its type and value.
    The position attribute is private to ensure proper formatting when printing.
    Getter and setter methods are provided to retrieve and update both attributes safely.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
            TypeError: If position is not a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Returns:
            tuple: The current position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square with validation.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Compute the area of the square.

        Returns:
            int: The current square area.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square using the character '#'.

        If size is 0, print an empty line.
        Position is respected: spaces are added horizontally (position[0]),
        and newlines are added vertically (position[1]).
        """
        if self.__size == 0:
            print("")
            return

        # Print vertical offset
        for _ in range(self.__position[1]):
            print("")

        # Print each line of the square with horizontal offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
