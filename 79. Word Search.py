class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ans = False

        lenRow, lenCol = len(board), len(board[0])

        def getNeighbors(row, col):
            result = []

            if row == -1 and col == -1:
                for row in range(lenRow):
                    for col in range(lenCol):
                        result.append((row, col))

            else:
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for direction in directions:
                    newRow, newCol = row + direction[0], col + direction[1]
                    if (
                        0 <= newRow < lenRow
                        and 0 <= newCol < lenCol
                        and (newRow, newCol) not in records
                    ):
                        result.append((newRow, newCol))

            return result

        records = []  # (row,col)

        def backtrack(
            n,
            lastRow,
            lastCol,
        ):
            if n == len(word):
                nonlocal ans
                ans = True
                return

            for row, col in getNeighbors(lastRow, lastCol):
                if board[row][col] != word[n]:
                    continue

                records.append((row, col))
                backtrack(n + 1, row, col)
                records.pop()

        backtrack(0, -1, -1)
        return ans


print(
    Solution().exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCCED",
    )
)  # True
print(
    Solution().exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="SEE",
    )
)  # True

print(
    Solution().exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCB",
    )
)  # False
