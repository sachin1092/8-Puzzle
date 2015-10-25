import math

PUZZLE_TYPE = 8
MAT_SIZE = int(math.sqrt(PUZZLE_TYPE + 1))

def get_goal():
	goal = []
	for x in xrange(1, PUZZLE_TYPE + 1):
		goal.append(x)
	goal.append(-1)
	return goal

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
		print "\nMoving x up"
		index = mat.index(-1)
		mat[index - MAT_SIZE], mat[index] = mat[index], mat[index - MAT_SIZE]
	else:
		print "\nOperation not allowed"

"""
Performs the move down operation
"""
def move_x_down(mat):
	if can_move_down(mat):
		print "\nMoving x down"
		index = mat.index(-1)
		mat[index + MAT_SIZE], mat[index] = mat[index], mat[index + MAT_SIZE]
	else:
		print "\nOperation not allowed"

"""
Performs the move left operation
"""
def move_x_left(mat):
	if can_move_left(mat):
		print "\nMoving x left"
		index = mat.index(-1)
		mat[index - 1], mat[index] = mat[index], mat[index - 1]
	else:
		print "\nOperation not allowed"

"""
Performs the move down operation
"""
def move_x_right(mat):
	if can_move_right(mat):
		print "\nMoving x right"
		index = mat.index(-1)
		mat[index + 1], mat[index] = mat[index], mat[index + 1]
	else:
		print "\nOperation not allowed"

# def general_search(mat, queueing_func):
# 	# make nodes here
# 	nodes = mat
# 	while True:
# 		if not len(nodes): return None 
# 		node = nodes.pop(0)
# 		if problem.GOAL-TEST(node.STATE) succeeds then return node
# 			nodes = QUEUEING-FUNCTION(nodes, EXPAND(node, problem.OPERATORS))  
	

if __name__ == "__main__":
	# mat = [1, 2, 3, -1]
	mat = [1, 2, 3, 4, 5, 6, 7, 8, -1]
	# mat = [1, 2, 3, 4, 5, 6, 7, 8, -1, 9, 10, 11, 12, 13, 14, 15]
	goal = get_goal()
	print "Initial State",
	print_board(mat)
	print "Goal State",
	print_board(goal)
	# TODO remove this later
	# print "Enter elements for %d Puzzle." % PUZZLE_TYPE
	# print "NOTE: Use \"x\" for blank.\n"
	# for i in xrange(MAT_SIZE):
		# print "Enter elements for row %d" % (i + 1)
		# mat.extend([-1 if x == "x" else int(x) for x in raw_input().split()])
	print "can move up? ", can_move_up(mat)
	print "can move down? ", can_move_down(mat)
	print "can move left? ", can_move_left(mat)
	print "can move right? ", can_move_right(mat)
	move_x_up(mat)
	print_board(mat)
	move_x_up(mat)
	print_board(mat)

	move_x_down(mat)
	print_board(mat)
	move_x_down(mat)
	print_board(mat)

	move_x_left(mat)
	print_board(mat)
	move_x_left(mat)
	print_board(mat)

	move_x_right(mat)
	print_board(mat)
	move_x_right(mat)
	print_board(mat)
