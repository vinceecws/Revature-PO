import numpy as np

'''
Python:

Create a function that determines whether each seat can "see" the front-stage. A number can "see" the front-stage if it is strictly greater than the number before it.

Everyone can see the front-stage in the example below:

# FRONT STAGE
[[1, 2, 3, 2, 1, 1],
[2, 4, 4, 3, 2, 2],
[5, 5, 5, 5, 4, 4],
[6, 6, 7, 6, 5, 5]]

# Starting from the left, the 6 > 5 > 2 > 1, so all numbers can see.
# 6 > 5 > 4 > 2 - so all numbers can see, etc.
Not everyone can see the front-stage in the example below:

# FRONT STAGE
[[1, 2, 3, 2, 1, 1],
[2, 4, 4, 3, 2, 2],
[5, 5, 5, 10, 4, 4],
[6, 6, 7, 6, 5, 5]]

# The 10 is directly in front of the 6 and blocking its view.
The function should return True if every number can see the front-stage, and False if even a single number cannot.

Examples:
can_see_stage([
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]) -> True

can_see_stage([
[0, 0, 0],
[1, 1, 1],
[2, 2, 2]
]) -> True

can_see_stage([
[2, 0, 0],
[1, 1, 1],
[2, 2, 2]
]) -> False

can_see_stage([
[1, 0, 0],
[1, 1, 1],
[2, 2, 2]
]) -> False

# Number must be strictly smaller than
# the number directly behind it.

Notes:
Numbers must be strictly greater than the number in front of it.
All numbers within the lists will be whole numbers greater than or equal to zero.
'''

def can_see_stage(seating):
	'''
		The problem can be simplified into finding whether an array is column-wise increasing

		Constraint:
		Given the seating array X, each X[i,j] >= 0 and is an integer

		Assumption:
		The seating array consists of 2 or more rows.

		Solution:
		1) Get the row-wise difference for all adjacent rows
		2) If all values in the difference matrix > 0, then all seats are strictly column-wise increasing. Otherwise, one or more pairs are not.

	'''
	return all([i > 0 for i in (np.array(seating[1:]) - np.array(seating[:-1])).flatten()])

if __name__ == '__main__':

	assert can_see_stage([
			[1, 2, 3],
			[4, 5, 6],
			[7, 8, 9]
		]) == True, "Wrong answer"

	assert can_see_stage([
			[0, 0, 0],
			[1, 1, 1],
			[2, 2, 2]
		]) == True, "Wrong answer"

	assert can_see_stage([
			[2, 0, 0],
			[1, 1, 1],
			[2, 2, 2]
		]) == False, "Wrong answer"

	assert can_see_stage([
			[1, 0, 0],
			[1, 1, 1],
			[2, 2, 2]
		]) == False, "Wrong answer"
