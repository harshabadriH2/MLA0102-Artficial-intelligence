import heapq

def greedy_best_first(matrix, heuristic, start, goal):
    n = len(matrix)
    visited = [False] * n

    # priority queue → (heuristic, node)
    pq = []
    heapq.heappush(pq, (heuristic[start], start))

    while pq:
        h, current = heapq.heappop(pq)

        if visited[current]:
            continue

        visited[current] = True
        print("Visiting:", current, " Heuristic:", h)

        if current == goal:
            print("Goal reached!")
            return

        for neighbor in range(n):
            if matrix[current][neighbor] > 0 and not visited[neighbor]:
                heapq.heappush(pq, (heuristic[neighbor], neighbor))

    print("Goal not reachable")
matrix = [
    [0, 1, 4, 0],
    [1, 0, 2, 5],
    [4, 2, 0, 1],
    [0, 5, 1, 0]
]

heuristic = [7, 6, 2, 0]

start = 0
goal = 3

greedy_best_first(matrix, heuristic, start, goal)
