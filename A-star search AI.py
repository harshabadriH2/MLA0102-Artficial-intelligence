import heapq

def a_star(matrix, heuristic, start, goal):
    n = len(matrix)
    visited = [False] * n

    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start))

    while open_list:
        f, g, current = heapq.heappop(open_list)

        if visited[current]:
            continue

        visited[current] = True
        print("Visiting:", current, " Cost:", g)

        if current == goal:
            print("Goal reached with total cost:", g)
            return

        for neighbor in range(n):
            if matrix[current][neighbor] > 0 and not visited[neighbor]:
                new_g = g + matrix[current][neighbor]
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(open_list, (new_f, new_g, neighbor))

    print("Goal not reachable")


# -------- MAIN --------
matrix = [
    [0, 1, 4, 0],
    [1, 0, 2, 5],
    [4, 2, 0, 1],
    [0, 5, 1, 0]
]

heuristic = [7, 6, 2, 0]

start = 0
goal = 3

a_star(matrix, heuristic, start, goal)

