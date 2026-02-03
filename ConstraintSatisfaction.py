from simpleai.search import CspProblem, backtrack

def constraint_func(names, values):
    return values[0] != values[1]

if __name__ == '__main__':
    n_regions = int(input("Enter number of regions: "))
    regions = []
    for i in range(n_regions):
        r = input(f"Enter name of region {i+1}: ")
        regions.append(r)

    n_colors = int(input("Enter number of colors: "))
    colors_list = []
    for i in range(n_colors):
        c = input(f"Enter color {i+1}: ")
        colors_list.append(c)

    colors = {r: colors_list for r in regions}

    n_edges = int(input("Enter number of edges (neighbor pairs): "))
    constraints = []
    
    print("Enter edges in format: region1 region2")
    for _ in range(n_edges):
        r1, r2 = input().split()
        constraints.append(((r1, r2), constraint_func))

    problem = CspProblem(regions, colors, constraints)

    solution = backtrack(problem)

    print("\nMap Coloring Solution:")
    if solution:
        for k, v in solution.items():
            print(k, "==>", v)
    else:
        print("No solution exists with given regions, colors, and constraints.")
