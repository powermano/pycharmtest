class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # count = 1
        # a = head
        # b = head
        # while head.next != None:
        #     head = head.next
        #     count += 1
        # if count == 1:
        #     return None
        # elif n == count:
        #     return a.next
        # else:
        #     for i in range(count-n-1):
        #         a = a.next
        #     a.next = a.next.next
        #     return b

        p1 = p2 = head
        for _ in range(n):
            p1 = p1.next
        if not p1:  # p1为空则n为length-1
            return head.next
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return head

