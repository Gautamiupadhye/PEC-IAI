from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

def bfs(graph, start, goal):
    visited = set()
    queue = deque([start])

    print("BFS Traversal:")

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            if node == goal:
                print("\nGoal node found!")
                return

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

start = 'A'
goal = 'G'

bfs(graph, start, goal)