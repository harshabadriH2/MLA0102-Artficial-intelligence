import heapq

def ucs(matrix, start, goal):
    n = len(matrix)
    visited = [False] * n

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cost, node = heapq.heappop(pq)

        if visited[node]:
            continue

        visited[node] = True
        print(f"Visited {node} with cost {cost}")

        if node == goal:
            print("Goal reached with minimum cost:", cost)
            return

        for i in range(n):
            if matrix[node][i] > 0 and not visited[i]:
                heapq.heappush(pq, (cost + matrix[node][i], i))

    print("Goal not reachable")

# ---------- MAIN ----------
matrix = [
    [0, 1, 4, 0],
    [1, 0, 2, 5],
    [4, 2, 0, 1],
    [0, 5, 1, 0]
]

start = 0
goal = 3

ucs(matrix, start, goal)
