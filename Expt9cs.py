states = ["Idle", "Working"]
actions = ["Work", "Charge"]
gamma = 0.9

reward = {
    ("Idle", "Work"): 5,
    ("Idle", "Charge"): 2,
    ("Working", "Work"): 8,
    ("Working", "Charge"): 1
}

transitions = {
    "Idle": {
        "Work": [("Working", 1.0)],
        "Charge": [("Idle", 1.0)]
    },
    "Working": {
        "Work": [("Working", 0.7), ("Idle", 0.3)],
        "Charge": [("Idle", 1.0)]
    }
}

# initial values and policy
V = {s: 0 for s in states}
policy = {s: "Work" for s in states}

for i in range(10):
    print(f"\nIteration {i}")

    # POLICY EVALUATION (few steps only)
    for _ in range(10):
        for s in states:
            a = policy[s]
            V[s] = sum(prob * (reward[(s, a)] + gamma * V[s2])
                       for s2, prob in transitions[s][a])

    print("Values:", {s: round(V[s], 2) for s in states})

    # POLICY IMPROVEMENT
    stable = True
    for s in states:
        old = policy[s]

        # find best action
        best = max(actions, key=lambda a:
                   sum(prob * (reward[(s, a)] + gamma * V[s2])
                       for s2, prob in transitions[s][a]))

        policy[s] = best
        print(f"{s}: {old} → {best}")

        if old != best:
            stable = False

    if stable:
        break

print("\nFinal Policy:", policy)
print("Final Values:", {s: round(V[s], 2) for s in states})
