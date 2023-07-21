import heapq


class Solution:
    def maxNumberOfApples(self, weight: list[int]) -> int:
        # 籃子能承重5000
        # 找出最多能放幾個蘋果

        # 作法：每次都拿最輕的蘋果放進籃子直到放不下為止

        # 思考一: sorted (nlogn)

        # 思考二: heap
        # heapify (n)
        # pop (每次都是logn)
        # 總共是 n + x * logn => 如果運氣很好裝滿，那就是nlogn

        # 所以用heap

        heapq.heapify(weight)
        ans = 0
        times = 0

        while ans < 5000 and weight:
            w = heapq.heappop(weight)
            if ans + w > 5000:
                break
            ans += w
            times += 1
        return times


solution = Solution()

print(solution.maxNumberOfApples([100, 200, 150, 1000]))  # 4
print(solution.maxNumberOfApples([900, 950, 800, 1000, 700, 800]))  # 5
