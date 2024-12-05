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
    100
    """

    def __init__(self, start):
        """Initialize the serial generator with a starting value."""
        self.start = start # Store the initial starting value.
        self.current = start # Set the current serial number to the starting value.
    
    def generate(self):
        """Generate the increase for serial number."""
        serial = self.current # Store the current serial number to then return.
        self.current += 1 # Increase by 1
        return serial
    
    def reset(self):
        """Reset the serial generator to the starting value."""
        self.current = self.start #Set the current serial number back to the starting value.
