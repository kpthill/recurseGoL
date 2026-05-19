# Game of Life
# Patrick and Seyoung

# rules:
# on each step, for each cell:
# - if live:
#   - 0-1 or >3 live neighbors dies
#   - 2-3 live neighbors lives
# - if dead:
#   - exactly 3 live neighbors, becomes alive
#   - otherwise stays dead

# startgrid = [
#     [False, False, False, False, False, False, False, False, False, False, False, False, False, ],
#     [False, False, False, False, False, False, False, False, False, False, False, False, False, ],
#     [False, False, False, False, False, False, False, False, False, False, False, False, False, ],
#     [False, False, False, False, False, False, True, False, False , False, False, False, False, ],
#     [False, False, False, False, True, False, True, False, False  , False, False, False, False, ],
#     [False, False, False, False, False, True, True, False, False  , False, False, False, False, ],
#     [False, False, False, False, False, False, False, False, False, False, False, False, False, ],
#     [False, False, False, False, False, False, False, False, False, False, False, False, False, ],
#     [False, False, False, False, False, False, False, False, False, False, False, False, False, ],
#     [False, False, False, False, False, False, False, False, False, False, False, False, False, ],
#     [False, False, False, False, False, False, False, False, False, False, False, False, False, ],
# ]


# blinker = [
#     [False, True, False],
#     [False, True, False],
#     [False, True, False],
#     ]

pulsar = [
    [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,],
    [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,],
    [False,False,False,False,True,True,True,False,False,False,True,True,True,False,False,False,False,],
    [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,],
    [False,False,True,False,False,False,False,True,False,True,False,False,False,False,True,False,False,],
    [False,False,True,False,False,False,False,True,False,True,False,False,False,False,True,False,False,],
    [False,False,True,False,False,False,False,True,False,True,False,False,False,False,True,False,False,],
    [False,False,False,False,True,True,True,False,False,False,True,True,True,False,False,False,False,],
    [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,],
    [False,False,False,False,True,True,True,False,False,False,True,True,True,False,False,False,False,],
    [False,False,True,False,False,False,False,True,False,True,False,False,False,False,True,False,False,],
    [False,False,True,False,False,False,False,True,False,True,False,False,False,False,True,False,False,],
    [False,False,True,False,False,False,False,True,False,True,False,False,False,False,True,False,False,],
    [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,],
    [False,False,False,False,True,True,True,False,False,False,True,True,True,False,False,False,False,],
    [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,],
    [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,],
]

# startgrid = [
#     [False, False, True, False, False],
#     [True, False, True, False, False],
#     [False, True, True, False, False],
# ]

def displayGrid(grid, generation):
    print(f"Generation {generation}")
    for line in grid:
        lineString = ''.join(["x" if present else "." for present in line])
        print(lineString)

def evolveGrid(grid):
    newgrid = [[cell for cell in row] for row in grid] # deep copy
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            liveN = countLiveNeighbors(grid, row, col);
            if (grid[row][col]):
                newgrid[row][col] = liveN in [2,3]
            else:
                newgrid[row][col] = liveN in [3]
    return newgrid

def countLiveNeighbors(grid, row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i == 0 and j == 0):
                continue
            if (liveAt(grid, row + i, col + j)):
                count+=1
    return count

def liveAt(grid, row, col):
    if row >= len(grid) or row < 0:
        return False
    if col >= len(grid[row]) or col < 0:
        return False
    return grid[row][col]

def main():
    currentGrid = pulsar
    generation = 0

    # clearGrid(currentGrid)

    displayGrid(currentGrid, generation)
    while(True):
        input()
        generation+=1
        currentGrid = evolveGrid(currentGrid)
        clearGrid(currentGrid)
        displayGrid(currentGrid, generation)

def clearGrid(grid):
    print(f"\x1b[{len(grid)+3}A")

main()
