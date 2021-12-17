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

# Done with reading in input.txt
# Now, let's find the winning board

# First, make a function that checks if a numpy array board has a complete row or column
def check_row_or_column(board):
    # check if any row or column is complete
    for i in range(5):
        # check if any row is complete
        if np.all(board[i,:]):
            return True
        # check if any column is complete
        if np.all(board[:,i]):
            return True
    return False

# Function that checks if any board is complete, and returns the index of the winning board
def check_complete(boards):
    for i in range(len(boards)):
        if check_row_or_column(boards[i]):
            return i
    return None


# make corresponding numpy arrays of falses matching the shape of each board
complete_boards = np.zeros(boards.shape, dtype=bool)

# now, loop through the bingo numbers, and mark off boards that have them
for number in bingo_numbers:
    # mark off the boards that have the number
    complete_boards[boards == number] = True

    # Now check if any board is complete
    winning_board = check_complete(complete_boards)
    if winning_board is not None:
        # if so, print the score
        # The score is the sum of all unmarked numbers on that board, times the number that was just called
        # unmarked numbers are numbers where complete_boards[i,j] == False
        score = np.sum(boards[winning_board][complete_boards[winning_board] == False]) * number
        print(score)
        break

########################################################################################################################
# Part 2
# On the other hand, it might be wise to try a different strategy: let the giant squid win.
# You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.
# In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

# Figure out which board will win last. Once it wins, what would its final score be?

# Solution
# The solution is the same as before, except now you're looking for the last board to win.

# New check_complete function that takes in a list of indices to ignore
def check_complete2(boards, ignore_indices):
    for i in range(len(boards)):
        if i in ignore_indices:
            continue
        if check_row_or_column(boards[i]):
            return i


# Make corresponding numpy arrays of falses matching the shape of each board
complete_boards = np.zeros(boards.shape, dtype=bool)

# now, loop through the bingo numbers, and mark off boards that have that number, and remove completed boards from boards
# keep track of boards that won
winning_boards = []
# track last number called
last_number = None

for number in bingo_numbers:
    # mark off the boards that have the number
    complete_boards[boards == number] = True

    # Now check if any board is complete
    winning_board = check_complete2(complete_boards, winning_boards)
    while winning_board is not None:
        # if so, add it to the list of winning boards
        winning_boards.append(winning_board)

        # Now check if any board is complete
        winning_board = check_complete2(complete_boards, winning_boards)

    # if all boards are complete, break
    if len(winning_boards) == len(boards):
        last_number = number
        break


print(winning_boards)

# The last board to win is the last one in the list
winning_board = winning_boards[-1]
# calcualte the score of that board
score = np.sum(boards[winning_board][complete_boards[winning_board] == False]) * last_number
print(score)


