class Solution:
    def maximum69Number(self, num: int) -> int:
        arr = list(map(int, str(num)))
        # PS: 事後才發現根本不用轉數字，直接用字串處理就好

        done = False
        for i in range(len(arr)):
            if done:
                break
            if arr[i] == 6:
                arr[i] = 9
                done = True

        return int("".join(map(str, arr)))


solution = Solution()

print(solution.maximum69Number(9669))  # 9969
