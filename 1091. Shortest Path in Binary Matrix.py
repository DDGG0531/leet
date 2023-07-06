from collections import deque


def test(grid):
    # 給一個matrix，要從左上走到右下，且只能走0的路
    # 可以走斜線，求最短路徑
    # 通常求最短路徑，就可以考慮BFS

    if grid[0][0] == 1:
        return -1

    def isValid(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0

    queue = deque([(0, 0, 1)])
    seen = set((0, 0))
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]

    while queue:
        (x, y, depth) = queue.popleft()

        if x == len(grid) - 1 and y == len(grid[0]) - 1:
            return depth

        for offsetX, offsetY in directions:
            nextX, nextY = x + offsetX, y + offsetY

            if isValid(nextX, nextY) and (nextX, nextY) not in seen:
                queue.append((nextX, nextY, depth + 1))
                seen.add((nextX, nextY))
    return -1


print(test([[0, 1], [1, 0]]))  # 2
print(test([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))  # 4
print(test([[0, 0, 0], [1, 1, 0], [1, 1, 1]]))
