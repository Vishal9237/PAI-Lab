from collections import deque

start = [1,3,0,4,2,6,7,5,8]
goal = [1,2,3,4,5,6,7,8,0]

moves = {
0:[1,3],
1:[0,2,4],
2:[1,5],
3:[0,4,6],
4:[1,3,5,7],
5:[2,4,8],
6:[3,7],
7:[4,6,8],
8:[5,7]
}

names = {
(0,1):"RIGHT",(1,0):"LEFT",
(0,3):"DOWN",(3,0):"UP",
(1,2):"RIGHT",(2,1):"LEFT",
(1,4):"DOWN",(4,1):"UP",
(2,5):"DOWN",(5,2):"UP",
(3,4):"RIGHT",(4,3):"LEFT",
(3,6):"DOWN",(6,3):"UP",
(4,5):"RIGHT",(5,4):"LEFT",
(4,7):"DOWN",(7,4):"UP",
(5,8):"DOWN",(8,5):"UP",
(6,7):"RIGHT",(7,6):"LEFT",
(7,8):"RIGHT",(8,7):"LEFT"
}

def print_grid(state):
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])
    print()

queue = deque([(start,[])])
visited=set()

while queue:
    state,path = queue.popleft()

    if state==goal:
        for move,grid in path:
            print("Move:",move)
            print_grid(grid)
        break

    visited.add(tuple(state))
    zero=state.index(0)

    for m in moves[zero]:
        new=state.copy()
        new[zero],new[m]=new[m],new[zero]

        if tuple(new) not in visited:
            move_name = names[(zero,m)]
            queue.append((new,path+[(move_name,new)]))
