from collections import defaultdict


def solution(nums, k):
    current = 0
    ans = 0
    counts = defaultdict(int)
    counts[0] = 1

    def isOdd(num):
        return num % 2 == 1

    for num in nums:
        current += 1 if isOdd(num) else 0
        ans += counts[current - k]
        counts[current] += 1
    return ans


# 16
print(solution([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
