import heapq
import time
import os

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    came_from = {}
    g_cost = {start: 0}
    
    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        neighbors = [(0,1), (1,0), (0,-1), (-1,0)]
        
        for dx, dy in neighbors:
            neighbor = (current[0] + dx, current[1] + dy)
            
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue
                
                new_cost = g_cost[current] + 1
                
                if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                    g_cost[neighbor] = new_cost
                    f_cost = new_cost + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_cost, neighbor))
                    came_from[neighbor] = current
    
    return None


def print_step(grid, path, step_index, start, goal):
    os.system('cls' if os.name == 'nt' else 'clear')  # clear screen
    
    display = [row[:] for row in grid]
    
    for i in range(step_index + 1):
        r, c = path[i]
        display[r][c] = '*'
    
    r, c = path[step_index]
    display[r][c] = 'X'  
    
    display[start[0]][start[1]] = 'S'
    display[goal[0]][goal[1]] = 'G'
    
    for row in display:
        print(" ".join(map(str, row)))
    print()


rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))

print("Enter grid (0 free, 1 obstacle):")
grid = [list(map(int, input().split())) for _ in range(rows)]

start = tuple(map(int, input("Enter start (row col): ").split()))
goal = tuple(map(int, input("Enter goal (row col): ").split()))

path = astar(grid, start, goal)

if path:
    print("\nRobot Moving Step-by-Step:\n")
    
    for i in range(len(path)):
        print_step(grid, path, i, start, goal)
        time.sleep(0.7)  # delay between steps
    
    print("\nDestination Reached!")
else:
    print("No path found")
