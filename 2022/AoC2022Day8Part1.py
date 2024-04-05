inputList = []
while True:
   line = input()
   if line == "'++'":
       break
   else:
       inputList.append(line)

trueCount = 0
grid = []
for i in inputList:
  grid.append([eval(j) for j in list(i)])

def evalAbove(height, row, col):
  global grid
  row -= 1
  if row <= -1:
    return True
  test = grid[row][col]
  if height > test:
    return evalAbove(height, row, col)
  if height <= test:
    return False

def evalBelow(height, row, col):
  global grid
  row += 1
  if row >= len(grid):
    return True
  test = grid[row][col]  
  if height > test:
    return evalBelow(height, row, col)
  if height <= test:
    return False

def evalLeft(height, row, col):
  global grid
  col -= 1
  if col <= -1:
    return True
  test = grid[row][col]  
  if height > test:
    return evalLeft(height, row, col)
  if height <= test:
    return False

def evalRight(height, row, col):
  global grid
  col += 1
  if col >= len(grid[row]):
    return True
  test = grid[row][col]
  if height > test:
    return evalRight(height, row, col)
  if height <= test:
    return False

for i in range(1,len(grid)-1):
  for j in range(1,len(grid[i])-1):
    if evalAbove(grid[i][j],i,j) or evalBelow(grid[i][j],i,j) or evalLeft(grid[i][j],i,j) or evalRight(grid[i][j],i,j):
      trueCount +=1

exterior = 2*(len(grid)) + 2*(len(grid[0])-2)
trueCount += exterior
print(trueCount)