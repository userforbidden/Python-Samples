import heapq



input = [ [3,5,7], [0,6], [0, 6, 28] ]
result = []
mergedResult = []
for i in input:
    result = result + i

print(result)

heapq.heapify(result)

for _ in range(len(result)):
    mergedResult.append(heapq.heappop(result))

print([heapq.heappop(result) for _ in range(len(result))])


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