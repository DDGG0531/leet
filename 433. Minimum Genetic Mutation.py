from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        # 用BFS找最短路徑
        # 避免循環用seen
        # neighbor 必須滿足在bank裡面，且只有一個字母不同
        # 跟開鎖很像，一種8格，每一格有四種變化，但沒有類似0只能轉到1跟9的限制

        def getNeighbors(gene):
            ans = []
            for i in range(8):
                currentChar = gene[i]
                for char in ["A", "C", "G", "T"]:
                    if currentChar == char:
                        continue
                    ans.append(gene[:i] + char + gene[i + 1 :])
            return ans

        seen = set(startGene)
        queue = deque([(startGene, 0)])

        while queue:
            gene, depth = queue.popleft()
            # 處理該基因序列
            if gene == endGene:
                return depth
            # 加入queue
            for neighbor in getNeighbors(gene):
                if neighbor not in seen and neighbor in bank:
                    seen.add(neighbor)
                    queue.append((neighbor, depth + 1))
        return -1


solution = Solution()
print(solution.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))
# startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
# Output: 1

print(
    solution.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"])
)
# Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
# Output: 2
