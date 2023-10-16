import random
import pygame
import sys


class MazeGenerator:
    def generateMaze(self, rows, cols):
        def neighbours(x, y):
            return [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]

        def isValid(x, y):
            return x >= 0 and x < rows and y >= 0 and y < cols

        cells = rows*cols
        visited = set()
        visit2 = []
        queue = [[0, 0]]
        path = []
        while len(visited) < cells:
            x, y = queue[-1]
            visited.add((x, y))
            visit2.append([x, y])
            if x == rows-1 and y == cols-1:
                if len(path) <= 0:
                    for coord in queue:
                        path.append(coord)
            adjCells = []
            for i, j in neighbours(x, y):
                if isValid(i, j) and (i, j) not in visited:
                    adjCells.append([i, j])
            if not adjCells:
                queue.pop()
                continue
            selectedCell = random.choice(adjCells)
            queue.append(selectedCell)
        return visit2, path
    
maze = MazeGenerator()
rows = 20
cols = 20
visit2, path = maze.generateMaze(rows, cols)
print(len(visit2))
# print(path)
cells = rows*cols
pathLength = len(path)
maxPathLength = cells/4
minPathLength = maxPathLength - 10
if cells >= 100:
    while pathLength > maxPathLength or pathLength < minPathLength:
        visit2, path = maze.generateMaze(rows, cols)
        pathLength = len(path)

# pygame
pygame.init()
size = 20
screen = pygame.display.set_mode([cols*size+362, rows*size+162])
clock = pygame.time.Clock()
pygame.display.set_caption("Maze")

GRID_COL = [3, 252, 177]
FADE_COL = [51, 51, 51]


#making the cell class
class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {"top": True, "right": True, "bottom": True, "left": True}
    
    def draw(self):
        x, y = self.x*size, self.y*size
        rect = pygame.Rect(x, y, size, size)
        pygame.draw.rect(screen, [30,30,30], rect)
        pygame.draw.line(screen, FADE_COL, (x, y), (x+size, y), 2)
        pygame.draw.line(screen, FADE_COL, (x, y+size), (x+size, y+size), 2)
        pygame.draw.line(screen, FADE_COL, (x+size, y), (x+size, y+size), 2)
        pygame.draw.line(screen, FADE_COL, (x, y), (x, y+size), 2)
        if self.walls["top"]:
            pygame.draw.line(screen, GRID_COL, (x, y), (x+size, y), 2)
        if self.walls["bottom"]:
            pygame.draw.line(screen, GRID_COL, (x, y+size), (x+size, y+size), 2)
        if self.walls["right"]:
            pygame.draw.line(screen, GRID_COL, (x+size, y), (x+size, y+size), 2)
        if self.walls["left"]:
            pygame.draw.line(screen, GRID_COL, (x, y), (x, y+size), 2)
        

wallMapping = {}
for i in range(rows):
    for j in range(cols):
        wallMapping[(i, j)] = {"top": True, "right": True, "bottom": True, "left": True}

t = pygame.time.get_ticks()
class Token:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.alt = 0
    
    def draw(self):
        x, y = self.x*size, self.y*size
        pygame.draw.ellipse(screen, [103, 252, 3], [x+8, y+8, 6, 6])
        self.alt = 1


def makePath(arr):
    count = 1
    while count < len(arr): 
        prevrow, prevcol = arr[count-1][0], arr[count-1][1]
        currow, curcol = arr[count][0], arr[count][1]
        if currow > prevrow:
            wallMapping[(currow, curcol)]["top"] = False
            wallMapping[(prevrow, prevcol)]["bottom"] = False
        elif currow < prevrow:
            wallMapping[(currow, curcol)]["bottom"] = False
            wallMapping[(prevrow, prevcol)]["top"] = False
        elif curcol > prevcol:
            wallMapping[(currow, curcol)]["left"] = False
            wallMapping[(prevrow, prevcol)]["right"] = False
        elif curcol < prevcol:
            wallMapping[(currow, curcol)]["right"] = False
            wallMapping[(prevrow, prevcol)]["left"] = False
        count += 1

makePath(visit2)
def getWall(i, j):
    dirs = ["left", "right", "top", "bottom"]
    if j == 0:
        dirs.remove("left")
    if j == cols-1:
        dirs.remove("right")
    if i == 0:
        dirs.remove("top")
    if i == rows-1:
        dirs.remove("bottom")
    return random.choice(dirs)

#removing additional walls from the path
removedWalls = 0
for i, j in wallMapping:
    if [i, j] in path:
        toss = random.randint(1, 2)
        if toss == 1:
            wallCount = 0
            for w in wallMapping[(i, j)].values():
                if w:
                    wallCount += 1
            if wallCount >= 2:
                removedWalls += 1
                wall = getWall(i, j)
                wallMapping[(i, j)][wall] = False
print("Removed Walls:",removedWalls)


tokens = []
def getTokens(arr):
    for i in range(rows):
        col1 = random.randint(0, cols-1)
        col2 = random.randint(0, cols-1)
        while col2 == col1:
            col2 = random.randint(0, cols-1)
        arr.append(Token(col1+9, i+4))
        arr.append(Token(col2+9, i+4))
getTokens(tokens)

gridCells = []
for i, j in wallMapping:
    cell = Cell(j+9, i+4)
    cell.walls = wallMapping[(i, j)]
    gridCells.append(cell)

#loading pygame window with a delay
bound = 1
showPath = False
while True:
    t = pygame.time.get_ticks()
    screen.fill([51,51,51])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # showPath = True
            continue
            
    [cell.draw() for cell in gridCells]
    [token.draw() for token in tokens]

    if showPath:
        for i, j in path[:bound]:
            rect = pygame.Rect(189 + j*size, 89 + i*size, 4, 4)
            pygame.draw.rect(screen, [255,255,255], rect)

        pygame.time.delay(100)
        if bound < len(path):
            bound += 1
    clock.tick(30)
    pygame.display.flip()

