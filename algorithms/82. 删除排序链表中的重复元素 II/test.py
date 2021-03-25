# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy = ListNode(0, head)

        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next

    def listToListNode(self, lists):
        dummy = ListNode(0)
        ptr = dummy
        for i in lists:
            ptr.next = ListNode(i)
            ptr = ptr.next

        ptr = dummy.next
        return ptr

data = Solution().listToListNode([1,1,1,2,3])
result = Solution().deleteDuplicates(data)
while result:
    print(result.val)
    result = result.next
