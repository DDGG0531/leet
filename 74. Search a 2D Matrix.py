class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # 以排序過的二維陣列，找target，回傳找不找得到
        # 如果不想要額外增加空間，可以用index來做
        # 由於已知是排序過的，所以可以用binary search
        cols = len(matrix[0])
        rows = len(matrix)
        left = 0
        right = cols * rows - 1

        def convertOneIndexIntoTwoIndex(index: int):
            return {
                "row": index // cols,
                "col": index % cols,
            }

        while left <= right:
            mid = (left + right) // 2
            result = convertOneIndexIntoTwoIndex(mid)
            midRow, midCol = result["row"], result["col"]

            midValue = matrix[midRow][midCol]
            if midValue == target:
                return True
            elif midValue > target:
                right = mid - 1
            elif midValue < target:
                left = mid + 1
        return False


solution = Solution()
print(
    solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
)  # True
print(
    solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)
)  # False
