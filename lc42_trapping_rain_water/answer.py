from typing import List


def get_water_trapped(elevation_coordinates: List[int]):
    # turn elevation coordinates into a matrix
    # example: [0, 2, 0, 1]
    # becomes: [[1, 0, 1, 0],
    #           [1, 0, 1, 1]]
    # 0 is a wall space and 1 is an "empty" space
    y_max = max(elevation_coordinates)
    matrix = [
        [
            0 if y < height else 1
            for height in elevation_coordinates
        ]
        for y in range(y_max)
    ]

    # find the index of the first wall position and the index of the last wall
    # position, then sum all of the "empty" spaces between those two walls.
    units = 0
    for row in matrix:
        first_wall = row.index(0)
        # list[::-1] reverses the list; if the last wall position is at index 0
        # it is really at the -1 th space in the list, thus the need for the or
        last_wall = row[::-1].index(0) or 1
        units += sum(row[first_wall:-last_wall])

    return units







