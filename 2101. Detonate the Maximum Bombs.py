from collections import defaultdict


class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        length = len(bombs)

        graph = defaultdict(list)

        def isNeighbor(i, j):
            if i == j:
                return False
            distance = (
                (bombs[j][0] - bombs[i][0]) ** 2 + (bombs[j][1] - bombs[i][1]) ** 2
            ) ** 0.5
            return True if distance <= bombs[i][2] else False

        for i in range(length):
            for j in range(length):
                if isNeighbor(i, j):
                    graph[i].append(j)

        def dfs(index):
            for neighbor in graph[index]:
                if neighbor not in seens:
                    seens.add(neighbor)
                    dfs(neighbor)

        answers = []
        for index in range(length):
            seens = set()
            if index not in seens:
                seens.add(index)
                dfs(index)
                answers.append(len(seens))

        return max(answers)


solution = Solution()
print(solution.maximumDetonation([[2, 1, 3], [6, 1, 4]]))  # 2
print(solution.maximumDetonation([[1, 1, 5], [10, 10, 5]]))  # 1
print(
    solution.maximumDetonation([[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]])
)  # 5
