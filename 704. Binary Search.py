class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # 試著在sorted arr中找到target，並回傳index
        # PS: 如果一個一個找，最差複雜度是O(n)
        # PS: 如果用binary search，最差複雜度是O(logn)

        leftIndex = 0
        rightIndex = len(nums) - 1

        # 1 [2] 3 => index:1
        # 1 [2] 3 4 => index:1

        while leftIndex <= rightIndex:
            midIndex = (rightIndex + leftIndex) // 2
            print(midIndex)

            if nums[midIndex] == target:
                return midIndex
            # 如果中間的數字比target大，代表target在左邊
            elif nums[midIndex] > target:
                rightIndex = midIndex - 1
            elif nums[midIndex] < target:
                leftIndex = midIndex + 1

        # 找不到的case
        return -1


solution = Solution()
print(solution.search([-1, 0, 3, 5, 9, 12], 9))  # 4
print(solution.search([-1, 0, 3, 5, 9, 12], 2))  # -1
