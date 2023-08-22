class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        records = ["("]  # ['(',')',')']

        def backtrack(level, ls, rs):
            if level == n * 2:
                ans.append("".join(records))
                return

            for el in ["(", ")"]:
                newls = ls + (el == "(")
                newrs = rs + (el == ")")

                if newls > n or newrs > n or newls < newrs:
                    continue

                records.append(el)
                backtrack(level + 1, newls, newrs)
                records.pop()

        backtrack(1, 1, 0)

        return ans


print(
    Solution().generateParenthesis(3)
)  # ["((()))","(()())","(())()","()(())","()()()"]
