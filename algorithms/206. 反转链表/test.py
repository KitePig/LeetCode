# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head

        while cur:
            # 先把原来cur.next位置存起来
            # 当前节点 下一个节点等于上一个节点
            # 当前节点作为上一个节点
            # 节点下移
            temp_node = cur.next
            cur.next = pre
            pre = cur
            cur = temp_node

        return pre

    def listToListNode(self, lists):
        dummy = ListNode(0)
        ptr = dummy
        for i in lists:
            ptr.next = ListNode(i)
            ptr = ptr.next

        ptr = dummy.next
        return ptr

data = Solution().listToListNode([1,2,3,4,5])
result = Solution().reverseList(data)
while result:
    print(result.val)
    result = result.next
