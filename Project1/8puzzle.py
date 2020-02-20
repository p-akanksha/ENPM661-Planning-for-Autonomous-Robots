"""
ENPM661-Planning-for-Autonomous-Robots
Project 1

Author(s): 
Akanksha Patel
M.Eng in Robotics,
University of Maryland, College Park
"""

import numpy as np
from collections import deque


# def getValidMoves(p, q, N):

def flattenState(initial_state):
	'''
	Returns a numeric form of state.
	For state: [1,4,7,2,5,8,3,6,0]
	returns 147258360
	'''
	num = 0

	for i in range(9):
		num = 10*num + initial_state[i]

	return num;

def unFlattenState(num):
	'''
	Given the numeric form returns state in array form
	'''
	state = [-1] * 9

	for i in range(8, -1, -1):
		state[i] = int(num % 10)
		num = int(num / 10)

	return state;

def getBlankTilePosition (state):
	'''
	Get the position of blank tile (row, column)
	'''
	l = len(state)
	n = -1

	for i in range(l):
		if (state[i] == 0):
			n = i
			break 

	if(n == -1):
		print("Where is the blank tile??")
	
	j = int(n / 3)
	i = int(n % 3)

	return (i, j)

def getValidMoves(pos):
	'''
	Get a list of valid moves for a given blank tile location. 
	'''

	r = pos[0]
	c = pos[1]

	valid_moves = []

	if(r > 0):
		valid_moves.append('u')
	if(r < 2):
		valid_moves.append('d')
	if(c > 0):
		valid_moves.append('l')
	if(c < 2):
		valid_moves.append('r')

	return valid_moves

def move(state, move, pos):
	'''
	Move the tiles according to a given move and return the updated state

	Input: 
		state: current state of the board
		move: move to be executed
		pos: position of the blank tile

	Output:
		new_state: state after movement

	'''

	new_state = state.copy()
	n = 3*pos[1] + pos[0]
	r = pos[0]
	c = pos[1]

	if(move == 'u'):
		r = r - 1
	elif(move == 'd'):
		r = r + 1
	elif(move == 'l'):
		c = c - 1
	elif(move == 'r'):
		c = c + 1

	m = 3*c + r

	t = new_state[n]
	new_state[n] = new_state[m]
	new_state[m] = t

	return new_state

def solvabilityCheck(initial_state):
	'''
	Check is the current tile arrangement is solvable and return True if is solvable
	'''

	arr = [0]*9

	for i in range(3):
		for j in range(3):
			arr[3*i + j] = initial_state[3*j + i]

	inv = 0
	for i in range(9):
		for j in range(8, i, -1):
			if (arr[j] < arr[i] and arr[j] != 0):
				inv = inv + 1

	if inv%2 == 0:
		return True
	else:
		return False

def main():

	'''
	States are entered colunm wise. 
	For: +-+-+-+  state would be [1,4,7,2,5,8,3,6,0]
		 |1|2|3|
		 +-+-+-+
		 |4|5|6|
		 +-+-+-+
		 |7|8|0|
		 +-+-+-+
	'''

	# initial_state = [1, 4, 7, 0, 2, 8, 3, 5, 6]
	initial_state = [2, 1, 7, 8, 6, 0, 3, 4, 5]
	# initial_state = [5, 4, 0, 2, 1, 3, 8, 7, 6]
	goal_state = [1, 4, 7, 2, 5, 8, 3, 6, 0]

	nodes = []
	nodes_info = []
	node_path = []

	solvable = solvabilityCheck(initial_state)

	if not solvable:
		print("This arrangement is not solvable")
		return

	goal = False

	q = deque()

	q.append(initial_state)
	nodes.append(initial_state)
	nodes_info.append([0, 0])
	visited = { flattenState(initial_state) : 0}

	print(nodes)
	print(nodes_info)
	print(visited)

	while q:
		state = q.popleft()
		blank_pos = getBlankTilePosition(state)
		moves = getValidMoves(blank_pos)
		index = visited.get(flattenState(state));

		print("Exploring state num: ", index)

		for m in moves:
			new_state = move(state, m, blank_pos)

			if (visited.get(flattenState(new_state)) == None):
				nodes.append(new_state)
				print("Found new state: ", len(nodes)-1)
				nodes_info.append([len(nodes)-1, index])
				visited[flattenState(new_state)] = len(nodes)-1

				if (new_state == goal_state):
					print("Reached goal!!")
					goal = True
					break

				q.append(new_state)

		if goal:
			break

	if not goal:
		print("Goal not found")

	nodes = np.asarray(nodes)
	nodes_info = np.asarray(nodes_info)

	# Backtracking to get the path

	x = nodes_info[len(nodes) -1][0]
	y = nodes_info[len(nodes) -1][1]
	res = []
	res.append(nodes[x])
	res.append(nodes[y])

	while (y != 0):
		y = nodes_info[y][1]
		res.append(nodes[y])

	while res:
		temp = res.pop()
		node_path.append(temp)


	node_path = np.asarray(node_path)
	print(node_path)

	# Save output in a text file
	np.savetxt('Nodes.txt', nodes, fmt='%i')
	np.savetxt('NodesInfo.txt', nodes_info, fmt='%i')
	np.savetxt('nodePath.txt', node_path, fmt='%i')





if __name__ == '__main__':
    main()

