def solution(head):
    # 1. 使N反轉
    # - N 是誰: current
    # - N要轉去哪裡: prev
    # - 為了不遺失N，誰要指向N: next
    # prev -> current -> next
    # prev <- current <- next

    def revertANode(prev, current):
        if current == None:
            return prev
        next = current.next
        current.next = prev
        return revertANode(current, next)

    current = head
    prev = None
    return revertANode(prev, current)
