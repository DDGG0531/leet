class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        # graph[0]中的數字代表0可以到達的點
        # 答案希望找出所有「從0到終點的路徑」

        # backtrack用在求路線很好用

        # 本題是從0 到 len(graph) - 1, index等於數字

        ans = []
        lastNumber = len(graph) - 1

        def backtrack(arr):
            if arr[-1] == lastNumber:
                ans.append(arr[:])
                return

            for _num in graph[arr[-1]]:
                arr.append(_num)
                backtrack(arr)
                arr.pop()

        backtrack([0])

        return ans


print(
    Solution().allPathsSourceTarget(graph=[[1, 2], [3], [3], []])
)  # [[0,1,3],[0,2,3]]
