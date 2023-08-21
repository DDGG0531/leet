class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # 同範例一的輸出結果，順序matters
        ans = []

        # arr == 至今為止累積的結果，此結果會在長度等於3時，加進答案，可以想作[1,2]就是過程中產生的結果
        # 繼續累積，就會得到[1,2,3]，這時候就可以加進答案
        def backtrack(arr):
            if len(arr) == len(nums):
                ans.append(arr[:])
                return

            for num in nums:
                # 在arr中的都是已經處理過的，只有不在arr中的才需要處理
                if num not in arr:
                    arr.append(num)
                    backtrack(arr)
                    arr.pop()

        # 初始[]，代表一開始沒有任何處理過的數字
        backtrack([])

        return ans


print(
    Solution().permute([1, 2, 3])
)  # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
