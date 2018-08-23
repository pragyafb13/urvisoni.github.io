# - Problem Description

#Rotate a given String in specified direction by specified magnitude.

#After each rotation make a note of first character of the rotated String, After all rotation are performed the accumulated first character as noted previously will form another string, say FIRST CHAR STRING.

#Check If FIRST CHAR STRING is an Anagram of any substring of the Original string.

#If yes print "YES" otherwise "NO". Input

#The first line contains the original string s. The second line contains a single integer q. The ith of the next q lines contains character d[i] denoting direction and integer r[i] denoting the magnitude.

#- Constraints

#1 <= Length of original string 30
#1<= q <= 10


#- Output

#YES or NO

#- Explanation

#Example 1

#Input

#Carrace
#3
#L 2
#R 2
#L 3

#Output 

#NO

#Explanation

#After applying all the rotations the FIRSTCHARSTRING string will be “rcr” which is not anagram of any sub string of original string “carrace”.

#Program 

#
















original = input().lower()
total_cases = int(input())

mx = 150
def eq(arr1, arr2):
	for i in range(mx):
		if arr1[i] != arr2[i]:
			return False
	return True

def search(fcs, org):
	cp = [0]*mx
	ct = [0]*mx

	N = len(org)
	M = len(fcs)
		
	for i in range(M):
		cp[ ord(fcs[i]) ] += 1
		ct[ ord(org[i]) ] += 1
 
	for i in range(M,N):
		if eq(cp, ct):
			return True
		ct[ ord(org[i]) ] += 1
		ct[ ord(org[i-M]) ] -= 1

	if eq(cp, ct):
		return True
	return False

l = len(original)
firstCharStr = ""
indexPointer = 0

while ( total_cases ):
	total_cases-=1
	[direction, num] = input().split(" ")
	if direction == "L":
		indexPointer =  (indexPointer + int(num) ) % l
	else:
		indexPointer =  (indexPointer - int(num) ) % l

	firstCharStr+=original[indexPointer]

if search(firstCharStr, original):
	print("YES")
else:
	print("NO")