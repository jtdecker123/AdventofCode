inputList = []
while True:
   line = input()
   if line == "'++'":
       break
   else:
       inputList.append(line)

maxScore = 0
maxPos = []
grid = []
for i in inputList:
  grid.append([eval(j) for j in list(i)])

def evalAbove(height, row, col):
  global grid
  global scenicTop
  row -= 1
  if row <= -1:
    return True
  test = grid[row][col]
  if height > test:
    scenicTop += 1
    return evalAbove(height, row, col)
  if height <= test:
    scenicTop += 1
    return False

def evalBelow(height, row, col):
  global grid
  global scenicBottom
  row += 1
  if row >= len(grid):
    return True
  test = grid[row][col]  
  if height > test:
    scenicBottom += 1
    return evalBelow(height, row, col)
  if height <= test:
    scenicBottom += 1
    return False

def evalLeft(height, row, col):
  global grid
  global scenicLeft
  col -= 1
  if col <= -1:
    return True
  test = grid[row][col]  
  if height > test:
    scenicLeft += 1
    return evalLeft(height, row, col)
  if height <= test:
    scenicLeft += 1
    return False

def evalRight(height, row, col):
  global grid
  global scenicRight
  col += 1
  if col >= len(grid[row]):
    return True
  test = grid[row][col]
  if height > test:
    scenicRight += 1
    return evalRight(height, row, col)
  if height <= test:
    scenicRight += 1
    return False

for i in range(0,len(grid)):
  for j in range(0,len(grid[i])):
    scenicTop = 0
    scenicBottom = 0
    scenicLeft = 0
    scenicRight = 0
    evalAbove(grid[i][j],i,j) 
    evalBelow(grid[i][j],i,j)  
    evalLeft(grid[i][j],i,j)  
    evalRight(grid[i][j],i,j)
    score = scenicTop * scenicBottom * scenicLeft * scenicRight
    if score > maxScore:
        maxScore = score
        maxPos = [grid[i][j],i,j]

print(maxPos)
print(maxScore)