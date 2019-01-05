import numpy
from heapq import *

WALKABLE_TILE = 0
NOT_WALKABLE_TILE = 1
STAIRS_UP = 10
STAIRS_DOWN = 11
STAIRS_BOTH = 12
STAIRS = {STAIRS_UP, STAIRS_BOTH}
START = 100
END = 101

GO_NORTH = 1
GO_WEST = 2
GO_SOUTH = 3
GO_EAST = 4
CLIMB_UP = 5
CLIMB_DOWN = 6

def heuristic(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

def astar(array, start, goal):
    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]

    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:heuristic(start, goal)}
    oheap = []

    heappush(oheap, (fscore[start], start))
    
    while oheap:

        current = heappop(oheap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j            
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:                
                    if array[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    continue
            else:
                continue
                
            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue
                
            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heappush(oheap, (fscore[neighbor], neighbor))
                
    return False


def get_positions(vals, floor):
    positions = []    
    for row_index, row in enumerate(floor):
        positions_in_row = [(row_index, col_index) for col_index, x in enumerate(row) if x in vals]
        if len(positions_in_row) > 0:
            positions.extend(positions_in_row)
    return positions


def get_command(drow, dcol):
    if drow == 1:
        return GO_SOUTH
    elif drow == -1:
        return GO_NORTH
    elif dcol == 1:
        return GO_EAST
    else:
        return GO_WEST

def path_to_commands(path):
    commands = []
    for i in range(1, len(path)):
        row1, col1 = path[i-1]
        row2, col2 = path[i]
        drow, dcol = row2-row1, col2-col1
        commands.append(get_command(drow, dcol))
    return commands

def _find_shortest_path(floors, start, floor_index):
    targets = []
    is_last_floor = floor_index == len(floors) - 1
    if is_last_floor:
        targets = get_positions({END}, floors[floor_index])
    else:
        targets = get_positions(STAIRS, floors[floor_index])
    
    paths = []
    for target in targets:
        path = astar(numpy.array(floors[floor_index]), start, target)
        if not path:
            continue
        path.reverse()
        if not is_last_floor:
            next_path = _find_shortest_path(floors, target, floor_index + 1)
            if next_path is None:
                continue
            path.extend(next_path)
        paths.append(path)
    return None if len(paths) == 0 else min(paths, key=lambda path: len(path))
  

def find_shortest_path(floors):
    start = get_positions({START}, floors[0])[0]
    path = _find_shortest_path(floors, start, 0)
    path.insert(0, start)
    return path
    
filename = input()
with open(filename) as input_file:
    width, height, nb_floors = (int(val) for val in input_file.readline().split(' '))
    floors = []

    for i in range(nb_floors):
        floors.append([])
        tiles = [int(val) for val in input_file.readline().split(' ')]
        for j in range(height):
            floors[i].append(tiles[j*width:(j+1)*width])

    path = find_shortest_path(floors)
    print(path_to_commands(path))




        
