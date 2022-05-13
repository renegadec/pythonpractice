import curses
from curses import wrapper
import enum
import queue
import time


maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

# print the maze using rows and column with i and j being the position
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j*2, "X", RED)
            else:
                stdscr.addstr(i, j*2, value, BLUE)
            

# determine the starting position
def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j

    # if function doesn't find the start point return none
    return None


def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    # position that have been visited already
    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear() #clear the whole terminal
        print_maze(maze, stdscr, path)
        time.sleep(0.2) 
        stdscr.refresh() #refresh screen so we can see output

        if maze[row][col] == end:
            return path
        
        # find out if neighbor has been visited or is a barrier
        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r, c = neighbor

            if maze[r][c] == "#":
                continue

            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)
    
def find_neighbors(maze, row, col):
    neighbors = []
    if row > 0: # UP
        neighbors.append((row, col - 1))
    if row + 1 < len(maze): # DOWN
        neighbors.append((row + 1, col))
    if col > 0: # LEFT
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]): # RIGHT
        neighbors.append((row, col + 1))

    return neighbors

# function for printing on the terminal
def main(stdscr):
    # setting the (ID, foreground color and background color)
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(maze, stdscr)
    stdscr.getch() # make the terminal wait for user intervention so it can clear the screen

wrapper(main)

