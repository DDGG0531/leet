from collections import defaultdict


def test(isConnected):
    # DFS 簡單講就是 鑽鑽樂，要鑽到底，才會折返
    # 通常都是用遞迴的方式實作
    # 這裡要用迭代的方式實作

    # 避免循環的seen
    seen = set()

    # 隨便放入一個點，用DFS走訪，走完時，就會把同一區塊的點都放進seen裡面
    # 所以答案的數量就等於，放入的點有真正觸發DFS的數量

    # 先把難用的adjacency matrix轉成好用的adjacency list

    graph = defaultdict(list)
    for i in range(len(isConnected)):
        for j in range(i + 1, len(isConnected)):
            if isConnected[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)

    def dfs(i):
        # 我需要利用stack資料結構來完成
        stack = [i]
        while stack:
            i = stack.pop()
            seen.add(i)

            for neighbor in graph[i]:
                if neighbor not in seen:
                    stack.append(neighbor)

    ans = 0
    # 走訪每個點
    for i in range(len(isConnected)):
        if i not in seen:
            ans += 1
            dfs(i)

    return ans


print(test([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
print(test([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))  # 3
