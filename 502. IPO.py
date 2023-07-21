import heapq


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: list[int], capital: list[int]
    ) -> int:
        # 直接參考答案
        # 過程：影片是用雙heap，這邊是用heap+sorted list
        # 因為這題只需要跑k次，所以雙heap會更有效率
        # 有多錢做多少投資，賺到的錢可以做更大的投資，且不能重複投資同一個專案

        # 在每個while中，把可以做的專案都加到heap中，在pop出最大產值的專案
        # 順便要小心現有的錢可能不夠投資任何專案，所以要先檢查heap是否為空
        n = len(profits)
        projects = sorted(zip(capital, profits))
        heap = []
        i = 0

        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])
                i += 1

            if len(heap) == 0:
                # not enough money to do any more projects
                return w

            # minus because we stored negative numbers on the heap
            w -= heapq.heappop(heap)

        return w
