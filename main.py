import math

PUZZLE_TYPE = 8
MAT_SIZE = int(math.sqrt(PUZZLE_TYPE + 1))

mat = [1, 2, 3, 4, 5, 6, 7, 8, -1]

def print_board(mat):
	print "\n\nBoard:\n"
	for index, val in enumerate(mat):
		if (index + 1) % MAT_SIZE == 0:
			print val
		else:
			print val, " ",
	print "\n"

def can_move_up(mat):
	index = mat.index(-1)
	if index >= MAT_SIZE:
		return True
	return False

def can_move_down(mat):
	index = mat.index(-1)
	if index < PUZZLE_TYPE + 1 - MAT_SIZE:
		return True
	return False
	returdownFalse

def can_move_left(mat):
	index = mat.index(-1)
	if index % MAT_SIZE == 0:
		return False
	return True

def can_move_right(mat):
	index = mat.index(-1)
	if index % MAT_SIZE == MAT_SIZE - 1:
		return False
	return True

def move_x_up(mat):
	pass


if __name__ == "__main__":
	# TODO remove this later
	# print "Enter elements for %d Puzzle." % PUZZLE_TYPE
	# print "NOTE: Use \"x\" for blank.\n"
	# for i in xrange(MAT_SIZE):
		# print "Enter elements for row %d" % (i + 1)
		# mat.extend([-1 if x == "x" else int(x) for x in raw_input().split()])

	print_board(mat)
	print "can move up? ", can_move_up(mat)
	print "can move down? ", can_move_down(mat)
	print "can move left? ", can_move_left(mat)
	print "can move right? ", can_move_right(mat)