from .position import Position

class Map:
    """Represents the gameboard."""

    def __init__(self, paths, start, exit, width, height):
        self._paths = set(paths)
        self.width = width
        self.height = height
        self.start = start
        self.exit = exit

    def __contains__(self, position):
        """Predicate testing if position is available in the maze."""
        return position in self._paths

    @classmethod
    def load_from_file(cls, filename):
        """Loads a new map from its textual description in a file."""
        paths = set()
        start, exit = None, None
        width, height = 0, 0

        with open(filename) as f:
            # Iterate through the lines and columns
            for x, line in enumerate(f):
                for y, col in enumerate(line):
                    if col in ".SE":
                        paths.add(Position(x, y))
                    if c == "S":
                        start = Position(x, y)
                    elif c == "E":
                        end = Position(x, y)
            # Extract the height and width
            height = x + 1
            width = y + 1

        self = cls(paths, start, exit, width, height)
        return self