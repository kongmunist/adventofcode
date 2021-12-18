# --- Day 5: Hydrothermal Venture ---
# You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.
# They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

# Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:
#
# An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
# An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
# For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.
#
# So, the horizontal and vertical lines from the above list would produce the following diagram:


# In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.
# To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.
# Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

# Part 1 solution
# first, read in input.txt, where each line is in the format x1,y1 -> x2,y2
def read_input(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines
# read in input.txt
lines = read_input('input.txt')
# Clean up the lines
lines = [line.strip() for line in lines]
# Split the lines into (x1,y1) and (x2,y2), where each coordinate is an integer
lines = [line.split('->') for line in lines]

# Split the coordinates into two separate lists
lines = [[line[0].split(','), line[1].split(',')] for line in lines]
# Convert the coordinates into integers
lines = [[[int(x) for x in line[0]], [int(x) for x in line[1]]] for line in lines]

# remove all lines that are not horizontal or vertical
lines = [line for line in lines if line[0][0] == line[1][0] or line[0][1] == line[1][1]]

# please import numpy
import numpy as np

# turn the lines into a numpy array
lines = np.array(lines)

###### Done Parsing, begin solving ######
# get max x and y coordinates of all lines
max_x = max(lines[:,0,0])
max_y = max(lines[:,0,1])

# create a numpy array of zeros with shape (max_x+1, max_y+1)
grid = np.zeros((max_x+1, max_y+1))

# for each line, add 1 to the grid at the start and end coordinates
for line in lines:
    # and also add 1 to the grid at all intermediate coordinates
    if line[0][0] != line[1][0]:
        # if the line is horizontal, add 1 to all x coordinates between the start and end coordinates
        for x in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0]) + 1):
            grid[x, line[0][1]] += 1
    else:
        # if the line is vertical, add 1 to all y coordinates between the start and end coordinates
        for y in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1]) + 1):
            grid[line[0][0], y] += 1


# count the number of points where at least two lines overlap, where the value is greater than 1
print(np.sum(grid > 1))


## Part 2 solution
# Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.
# Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:
#
# An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
# An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
# Considering all lines from the above example would now produce the following diagram:

# You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.
# Consider all of the lines. At how many points do at least two lines overlap?


## read in input.txt
lines = read_input('input.txt')
# Clean up the lines
lines = [line.strip() for line in lines]
# Split the lines into (x1,y1) and (x2,y2), where each coordinate is an integer
lines = [line.split('->') for line in lines]

# Split the coordinates into two separate lists
lines = [[line[0].split(','), line[1].split(',')] for line in lines]
# Convert the coordinates into integers
lines = [[[int(x) for x in line[0]], [int(x) for x in line[1]]] for line in lines]

# turn the lines into a numpy array
lines = np.array(lines)

###### Done Parsing, begin solving ######
# get max x and y coordinates of the first element of each line


# create a numpy array of zeros with shape (max_x*2, max_y*2)
# get biggest of the max_x and max_y
maxofBoth = max(max_x, max_y)
grid = np.zeros((maxofBoth*2, maxofBoth*2))

# split each line into two points, and add them to the start and end coordinates list respectively
start_points = lines[:,0]
end_points = lines[:,1]


# for each start_point, add 1 to the grid at every point between the start_point and corresponding end_point
# user enumerate(start_points) to get the index of the start_point
for i, start_point in enumerate(start_points):
    # get corresponding end_point
    end_point = end_points[i]
    # find direction of line by subtracting start_point from end_point to find the signs
    direction = end_point - start_point
    # divide direction by the absolute value of the direction to find the slope
    slope = direction / np.abs(direction)
    # turn nan to 0
    slope[np.isnan(slope)] = 0
    # convert slope to ints
    slope = slope.astype(int)

    # find the number of steps to take, take max of the x and y + 1
    steps = max(np.abs(direction)) + 1

    # for each step, add 1 to the grid at the start_point + the slope * step
    for step in range(steps):
        grid[start_point[0] + slope[0]*step, start_point[1] + slope[1]*step] += 1


# count the number of points where at least two lines overlap, where the value is greater than 1
print(np.sum(grid > 1))
print(grid.transpose())


