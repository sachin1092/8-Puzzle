import math

PUZZLE_TYPE = 8
MAT_SIZE = int(math.sqrt(PUZZLE_TYPE + 1))

class Node(object):
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

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
		Problem.print_board(self.current_state)

	"""
	Print the current state of board
	"""
	@staticmethod
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
	def can_move_up(self):
		return True if self.current_state.index(-1) >= MAT_SIZE else False

	"""
	Check if move down operation is possible
	"""
	def can_move_down(self):
		return True if self.current_state.index(-1) < PUZZLE_TYPE + 1 - MAT_SIZE else False

	"""
	Check if move left operation is possible
	"""
	def can_move_left(self):
		return False if self.current_state.index(-1) % MAT_SIZE == 0 else True

	"""
	Check if move right operation is possible
	"""
	def can_move_right(self):
		return False if self.current_state.index(-1) % MAT_SIZE == MAT_SIZE - 1 else True

	"""
	Performs the move up operation
	"""
	def move_x_up(self):
		if self.can_move_up():
			print "\nMoving x up"
			index = self.current_state.index(-1)
			self.current_state[index - MAT_SIZE], self.current_state[index] = self.current_state[index], self.current_state[index - MAT_SIZE]
		else:
			print "\nOperation not allowed"

	"""
	Performs the move down operation
	"""
	def move_x_down(self):
		if self.can_move_down():
			print "\nMoving x down"
			index = self.current_state.index(-1)
			self.current_state[index + MAT_SIZE], self.current_state[index] = self.current_state[index], self.current_state[index + MAT_SIZE]
		else:
			print "\nOperation not allowed"

	"""
	Performs the move left operation
	"""
	def move_x_left(self):
		if self.can_move_left():
			print "\nMoving x left"
			index = self.current_state.index(-1)
			self.current_state[index - 1], self.current_state[index] = self.current_state[index], self.current_state[index - 1]
		else:
			print "\nOperation not allowed"

	"""
	Performs the move down operation
	"""
	def move_x_right(self):
		if self.can_move_right():
			print "\nMoving x right"
			index = self.current_state.index(-1)
			self.current_state[index + 1], self.current_state[index] = self.current_state[index], self.current_state[index + 1]
		else:
			print "\nOperation not allowed"

# def general_search(problem, queueing_func):
# 	# make nodes here
# 	nodes = [problem.get_current_state()]
# 	while True:
# 		if not len(nodes): return None 
# 		node = nodes.pop(0)
# 		if problem.goal_test(): 
# 			return node
# 		nodes = QUEUEING-FUNCTION(nodes, EXPAND(node, problem.OPERATORS))  
	

if __name__ == "__main__":
	# mat = [1, 2, 3, -1]
	mat = [1, 2, 4, 7, 5, -1, 3, 6, 8]
	# mat = [1, 2, 3, 4, 5, 6, 7, 8, -1, 9, 10, 11, 12, 13, 14, 15]
	problem = Problem(mat)
	print "Initial State",
	problem.print_current_board()
	print "Goal State",
	Problem.print_board(problem.get_goal_state())
	# TODO remove this later
	# print "Enter elements for %d Puzzle." % PUZZLE_TYPE
	# print "NOTE: Use \"x\" for blank.\n"
	# for i in xrange(MAT_SIZE):
		# print "Enter elements for row %d" % (i + 1)
		# mat.extend([-1 if x == "x" else int(x) for x in raw_input().split()])
	print "can move up? ", problem.can_move_up()
	print "can move down? ", problem.can_move_down()
	print "can move left? ", problem.can_move_left()
	print "can move right? ", problem.can_move_right()
	problem.move_x_up()
	problem.print_current_board()
	problem.move_x_up()
	problem.print_current_board()

	problem.move_x_down()
	problem.print_current_board()
	problem.move_x_down()
	problem.print_current_board()

	problem.move_x_left()
	problem.print_current_board()
	problem.move_x_left()
	problem.print_current_board()

	problem.move_x_right()
	problem.print_current_board()
	problem.move_x_right()
	problem.print_current_board()
