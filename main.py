import math
from random import shuffle

PUZZLE_TYPE = 3
MAT_SIZE = int(math.sqrt(PUZZLE_TYPE + 1))

class Problem(object):

	def __init__(self, initial_state=None):
		self.current_state = initial_state
		self.goal_state = self.get_goal()

	def goal_test():
		return self.current_state == self.goal_state

	def get_current_state(self):
		return self.current_state

	def get_goal_state(self):
		return self.goal_state

	def get_goal(self):
		goal = []
		for x in xrange(1, PUZZLE_TYPE + 1):
			goal.append(x)
		goal.append(-1)
		return goal

	def print_current_board(self):
		print_board(self.current_state)

"""
Print the current state of board
"""
def print_board(mat):
	print "\nBoard:"
	print "*" * 5 * MAT_SIZE
	for index, val in enumerate(mat):
		if (index + 1) % MAT_SIZE == 0:
			print val if val != -1 else "x"
		else:
			print val if val != -1 else "x", " ",
	print "*" * 5 * MAT_SIZE

"""
Check if move up operation is possible
"""
def can_move_up(mat):
	return True if mat.index(-1) >= MAT_SIZE else False

"""
Check if move down operation is possible
"""
def can_move_down(mat):
	return True if mat.index(-1) < PUZZLE_TYPE + 1 - MAT_SIZE else False

"""
Check if move left operation is possible
"""
def can_move_left(mat):
	return False if mat.index(-1) % MAT_SIZE == 0 else True

"""
Check if move right operation is possible
"""
def can_move_right(mat):
	return False if mat.index(-1) % MAT_SIZE == MAT_SIZE - 1 else True

"""
Performs the move up operation
"""
def move_x_up(mat):
	if can_move_up(mat):
		# print "\nMoving x up"
		index = mat.index(-1)
		mat[index - MAT_SIZE], mat[index] = mat[index], mat[index - MAT_SIZE]
		return mat
		# print "\nOperation not allowed"
	return None

"""
Performs the move down operation
"""
def move_x_down(mat):
	if can_move_down(mat):
		# print "\nMoving x down"
		index = mat.index(-1)
		mat[index + MAT_SIZE], mat[index] = mat[index], mat[index + MAT_SIZE]
		return mat
		# print "\nOperation not allowed"
	return None

"""
Performs the move left operation
"""
def move_x_left(mat):
	if can_move_left(mat):
		# print "\nMoving x left"
		index = mat.index(-1)
		mat[index - 1], mat[index] = mat[index], mat[index - 1]
		return mat
		# print "\nOperation not allowed"
	return None

"""
Performs the move down operation
"""
def move_x_right(mat):
	if can_move_right(mat):
		# print "\nMoving x right"
		index = mat.index(-1)
		mat[index + 1], mat[index] = mat[index], mat[index + 1]
		return mat
	return None

def general_search(problem, queueing_func):
	nodes = [problem.get_current_state()]
	while len(nodes):
		node = nodes.pop(0)
		if problem.goal_test(): 
			return node
		queueing_func(nodes, expand(node))  
	
def expand(node):
	all_nodes = []
	node1 = move_x_up(node)
	node2 = move_x_down(node)
	node3 = move_x_left(node)
	node4 = move_x_right(node)
	if node1:
		all_nodes.append(node1)
	if node2:
		all_nodes.append(node2)
	if node3:
		all_nodes.append(node3)
	if node4:
		all_nodes.append(node4)
	return all_nodes

def uniform_cost_search(nodes, new_nodes):
	nodes.extends(new_nodes)

def calculate_misplaced(node):
	count = 0
	for i in xrange(PUZZLE_TYPE):
		if i != node[i]:
			count += 1
	return count

def misplaced_tile_heuristic(nodes, new_nodes):
	pass

def manhattan_distance_heuristic(nodes, new_nodes):
	pass

if __name__ == "__main__":
	# mat = [1, 2, 3, -1]
	# mat = [1, 2, 4, 7, 5, -1, 3, 6, 8]
	# mat = [1, 2, 3, 4, 5, 6, 7, 8, -1, 9, 10, 11, 12, 13, 14, 15]
	# TODO remove this later
	print "Welcome to the awesome %d-puzzle solver." % PUZZLE_TYPE
	print "Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle."
	choice = int(raw_input())
	mat = []
	if choice == 1:
		for i in xrange(PUZZLE_TYPE):
			mat.append(i + 1)
		mat.append(-1)
		shuffle(mat)
	elif choice == 2:
		print "Enter elements for %d Puzzle." % PUZZLE_TYPE
		print "NOTE: Use \"x\" for blank.\n"
		for i in xrange(MAT_SIZE):
			print "Enter elements for row %d" % (i + 1)
			mat.extend([-1 if x == "x" else int(x) for x in raw_input().split()])

	problem = Problem(mat)
	print "Initial State",
	problem.print_current_board()
	print "Goal State",
	print_board(problem.get_goal_state())
	# print "can move up? ", can_move_up(problem.get_current_state())
	# print "can move down? ", can_move_down(problem.get_current_state())
	# print "can move left? ", can_move_left(problem.get_current_state())
	# print "can move right? ", can_move_right(problem.get_current_state())
	# move_x_up(problem.get_current_state())
	# problem.print_current_board()
	# move_x_up(problem.get_current_state())
	# problem.print_current_board()

	# move_x_down(problem.get_current_state())
	# problem.print_current_board()
	# move_x_down(problem.get_current_state())
	# problem.print_current_board()

	# move_x_left(problem.get_current_state())
	# problem.print_current_board()
	# move_x_left(problem.get_current_state())
	# problem.print_current_board()

	# move_x_right(problem.get_current_state())
	# problem.print_current_board()
	# move_x_right(problem.get_current_state())
	# problem.print_current_board()
