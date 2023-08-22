class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        hashMap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        ans = []

        if digits == "":
            return ans

        def backtrack(arr, startIndex):
            if len(arr) == len(digits):
                ans.append("".join(arr))
                return

            for letters in hashMap[digits[startIndex]]:
                arr.append(letters)
                backtrack(arr, startIndex + 1)
                arr.pop()

        backtrack([], 0)

        return ans


print(
    Solution().letterCombinations("23")
)  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]

print(Solution().letterCombinations(""))  # []

print(Solution().letterCombinations("2"))  # ["a","b","c"]
