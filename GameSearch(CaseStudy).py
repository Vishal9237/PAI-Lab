n = int(input("Enter number of nodes: "))
tree = [[] for _ in range(n)]
values = [None] * n

print("Enter edges (parent child), 0-indexed. Enter -1 -1 to stop:")
while True:
    u, v = map(int, input().split())
    if u == -1 and v == -1:
        break
    tree[u].append(v)

print("Enter leaf node values (node_index value). Enter -1 -1 to stop:")
while True:
    u, val = map(int, input().split())
    if u == -1 and val == -1:
        break
    values[u] = val

def alpha_beta(node, maximizing, alpha, beta):
    if values[node] is not None:
        return values[node]
    if maximizing:
        max_eval = -float('inf')
        for child in tree[node]:
            eval = alpha_beta(child, False, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child in tree[node]:
            eval = alpha_beta(child, True, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

best_value = alpha_beta(0, True, -float('inf'), float('inf'))
print("Best value for root:", best_value)
