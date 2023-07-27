class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # 題目說是 sorted list & unique values
        # 找出target在哪個位置，如果找不到就回傳他應該擺放的位置

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            midValue = nums[mid]
            if midValue == target:
                return mid
            elif midValue > target:
                right = mid - 1
            else:
                left = mid + 1
        return left


print(Solution().searchInsert([1, 3, 5, 6], 5))  # 2
print(Solution().searchInsert([1, 3, 5, 6], 2))  # 1
print(Solution().searchInsert([1, 3, 5, 6], 7))  # 4
