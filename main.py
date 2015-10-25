import math

PUZZLE_TYPE = 8
MAT_SIZE = math.sqrt(PUZZLE_TYPE + 1)

mat = []

def print_board(mat):
	print "\n\nBoard:\n"
	for index, val in enumerate(mat):
		if (index + 1) % MAT_SIZE == 0:
			print val
		else:
			print val, " ",

def move_x_up(mat):
	

if __name__ == "__main__":
	print "Enter elements for %d Puzzle." % PUZZLE_TYPE
	print "NOTE: Use \"x\" for blank.\n"
	for i in xrange(int(MAT_SIZE)):
		print "Enter elements for row %d" % (i + 1)
		mat.extend([-1 if x == "x" else int(x) for x in raw_input().split()])

	print_board(mat)