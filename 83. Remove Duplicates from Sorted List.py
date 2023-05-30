def solution(head):
    if not head:
        return head
    travel = head
    recordNode = travel
    while travel:
        # 判斷是否重複，如果重複就忽略
        # 否則就把recordNode跟當前的點做連接
        if recordNode.val != travel.val:
            recordNode.next = travel
            recordNode = travel
        # 移動
        travel = travel.next
    recordNode.next = None

    return head
