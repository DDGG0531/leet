# 超時


class Solution:
    def totalNQueens(self, n: int) -> int:
        def convert2DTo1D(col, row):
            return col + n * row

        def convert1DTo2D(index):
            return (index % n, index // n)

        def flatten(lst):
            flattened = []
            for item in lst:
                if isinstance(item, list):
                    flattened.extend(flatten(item))
                else:
                    flattened.append(item)
            return flattened

        # 輸入index找出該index佔據的位置

        # 輸入佔據的位置arr，找出剩下的位置arr (擔心這邊會超時)

        # 每次都從這些剩下的位置arr去放置，直到放完n個皇后，且每次放的位置都要往後

        def getOccupies(index):
            occupies = set()
            col, row = convert1DTo2D(index)

            for i in range(n):
                occupies.add(convert2DTo1D(col, i))
                occupies.add(convert2DTo1D(i, row))

            directions = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
            seen = set()

            for direction in directions:
                nextCol = col + direction[0]
                nextRow = row + direction[1]

                while (
                    nextCol >= 0
                    and nextCol <= n - 1
                    and nextRow >= 0
                    and nextRow <= n - 1
                ):
                    idx = convert2DTo1D(nextCol, nextRow)

                    if idx not in seen:
                        occupies.add(idx)
                        seen.add(idx)

                    nextCol += direction[0]
                    nextRow += direction[1]

            return list(occupies)

        def getEmpties(occupies):
            empties = set()

            for i in range(n**2):
                if i not in flatten(occupies):
                    empties.add(i)

            return list(empties)

        def backtrack(placed, occupies, startIndex):
            if placed == n:
                nonlocal ans
                ans += 1
                return

            empties = getEmpties(occupies)
            for index in empties:
                if index >= startIndex:
                    occupies.append(getOccupies(index))
                    backtrack(placed + 1, occupies, index)
                    occupies.pop()

        ans = 0

        backtrack(0, [], 0)
        return ans


print(Solution().totalNQueens(4))  # 2
# print(Solution().totalNQueens(1))  # 1
