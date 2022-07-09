"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    0
    """
    def __init__(self, start=0):
        """ Creates a new generator instance, starting at 0, when no start argument is given"""
        self.start = start


    def generate(self):
        """ Generates next serial number (+1) """
        self.start += 1
        return self.start - 1


    def reset(self):
        """ Resets counter to 0 """
        self.start = 0


