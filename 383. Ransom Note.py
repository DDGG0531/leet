from collections import defaultdict


def solution(ransomNote, magazine):
    counts = defaultdict(int)

    for i in magazine:
        counts[i] += 1

    for i in ransomNote:
        if counts[i] == 0:
            return False
        counts[i] -= 1
    return True


# false
print(solution("aa", "aab"))
