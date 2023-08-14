import sys


class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        # 回想一下切巧克力的那題，但這一題要「最大的那塊」的甜度最小
        # 不要執著下刀點，而是從「答案」aka 「和最大的那塊」出發
        # 先想著「和最大的那塊」可能的值是哪裡到哪裡
        # 因為可能的區間有著「一個閾值區分兩塊的特性」，所以可以用二分法

        groups = k

        l = max(nums)
        r = sum(nums)

        ans = sys.maxsize

        def get_min_groups(value):
            # True: 從頭開始分，只要每個人都拿到<=value的甜度，就可以
            # !要盡量餵給每一組，因為要分完
            pass_count = 0
            current_sum = 0
            for i in range(len(nums)):
                if current_sum + nums[i] <= value:
                    current_sum += nums[i]
                else:
                    pass_count += 1
                    current_sum = nums[i]

            return pass_count + 1

        while l <= r:
            mid = (l + r) // 2
            min_groups = get_min_groups(mid)

            if min_groups <= groups:
                r = mid - 1
                ans = min(ans, mid)
            else:
                l = mid + 1
        return ans


print(Solution().splitArray([7, 2, 5, 10, 8], 2))  # 18
print(Solution().splitArray([1, 2, 3, 4, 5], 2))  # 9
print(Solution().splitArray([1, 4, 4], 3))  # 4
