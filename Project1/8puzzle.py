"""
ENPM661-Planning-for-Autonomous-Robots
Project 1

Author(s): 
Akanksha Patel
M.Eng in Robotics,
University of Maryland, College Park
"""

import numpy as np


# def getValidMoves(p, q, N):
	


def getFlattenState(initial_state):
	num = 0

	for j in range(3):
		for i in range(3):
			num = 10*num + initial_state[i][j]

	return num;

def main():
	initial_state = [[1, 0, 3],
					 [4, 2, 5],
					 [7, 8, 6]]
	goal_state = [[1, 2, 3], 
				  [4, 5, 6],
				  [7, 8, 0]]

	flat_state = getFlattenState(initial_state)

	print(flat_state)

	# Save state index in an array

	index_to_state = []
	index_to_state.append(initial_state)

	# Dict to keep a track of all the nodes visited
	# Add a variable path to dict (not recursion required)


	state_to_index = {flat_state : 0}

	# print(type(state_to_index))


	# Queue to keep a track of all the nodes to visit next





if __name__ == '__main__':
    main()

