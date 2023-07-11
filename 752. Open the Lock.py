from collections import deque


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        seen = set(deadends)
        queue = deque([("0000", 0)])

        if "0000" in seen:
            return -1

        def getNeighbors(node: str) -> list[str]:
            ans = []
            for i in range(4):
                charater = node[i]
                for move in [1, -1]:
                    newCharater = str((int(charater) + move) % 10)
                    ans.append(node[:i] + newCharater + node[i + 1 :])
            return ans

        while queue:
            node, depth = queue.popleft()

            if node == target:
                return depth

            for neighbor in getNeighbors(node):
                if neighbor not in seen:
                    queue.append((neighbor, depth + 1))
                    seen.add(neighbor)
        return -1


solution = Solution()
print(solution.openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))  # 6
print(solution.openLock(["8888"], "0009"))  # 1
