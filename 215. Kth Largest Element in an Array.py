import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # 要找第K大的數字
        # 必須用max heap => min heap with 負數
        nums = [-v for v in nums]
        heapq.heapify(nums)

        while k > 1:
            heapq.heappop(nums)
            k -= 1

        return -(nums[0])


solution = Solution()
print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
print(solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
