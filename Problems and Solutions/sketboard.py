# Problem Description

#The amusement park at Patagonia has introduced a new skateboard competition. The skating surface is a grid of N x N squares. Most squares are so constructed
#with slopes that it is possible to direct the skateboard in any of up to three directions of the possible four (North , East, South or West, represented by the letters N, E, S and W respectively). Some squares however have a deep drop from the adjacent square from which it is impossible to go to any adjacent square. These are represented by D (for Drop) in that square. The objective is to maneuver the skateboard to reach the South East corner of the grid, marked F.
#Each contestant is given a map of the grid, which shows where the Drop squares are (marked D), where the Final destination is (marked F), and, for each other
#square, the directions it is possible to maneuver the skateboard in that square.

#The contestant draws lots to determine which of the squares on the boundaries of the grid on the North or the West of the grid (the top or the left in the diagram) he
#or she should start in. Then, using a map of the grid, he or she needs to try to reach the South East corner destination by maneuvering the skateboard.



#In some cases, it is impossible to reach the destination. For example, in the diagram above, if one starts at the North East corner (top right in the diagram), the only way is to go is South, until the Drop square is reached (three squares South), and the contestant is stuck there.

#A contestant asks you to figure out the number of squares at the North or West boundary (top or left boundary in the map) from which it is feasible to reach the
#Destination.

#- Constraints

#5<=N<=50

#Input Format

#The first line of the input is a positive integer N, which is the number of squares in each side of the grid.

#The next N lines have a N strings of characters representing the contents of the map for that corresponding row. Each string may be F, representing the Final
#destination, D, representing a drop square, or a set of up to three of the possible four directions (N,E,S,W) in some random order. These represent the directions in
#which the contestant can maneuver the skateboard when in that square.

#- Output

#The output is one line with the number of North or West border squares from which there is a safe way to maneuver the skateboard to the final destination.

#- Explanation

#Example 1

#Input
#6
#ES,ES.SE.ES.ES.S
#SE,ES,SE,ES,ES,S
#ES,ES,SE,ES,SE,S
#ES,SE,ES,SE,E,D
#SE,ES,D,WSE,NES,NS
#E,E,NE,E,E,F

#Output
#9
#Explanation
#N=6, and the size of the grid is 6x6. The map of the grid is as below.



#There are many ways to maneuver the skateboard. For example, if the contestant starts from the North West corner (top left in the map) and goes East all the way
#until he reaches the top right corner in the map, and then goes South, he will reach a Drop square. But if he goes South all the way from the same square until he
#reaches the bottom left square on the map, and keeps going East from there, the Final destination will be reached. Hence the top left square (1,1) is safe.

#Similarly, from the square (1,5), all the paths lead to a drop square. , The other 9 North and West border squares have ways skateboard to get to the final destination.
#The output is 9

class box(object):
	"""docstring for box"""
	def __init__(self, val):
		super(box, self).__init__()
		self.visited = False
		self.val = val
		self.isSafe = False
	def __repr__(self):
		return str(self.isSafe)

	def setSafe(self):
		if self.val != "D" :
			self.visited = True
			self.isSafe = True


def callOn(i, j):
	if (i-1 >= 0) and (not matrix[i-1][j].visited) and  ("S" in matrix[i-1][j].val):
			matrix[i-1][j].setSafe()
			callOn( i-1, j)

	if (i+1 < n) and (not matrix[i+1][j].visited) and  ("N" in matrix[i+1][j].val):
			matrix[i+1][j].setSafe()
			callOn( i+1, j)

	if (j-1 >=0) and (not matrix[i][j-1].visited) and  ("E" in matrix[i][j-1].val):
			matrix[i][j-1].setSafe()
			callOn( i, j-1)

	if (j+1 < n) and (not matrix[i][j+1].visited) and  ("W" in matrix[i][j+1].val):
			matrix[i][j+1].setSafe()
			callOn( i, j+1)
	pass
matrix= []
findF = True;
finalPosition = []
n = int(input())
for x in range(n):
	ar = input().split(",")
	for j, el in enumerate(ar):
		if el == "F":
			finalPosition = [x,j]
			findF = False
		ar[j] = box( ar[j] )

	matrix.append( ar )

callOn( finalPosition[0], finalPosition[1] )
# [i,j] = finalPosition
# pprint( matrix[i-1][j].visited )
count = 0
if matrix[0][0].isSafe == True:
	count = 1 

for i in range(1,n):
	if matrix[0][i].isSafe == True:
		count += 1
	if matrix[i][0].isSafe == True:
		count += 1

print(count)
