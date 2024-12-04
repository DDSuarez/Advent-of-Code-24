# variable setup
colOne = []
colTwo = []
pOneAns = 0
pTwoAns = 0
demoInput = "inputs/onedemo.txt"
input = "inputs/one.txt"

# read the input file and save each column to a list
# strip used to remove the new line character from column two
f = open(input, "r")
for x in f:
    currRow = x.split("   ")
    colOne.append(currRow[0])
    colTwo.append(currRow[1].strip())

# convert string lists to int
colOne = [int(x) for x in colOne]
colTwo = [int(x) for x in colTwo]

#print(colOne)
#print(colTwo)

# Part Two - finds the similarity score
# easier to do this now before removing the elements for part one's calculation
# loop through colOne and add the current number times it's count in colTwo to the part two answer
for i in colOne:
    #print(i)
    pTwoAns += i * colTwo.count(i)

# Part One - finds the total difference
# while the lists aren't empty, get the min of each, subtract them,
# absolute value them to make it positive, add to the part one answer,
# then remove the current min value from the lists
while colOne and colTwo:
    minOne = min(colOne)
    minTwo = min(colTwo)
    pOneAns += abs(minOne - minTwo)
    colOne.remove(minOne)
    colTwo.remove(minTwo)

print(f"Day 1 Part 1: The total distance is {pOneAns}.")

print(f"Day 1 Part 2: The similarity score is {pTwoAns}.")
