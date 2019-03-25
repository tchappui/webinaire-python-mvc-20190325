"""Module defining a data structure representing a Position."""

class Position(tuple):
    """Object representing a position in a maze.

    The origin of the coordinate system is located at the top left corner of
    the maze. x is increasing when moving downwards and y is increasing 
    when moving to the right.

    Attributes:
        x (int): vertical position relative to the origin.
        y (int): horizontal position relative to the origin.

    """

    def __new__(cls, coords):
        """Creates a new position. 

        Tuples being immutables, it is necessary to subclass __new__ instead of
        __init__ to achieve inheritance.

        Args:
            coords (sequence): coordinates of the current position as a 
                sequence.

        Raises:
            ValueError: if coords is not a sequence of length 2.
            TypeError: if coords is not a sequence.

        """
        if len(coords) != 2:
            raise ValueError("coords must be a sequence of length 2")
        return super(cls, cls).__new__(cls, coords)
    
    @property
    def x(self):
        """Vertical position relative to the top-left origin."""
        return self[0]

    @property
    def y(self):
        """Horizontal position relative to the top-left origin."""
        return self[1]

    @property
    def up(self):
        """Returns a new adjacent position above the current position."""
        return self.__class__((self.x - 1, self.y))

    @property
    def down(self):
        """Returns a new adjacent position below the current position."""
        return self.__class__((self.x + 1, self.y))

    @property
    def left(self):
        """Returns a new adjacent position on the left of the current 
        position.
        """
        return self.__class__((self.x, self.y - 1))

    @property
    def right(self):
        """Returns a new adjacent position on the right of the current 
        position.
        """
        return self.__class__((self.x, self.y + 1))

    def get(self, direction):
        """Returns a new adjacent position located in a given direction.

        Args:
            direction (str): direction for the required new position.

        """
        return getattr(self, str(direction))

