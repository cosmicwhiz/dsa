class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeDuplicates(self, head):
        if head is None:
            return None
        if head.next is None:
            return head

        current = head.next
        res = head
        prev = head
        lastNewVal = head

        while current:
            if current.val != prev.val:
                res.next = current
                res = res.next
                lastNewVal = current
            prev = current
            current = current.next
        lastNewVal.next = None
        return head

    def printList(self, head):
        current = head
        while current:
            print(current.val)
            current = current.next

    def removeListElements(self, head, val):
        current = head.next
        res = head
        while current:
            if current.val != val:
                res.next = current
                res = res.next
            current = current.next
        res.next = None
        if head.val == val:
            head = head.next
        return head
    
    def removeMiddleNode(self, head):
        if head.next is None:
            return None

        current = head
        count = 0
        while current:
            count += 1
            current = current.next

        mid = count//2
        current = head
        count = 0

        while count < mid-1:
            count += 1
            current = current.next

        temp = current.next.next
        current.next = temp

        return head



listNode = Node(1)
# listNode.next = Node(2)
# listNode.next.next = Node(3)
# listNode.next.next.next = Node(4)
# listNode.next.next.next.next = Node(3)

solution = Solution()
res = solution.removeMiddleNode(listNode)
solution.printList(res)