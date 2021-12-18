# --- Day 6: Lanternfish ---
# The sea floor is getting steeper. Maybe the sleigh keys got carried this way?
# A massive school of glowing lanternfish swims past. They must spawn quickly to reach such large numbers - maybe exponentially quickly? You should model their growth rate to be sure.
# Although you know nothing about this specific species of lanternfish, you make some guesses about their attributes. Surely, each lanternfish creates a new lanternfish once every 7 days.
# However, this process isn't necessarily synchronized between every lanternfish - one lanternfish might have 2 days left until it creates another lanternfish, while another might have 4. So, you can model each fish as a single number that represents the number of days until it creates a new lanternfish.
# Furthermore, you reason, a new lanternfish would surely need slightly longer before it's capable of producing more lanternfish: two more days for its first cycle.
# So, suppose you have a lanternfish with an internal timer value of 3:
#
# After one day, its internal timer would become 2.
# After another day, its internal timer would become 1.
# After another day, its internal timer would become 0.
# After another day, its internal timer would reset to 6, and it would create a new lanternfish with an internal timer of 8.
# After another day, the first lanternfish would have an internal timer of 5, and the second lanternfish would have an internal timer of 7.
# A lanternfish that creates a new fish resets its timer to 6, not 7 (because 0 is included as a valid timer value). The new lanternfish starts with an internal timer of 8 and does not start counting down until the next day.
#
# Realizing what you're trying to do, the submarine automatically produces a list of the ages of several hundred nearby lanternfish (your puzzle input). For example, suppose you were given the following list:
#
# 3,4,3,1,2
# This list means that the first fish has an internal timer of 3, the second fish has an internal timer of 4, and so on until the fifth fish, which has an internal timer of 2. Simulating these fish over several days would proceed as follows:
#
# Initial state: 3,4,3,1,2
# After  1 day:  2,3,2,0,1
# After  2 days: 1,2,1,6,0,8
# After  3 days: 0,1,0,5,6,7,8
# After  4 days: 6,0,6,4,5,6,7,8,8
# After  5 days: 5,6,5,3,4,5,6,7,7,8
# After  6 days: 4,5,4,2,3,4,5,6,6,7
# After  7 days: 3,4,3,1,2,3,4,5,5,6
# After  8 days: 2,3,2,0,1,2,3,4,4,5
# After  9 days: 1,2,1,6,0,1,2,3,3,4,8
# After 10 days: 0,1,0,5,6,0,1,2,2,3,7,8
# After 11 days: 6,0,6,4,5,6,0,1,1,2,6,7,8,8,8
# After 12 days: 5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8
# After 13 days: 4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8
# After 14 days: 3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
# After 15 days: 2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
# After 16 days: 1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
# After 17 days: 0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
# After 18 days: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8
# Each day, a 0 becomes a 6 and adds a new 8 to the end of the list, while each other number decreases by 1 if it was present at the start of the day.
#
# In this example, after 18 days, there are a total of 26 fish. After 80 days, there would be a total of 5934.
#
# Find a way to simulate lanternfish. How many lanternfish would there be after 80 days?


# Part 1 solution
# function that reads in input from input.txt, it's a list of comma separated integers
def read_input():
    with open("input.txt") as f:
        return [int(x) for x in f.read().split(",")]

# read in input.txt
input = read_input()

# please import numpy
import numpy as np

# create a numpy array of the input
input_array = np.array(input)

# function that takes in a numpy array of integers and returns the number of fish after 80 days
def fishlistUpdateSingleDay(input_array):
    # find the number of zeros in the input array
    zeros = np.count_nonzero(input_array == 0)

    # subtract 1 from all non-zero values
    input_array -= 1

    # turn all neg 1s into 6s
    input_array[input_array == -1] = 6

    # add 8s to the end of the array
    input_array_tmp = np.append(input_array, np.full(zeros, 8))

    return input_array_tmp


    #
    #
    # # iterate over the indices of the fishlist
    # for i in range(len(fishlist)):
    #     # if the fishlist is not empty
    #     if fishlist[i] != 0:
    #         # decrement the fishlist by 1
    #         fishlist[i] -= 1
    #     else:
    #         # add a new fish to the end of the list
    #         fishlist.append(8)
    #         # reset that fish to 6
    #         fishlist[i] = 6
    # # return the updated fishlist
    # return fishlist

# do the update 80 times
for i in range(80):
    # take the input and update it
    input_array = fishlistUpdateSingleDay(input_array)

#print len of array
print(len(input_array))

# --- Part Two ---
# Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?
# After 256 days in the example above, there would be a total of 26984457539 lanternfish!
# How many lanternfish would there be after 256 days?

# part 2 solution
input = read_input()
input_array = np.array(input)

# count number of each number in input_array
counts = np.bincount(input_array)
# convert counts to a list
counts = counts.tolist()

# add 0s until length is 9
while len(counts) < 9:
    counts.append(0)

def updateDay(counts):
    # find number in the 0th index
    zeros = counts[0]

    # remove the 0th index
    counts.pop(0)

    # add zeros to 6th index
    counts[6] += zeros

    # add zeros number of 8s to the end of the list
    counts.append(zeros)

    # return counts
    return counts

# do the update 256 times
for i in range(256):
    # take the input and update it
    updateDay(counts)

# print the sum of the counts
print(sum(counts))

# # maintain a list of length 9 of number of fish at each day
# fishlist = np.zeros(9)
# # count number of fish in input_array that match each index
# for i in range(len(input_array)):
#     # if it equal i, increment the index of the fishlist
#     if input_array[i] == i:
#         fishlist[i % 9] += 1




print(fishlistUpdateSingleDay(input_array))
print(updateDay(counts), sum(counts))