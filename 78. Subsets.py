class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []

        # 有公式可以繞過彎路=> 「每個數字只能接比自身index還大的數字」，且index要一路傳遞
        # index代表這次可以挑哪個數字當作下一個

        def backtrack(arr, index):
            ans.append(arr[:])

            if index == len(nums):
                return

            for i in range(index, len(nums)):
                arr.append(nums[i])
                # i + 1 因為屬於i的數字，在上一行被處理了
                backtrack(arr, i + 1)
                arr.pop()

        # 初始index=> 0, 因為一開始可以從任意數字做選擇
        backtrack([], 0)
        return ans


print(Solution().subsets([1, 2, 3]))  # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
