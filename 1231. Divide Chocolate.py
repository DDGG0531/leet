import sys


class Solution:
    def maximizeSweetness(self, sweetness: list[int], k: int) -> int:
        # 要分成k+1份
        # 使著調整刀法，使得「最小的那塊」的甜度最大

        groups = k + 1

        # 檢驗是否pass的方式，每一組拿到至少這個值
        # 但或許不會有一組剛好等於這個值的情況 => 這邊有點tricky，經過實驗可以得到，如果3是可行的，但當全部的塊都大於3時(ex: 4, 5, 6)，那一定能夠很自然地找到4也是答案
        # 所以放心繼續找即可

        # 考慮自己怎麼拿，才能湊出二分法區域，「甜度最大這件事」會在二分法的過程中被找出來
        #         [pass*][notpass]
        l = min(sweetness)
        r = (sum(sweetness) // groups) + 1
        ans = 0

        def check_isAvalible(value):
            # True: 從頭開始分，只要每個人都拿到>=value的甜度，就可以
            pass_count = 0
            current_sum = 0
            for i in range(len(sweetness)):
                current_sum += sweetness[i]
                if current_sum >= value:
                    pass_count += 1
                    current_sum = 0
            return pass_count >= groups

        while l <= r:
            mid = (l + r) // 2
            isAvalible = check_isAvalible(mid)

            if isAvalible:
                l = mid + 1
                ans = max(ans, mid)
            else:
                r = mid - 1
        return ans


print(sys.maxsize)
print(Solution().maximizeSweetness([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))  # 6
print(Solution().maximizeSweetness([5, 6, 7, 8, 9, 1, 2, 3, 4], 8))  # 1
print(Solution().maximizeSweetness([1, 2, 2, 1, 2, 2, 1, 2, 2], 2))  # 5
