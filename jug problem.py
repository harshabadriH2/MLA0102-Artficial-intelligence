from collections import deque

def water_jug_problem(capacity1, capacity2, target):
    visited = set()
    queue = deque()

    queue.append((0, 0))
    visited.add((0, 0))

    while queue:
        jug1, jug2 = queue.popleft()
        print(jug1, jug2)

        if jug1 == target or jug2 == target:
            print("Goal reached")
            return

        states = [
            (capacity1, jug2),
            (jug1, capacity2),
            (0, jug2),
            (jug1, 0),
            (jug1 - min(jug1, capacity2 - jug2), jug2 + min(jug1, capacity2 - jug2)),
            (jug1 + min(jug2, capacity1 - jug1), jug2 - min(jug2, capacity1 - jug1))
        ]

        for state in states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

    print("Goal not possible")


capacity1 = 4
capacity2 = 3
target = 2

water_jug_problem(capacity1, capacity2, target)
