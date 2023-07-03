# [0,1,0,0,1] => 3
# [0,1,0,0] => 1
# [0,1,1,1,0,1,1,0,0,0] => 2


def test(nums):
    if len(nums) == 0:
        return 1
    levels = []
    ans = 1
    lastIndex = len(nums) - 1

    for l in range(len(nums)):
        if nums[l] == 1:
            r = l + 1
            if r >= lastIndex:
                levels.append(1)
            else:
                while nums[r] == 0:
                    r += 1
                    if r > lastIndex:
                        r = l + 1
                        break
                levels.append(r - l)
    if len(levels) == 0:
        return 0

    for level in levels:
        ans *= level
        ans %= 10**9 + 7
    return ans


print(test([0, 1, 0, 0, 1]))
