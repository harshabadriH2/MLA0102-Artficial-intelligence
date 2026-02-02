def minimax(depth, nodeIndex, isMax, scores, maxDepth):
    if depth == maxDepth:
        return scores[nodeIndex]

    if isMax:
        best = -1000
        for i in range(2):
            value = minimax(depth + 1, nodeIndex * 2 + i, False, scores, maxDepth)
            best = max(best, value)
        return best
    else:
        best = 1000
        for i in range(2):
            value = minimax(depth + 1, nodeIndex * 2 + i, True, scores, maxDepth)
            best = min(best, value)
        return best


scores = [3, 5, 2, 9, 12, 5, 23, 23]
depth = 3

result = minimax(0, 0, True, scores, depth)
print(result)
