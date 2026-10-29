def solve_example_3():
    graph = {
        'A': [('B', 2), ('C', 4)],
        'B': [('D', 3)],
        'C': [('E', 2)],
        'D': [('G', 2)],
        'E': [('G', 3)],
        'G': []
    }
    heuristics = {'A': 6, 'B': 5, 'C': 4, 'D': 2, 'E': 3, 'G': 0}
    start = 'A'
    goal = 'G'
    open_list = [[heuristics[start], 0, start, [start]]]
    visited = set()
    while open_list:
        open_list.sort()
        f, g, current, path = open_list.pop(0)
        if current in visited:
            continue
        visited.add(current)
        if current == goal:
            print("--- Example 3 Solution ---")
            print("Path Found:", " -> ".join(path))
            print("Total Cost:", g)
            return
        for neighbor, cost in graph.get(current, []):
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristics[neighbor]
                open_list.append([new_f, new_g, neighbor, path + [neighbor]])
