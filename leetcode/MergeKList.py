# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
#
#         res = None
#         for i in range(len(lists)):
#             res = self.mergeTwoLists(res, lists[i])
#         return res
#
#     def mergeTwoLists(self, l1, l2):
#         if not l1 or not l2:
#             return l1 or l2
#         if l1.val < l2.val:
#             l1.next = self.mergeTwoLists(l1.next, l2)
#             return l1
#         else:
#             l2.next = self.mergeTwoLists(l1, l2.next)
#             return l2

        return self.divide(lists, 0, len(lists) - 1)


    def divide(self, lists, start, end):
        if start == end:
            return lists[start]
        if start < end:
            mid = (end + start) // 2
            l1 = self.divide(lists, start, mid)
            l2 = self.divide(lists, mid + 1, end)
            return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):

        # if not l1 or not l2:
        #     return l1 or l2
        # if l1.val < l2.val:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l1, l2.next)
        #     return l2
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
############
#for test PriorityQueue
import queue
import threading
import operator
import random

# class Job(object):
#     def __init__(self, priority, description):
#         self.priority = priority
#         self.description = description
#         print ('Job:',description)
#         return
#     def __lt__(self, other):
#         return self.priority < other.priority




# q = queue.PriorityQueue()
#
# # q.put(Job(3, 'level 3 job'))
# # q.put(Job(10, 'level 10 job'))
# # q.put(Job(1, 'level 1 job'))
# # q.put(Job(5, 'level 5 job'))
# # q.put(Job(4, 'level 4 job'))
# def generator_job(q):
#     for i in range(5, 1, -1):
#         a = random.randint(1,10)
#         q.put(Job(a, 'level %d job'%a))
#
# def process_job(q):
#     while True:
#         next_job = q.get()
#         print ('for:', next_job.description)
#         # q.task_done()
#
# workers = [threading.Thread(target=generator_job, args=(q,)),
#         threading.Thread(target=process_job, args=(q,))
#         ]
#
# for w in workers:
#     w.setDaemon(True)
#     w.start()
#
# # q.join()
# for i in workers:
#     i.join()







