
""" import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        result = []
        head = point = ListNode(0)
        
        heapq.heapify(result)
        for i in lists:
            while i:
                heapq.heappush(result,i.val)
                i = i.next
        for _ in range(len(result)):
            point.next = ListNode(heapq.heappop(result))
            point = point.next
        return head.next """