class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # 用candidates中的數字，組出target
        # 由於 [2,3] == [3,2] 所以<只能往後選>

        def isNumberValid(accSum, num):
            return accSum + num <= target

        ans = []

        def backtrack(arr, startIndex):
            if sum(arr) == target:
                ans.append(arr[:])
                return

            for index, candidate in enumerate(candidates[startIndex:]):
                if isNumberValid(sum(arr), candidate):
                    arr.append(candidate)
                    backtrack(arr, index + startIndex)
                    arr.pop()

        backtrack([], 0)
        return ans


print(Solution().combinationSum([2, 3, 6, 7], 7))  # [[2,2,3],[7]]
print(Solution().combinationSum([2, 3, 5], 8))  # [[2,2,2,2],[2,3,3],[3,5]]
