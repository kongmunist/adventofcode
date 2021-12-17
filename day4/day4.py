# --- Day 4: Giant Squid ---

# You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.
# Maybe it wants to play bingo?
# Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)
# The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:
# At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).
# The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.
# To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?


# Read in input.txt
with open('input.txt', 'r') as f:
    # the first line is a list of numbers that get called out in bingo
    bingo_numbers = [int(x) for x in f.readline().split(',')]




    # the rest of the lines are the 5x5 bingo boards separated by newlines
    boards = []
    for line in f:
        # if line is blank, skip it
        if line == '\n':
            continue
        # otherwise, add the line to the list of boards
        boards.append(line.strip())

    # Split each line into a list of numbers
    for i in range(len(boards)):
        boards[i] = [int(x) for x in boards[i].split()]

    # split boards into groups of 5
    boards = [boards[i:i+5] for i in range(0, len(boards), 5)]
    # split each list of strings in boards into a lists of numbers




# now please import numpy
import numpy as np
# convert boards to numpy arrays
boards = np.array(boards)
