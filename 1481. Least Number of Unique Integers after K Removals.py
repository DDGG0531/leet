from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        # 把arr 刪除 k個數字 => 讓剩下的數字種類，最少，回傳剩餘的種類數量
        # 作法：Greedy的方式，從出現次數最少的開始刪除
        counter = Counter(arr)

        values = sorted(counter.values())

        currentIndex = 0

        for _ in range(k):
            while values[currentIndex] == 0:
                currentIndex += 1

            values[currentIndex] -= 1

        return len(list(filter(lambda x: x != 0, values)))


solution = Solution()

print(solution.findLeastNumOfUniqueInts([5, 5, 4], 1))  # 1
print(solution.findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3))  # 2
