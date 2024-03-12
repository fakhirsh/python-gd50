import random
from src.Brick import Brick

class LevelMaker:
    # This is basically a "class" method, which is the Python equivalent of a
    # static method. It's a method that's called on the class itself, rather than
    # an instance of the class. It's a method that makes sense to call even if we
    # don't have an instance of the class created yet:  LevelMaker.createMap(...)
    @staticmethod
    def createMap(atlas, brickQuads, level=1):
        # Create an empty list of bricks
        bricks = []

        # Randomly choose the number of rows
        num_rows = random.randint(1, 5)

        # Randomly choose the number of columns
        num_cols = random.randint(7, 13)

        # Lay out bricks such that they touch each other and fill the space
        for y in range(num_rows):
            for x in range(num_cols):
                # Calculate the brick's x-coordinate
                brick_x = ((x) * 32) + 8 + ((13 - num_cols) * 16)

                # Calculate the brick's y-coordinate
                brick_y = (y + 1) * 16  # Adjusted for Python's 0-indexing

                # Create a new Brick instance and add it to the bricks list
                b = Brick(brick_x, brick_y, atlas, brickQuads)
                bricks.append(b)

        return bricks
