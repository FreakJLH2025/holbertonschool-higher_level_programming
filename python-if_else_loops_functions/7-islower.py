#!/usr/bin/python3
def islower(c):
    """Check if a character is lowercase."""
    if ord('a') <= ord(c) <= ord('z'):
        return True
    return False
