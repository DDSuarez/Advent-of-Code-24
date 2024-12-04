# variable setup
data = []
pOneAns = 0
pTwoAns = 0
demoInput = "inputs/twodemo.txt"
input = "inputs/two.txt"

# read the input file and save each column to a list
# strip used to remove the new line character from column two
f = open(demoInput, "r")
for x in f:
    currRow = x.split("   ")
    currRow = currRow[-1].strip()
    for i in range(len(currRow)):
        if currRow[i] < currRow[i + 1]:
            print("We should be increasing")

print(data)
