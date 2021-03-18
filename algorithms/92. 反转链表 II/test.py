# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 设置 dummyNode 是这一类问题的一般做法
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node
        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        return dummy_node.next

    def listToListNode(self, lists):
        dummy = ListNode(0)
        ptr = dummy
        for i in lists:
            ptr.next = ListNode(i)
            ptr = ptr.next

        ptr = dummy.next
        return ptr

data = Solution().listToListNode([1,2,3,4,5])
result = Solution().reverseBetween(data, 2, 4)
while result:
    print(result.val)
    result = result.next
