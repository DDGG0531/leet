from collections import defaultdict

[[1, 1, 0], [1, 1, 0], [0, 0, 1]]


def test(isConnected):
    # 走訪每個點，但要確保不走重複的點 => seen
    # 走訪時用DFS走，可以確保不會有點被漏掉
    # PS: 建立graph dict 可以提前算出每個點的鄰居是誰!
    # PS: DFS 走訪時，要用鄰居做遞迴，graph dict派上用場了!
    # Q: DFS遞迴時，要怎麼確保不走重複的點? => seen

    # 先建立graph
    n = len(isConnected)
    graph = defaultdict(list)
    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j] == 1:
                # 找出每個點的鄰居
                graph[i].append(j)
                graph[j].append(i)

    # 建立seen
    seen = set()
    # 前置作業結束，可以開始找答案了
    ans = 0

    # 走訪該點的鄰居
    def dfs(node):
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                dfs(neighbor)

    # 走訪每個點
    for i in range(n):
        if i not in seen:
            # 此處執行DFS
            # PS: DFS的目的就是把同一區塊的點，都放進seen裡面
            dfs(i)
            seen.add(i)
            ans += 1
    return ans


print(test([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
print(test([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))  # 3
