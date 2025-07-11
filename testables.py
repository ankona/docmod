import ast
import os
from dataclasses import dataclass


class Squarer:
    """Perform the mathematical operation 'square.'"""

    def __init__(self, value: int) -> None:
        """Initialize the instance."""
        self.value = value

    def square(self) -> int:
        """
        Calculate the square of the objects value.

        Returns
        ----------
        int
            The square of the initial value
        """
        return self.value * self.value
