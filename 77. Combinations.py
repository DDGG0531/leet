class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans = []

        def backtrack(arr, startNum):
            if len(arr) == k:
                ans.append(arr[:])
                return

            for _num in range(startNum, n + 1):
                arr.append(_num)
                backtrack(arr, _num + 1)
                arr.pop()

        backtrack([], 1)

        return ans


print(Solution().combine(4, 2))  # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
