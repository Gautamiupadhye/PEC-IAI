from collections import deque

graph = {
    5: [3, 7],
    3: [2, 4],
    7: [8],
    2: [],
    4: [8],
    8: []
}

def bfs(graph, start, goal):
    visited = set()
    queue = deque([start])

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

start = 5
goal = 8

print("BFS Traversal:")
bfs(graph, start, goal)