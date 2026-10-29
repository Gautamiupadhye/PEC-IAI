def solve_example_1():
    graph = {
        'a': [('b', 5), ('c', 6), ('d', 4)],
        'b': [('e', 2), ('c', 2)],
        'c': [('f', 4)],
        'd': [('c', 3), ('i', 6)],
        'e': [('g', 1)],
        'g': [('f', 4)],
        'f': [('c', 5)],
        'i': [('f', 4)],
    }
    heuristics = {'a': 10, 'b': 8, 'c': 4, 'd': 5, 'e': 3, 'f': 0, 'g': 0, 'i': 2}
    start = 'a'
    goal = 'f'
    open_list = [[heuristics[start], 0, start, [start]]] # [f, g, current_node, path_taken]
    visited = set()
    while open_list:
        open_list.sort() # Sort to pick the smallest f(n)
        f, g, current, path = open_list.pop(0)
        if current in visited:
            continue
        visited.add(current)
        if current == goal:
            print("--- Example 1 Solution ---")
            print("Path Found:", " -> ".join(path))
            print("Total Cost:", g)
            return
        for neighbor, cost in graph.get(current, []):
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristics[neighbor]
                open_list.append([new_f, new_g, neighbor, path + [neighbor]])
