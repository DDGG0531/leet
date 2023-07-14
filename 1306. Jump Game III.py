from collections import deque


class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        # start給的是index，也是你開始的位置
        # arr中的數字代表，走在這個點上，可以對你的位置做移動
        # 題目要問的是，你是否可以走到一個數字是0的點上

        # 我的想法就是，把他當成graph去走，只要走到某個點上，發現他是0，就回傳True
        # 如果找不到，就回傳False
        # 然後一樣是用seen來紀錄是否有走過某個點，走過就不走
        # PS: DFS/BFS都可以，但這因為是比較點，所以我習慣用BFS

        def getNeighbor(index):
            maxIndex = len(arr) - 1
            minIndex = 0
            move = arr[index]
            ans = []
            for diff in [move, -move]:
                newIndex = index + diff
                if minIndex <= newIndex <= maxIndex:
                    ans.append(newIndex)
            return ans

        seen = set({start})
        queue = deque([start])

        while queue:
            index = queue.popleft()
            if arr[index] == 0:
                return True
            for neighbor in getNeighbor(index):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        return False


solution = Solution()

print(solution.canReach([4, 2, 3, 0, 3, 1, 2], 5))  # True

print(solution.canReach([4, 2, 3, 0, 3, 1, 2], 0))  # True

print(solution.canReach([3, 0, 2, 1, 2], 2))  # False
