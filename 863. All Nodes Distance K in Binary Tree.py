from collections import deque


def test(root, target, k):
    # 要給任意點，找到距離k的其他點，需要用graph的概念從該點向外走K步
    # 運用BFS可以很好辨識出K
    # 既然要用到graph的概念就需要，把原本的BST轉換成無向圖

    # 原本點只有 left, right, val，現在要多一個parent

    # 用DFS (遞迴)(比較乾淨)，走遍每個點，把每個點的parent補上

    def dfs(node, parent):
        if not node:
            return

        node.parent = parent
        dfs(node.left, node)
        dfs(node.right, node)

    dfs(root, None)

    # 用BFS從targetNode開始走，走K層，就是答案

    queue = deque([target])
    seen = set(target)
    distance = 0

    while queue:
        nodes_in_current_level = len(queue)

        if distance == k:
            return [node.val for node in queue]

        for _ in range(nodes_in_current_level):
            node = queue.popleft()

            for n in [node.left, node.right, node.parent]:
                if n and (n.val) not in seen:
                    queue.append(n)
                    seen.add(n)
        distance += 1
