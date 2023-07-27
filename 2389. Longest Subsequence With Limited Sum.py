class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        # 題目要求利用nums的數字作累加，盡可能地用越多數字，但不能超過queries的上限
        # 暴力法可以先sort nums，再一個一個加直到超過上限
        # 二元搜尋法可以先sort再累加nums，再尋找上限會落在哪個位置，找出小於等於該數字的個數
        # 由於每個數至少是1，所以該arr不會有相同的數字
        nums.sort()
        accumulate = []
        sum_so_far = 0
        for num in nums:
            accumulate.append(sum_so_far + num)
            sum_so_far += num

        def binary_search(arr, target):
            left = 0
            right = len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                midValue = arr[mid]
                # 這題不要回傳，因為我不是要找，而是確定要塞，而且是塞在靠右邊的位置
                if midValue == target:
                    left = mid + 1
                elif midValue > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return left

        ans = []
        for query in queries:
            idx = binary_search(accumulate, query)
            ans.append(idx)
        return ans


print(Solution().answerQueries(nums=[4, 5, 2, 1], queries=[3, 10, 21]))  # [2,3,4]
