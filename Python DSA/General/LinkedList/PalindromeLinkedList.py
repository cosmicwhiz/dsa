class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
        if not head:
            return None

        current = head
        values = []

        while current.next:
            values.append(current.val)
            current = current.next

        values.append(current.val)
        print(values)

        for i in range(len(values)//2):
            if values[i] != values[-i-1]:
                return False
        return True

    def reverseList(self, head):
        if head is None:
            return []
        current = head
        prev = None
        while current and current.next:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        current.next = prev
        return current
    
    def printList(self, head):
        current = head
        while current:
            print(current.val)
            current = current.next
    
    def reverseListII(self, head, left, right):
        nodesPosition = {}
        current = head
        count = 0
        while current:
            count += 1
            if count == left:
                nodesPosition[left] = current
            elif count == right:
                nodesPosition[right] = current
            current = current.next
            
        if left != right:
            prevNode = None
            #getting the node right before left
            if left > 1:
                current = head
                while current.next != nodesPosition[left]:
                    current = current.next
                prevNode = current

            current = nodesPosition[left]
            # prev stores node next to the right node
            prev = nodesPosition[right].next 
            
            while current != nodesPosition[right]:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            current.next = prev
            if left > 1:
                prevNode.next = current
            else:
                return current
        return head
        
listNode = ListNode(4)
listNode.next = ListNode(5)
listNode.next.next = ListNode(6)
listNode.next.next.next = ListNode(8)
listNode.next.next.next.next = ListNode(9)

solution = Solution()
# result = solution.isPalindrome(listNode)
# print(result)
head = solution.reverseListII(listNode, 1, 4)
solution.printList(head)