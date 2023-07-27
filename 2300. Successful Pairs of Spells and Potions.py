class Solution:
    def successfulPairs(
        self, spells: list[int], potions: list[int], success: int
    ) -> list[int]:
        # spells是乘數，乘上potions裡面的數後，問新的positions有幾個數字大於等於success
        # 這一題的binary search 點在於，如果先sort potions，再乘，就可以很快速的找到再哪個index後的數字可以符合條件
        # 也是利用binary search find or insert的概念
        potions.sort()
        ans = []
        n = len(potions)

        def binary_search(arr, target) -> int:
            # 在arr中找到某數字的index，如果找不到就回傳他應該擺放的index
            # 重複數字要找哪一個index也是有玄機的 => 如果是大於等於，就找最左；大於就找最右；小於找最左；小於等於找最右
            # 而大於等於跟小於互補，所以沒差
            # 這題要找大於等於，所以找最左

            left = 0
            right = len(arr) - 1

            while left <= right:
                mid = left + (right - left) // 2
                midValue = arr[mid]
                if midValue == target:
                    right = mid - 1
                elif midValue > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        for spell in spells:
            result = binary_search(potions, success / spell)
            ans.append(n - result)

        return ans


solution = Solution()
print(solution.successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7))  # [4,0,3]
