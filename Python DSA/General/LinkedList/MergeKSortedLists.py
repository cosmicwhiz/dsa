class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    res, prev = None, None
    while True:
        miniNode, mini = None, 1e5
        ind = 0
        for i, head in enumerate(lists):
            if head and head.val < mini:
                miniNode, mini = head, head.val
                ind = i
        if not miniNode:
            break
        lists[ind] = lists[ind].next
        miniNode.next = None
        if prev:
            prev.next = miniNode
        else:
            res = miniNode
        prev = miniNode
    return res


tempLists = [[1,4,5],[1,3,4],[2,6]]
lists = []
for row in tempLists:
    head = ListNode(row[0])
    current = head
    for n in row[1:]:
        current.next = ListNode(n)
        current = current.next
    lists.append(head)

res = mergeKLists(lists)
while res:
    print(res.val, end=" ")
    res = res.next