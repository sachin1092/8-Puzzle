import math

PUZZLE_TYPE = 8
MAT_SIZE = int(math.sqrt(PUZZLE_TYPE + 1))

def print_board(mat):
	print "\nBoard:"
	print "*"*15
	for index, val in enumerate(mat):
		if (index + 1) % MAT_SIZE == 0:
			print val if val != -1 else "x"
		else:
			print val if val != -1 else "x", " ",
	print "*"*15

def can_move_up(mat):
	return True if mat.index(-1) >= MAT_SIZE else False

def can_move_down(mat):
	return True if mat.index(-1) < PUZZLE_TYPE + 1 - MAT_SIZE else False

def can_move_left(mat):
	return False if mat.index(-1) % MAT_SIZE == 0 else True

def can_move_right(mat):
	return False if mat.index(-1) % MAT_SIZE == MAT_SIZE - 1 else True

def move_x_up(mat):
	if can_move_up(mat):
		print "\nMoving x up"
		index = mat.index(-1)
		mat[index - MAT_SIZE], mat[index] = mat[index], mat[index - MAT_SIZE]
	else:
		print "\nOperation not allowed"

def move_x_down(mat):
	if can_move_down(mat):
		print "\nMoving x down"
		index = mat.index(-1)
		mat[index + MAT_SIZE], mat[index] = mat[index], mat[index + MAT_SIZE]
	else:
		print "\nOperation not allowed"


if __name__ == "__main__":
	mat = [1, 2, 3, -1, 4, 5, 6, 7, 8]
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
	move_x_up(mat)
	print_board(mat)
	move_x_up(mat)
	print_board(mat)
	move_x_down(mat)
	print_board(mat)
	move_x_down(mat)
	print_board(mat)
