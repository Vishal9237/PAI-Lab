from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque()
    queue.append((0, 0, []))  # (jug1, jug2, path)
    visited.add((0, 0))
    
    while queue:
        jug1, jug2, path = queue.popleft()
        
        if jug1 == target or jug2 == target:
            return path + [(jug1, jug2)]
        
        status = [
            (jug1_capacity, jug2),  
            (jug1, jug2_capacity),  
            (0, jug2),              
            (jug1, 0),              
            (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)),  
            (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1))   
        ]
        
        for state in status:
            if state not in visited:
                visited.add(state)
                queue.append((state[0], state[1], path + [(jug1, jug2)]))
    
    return None

bfs_result = water_jug_bfs(4, 3, 2)
print("BFS Path to solution:")
for step in bfs_result:
    print(step)
