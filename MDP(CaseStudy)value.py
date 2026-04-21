states = ["Low", "Medium", "High"]
actions = ["Short", "Medium", "Long"]
gamma = 0.9

reward = {"Low": 10, "Medium": 5, "High": -10}

transitions = {
    "Low": {
        "Short": [("Low", 0.7), ("Medium", 0.3)],
        "Medium": [("Low", 0.6), ("Medium", 0.4)],
        "Long": [("Medium", 0.6), ("High", 0.4)]
    },
    "Medium": {
        "Short": [("Low", 0.4), ("Medium", 0.6)],
        "Medium": [("Medium", 0.5), ("High", 0.5)],
        "Long": [("High", 0.7), ("Medium", 0.3)]
    },
    "High": {
        "Short": [("Medium", 0.6), ("High", 0.4)],
        "Medium": [("Medium", 0.7), ("High", 0.3)],
        "Long": [("Low", 0.5), ("Medium", 0.5)]
    }
}

V = {s: 0 for s in states}

for i in range(10):
    print(f"\nIteration {i}")
    new_V = {}

    for s in states:
        values = {}

        for a in actions:
            values[a] = sum(prob * (reward[s2] + gamma * V[s2])
                            for s2, prob in transitions[s][a])
            print(f"{s}-{a}: {values[a]:.2f}")

        best = max(values, key=values.get)
        new_V[s] = values[best]

        print(f"Best for {s}: {best} → {new_V[s]:.2f}")

    V = new_V
    print("Values:", {s: round(V[s], 2) for s in states})

print("\nFinal Values:", {s: round(V[s], 2) for s in states})
