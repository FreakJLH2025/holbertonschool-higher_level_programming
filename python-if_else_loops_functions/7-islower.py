#!/usr/bin/python3
def islower(c):
    """Check if a character is lowercase."""
    if len(c) > 0 and ord('a') <= ord(c) <= ord('z'):
        return True
    return False
