class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

curr = Node(1,'next','random')
dict = {}
dict[curr] = Node(curr.val,None,None)
print(dict.get(curr).next)
print(dict.get(curr).random)
dict.get(curr).next = curr.next
dict.get(curr).random = curr.random
print(dict.get(curr).next)
print(dict.get(curr).random)
print(curr.val,curr.next,curr.random)
print(dict)


# class Solution(object):
#     def copyRandomList(self, head):
#         """
#         :type head: Node
#         :rtype: Node
#         """
#         if not head:
#             return None
        
#         cloneMap = {}
        
#         curr = head
#         while curr:
#             cloneMap[curr] = Node(curr.val,None,None)
#             curr = curr.next
        
#         curr = head
        
#         while curr:
#             cloneMap[curr].next = cloneMap[curr.next]
#             cloneMap[curr].random = cloneMap[curr.random]
#             curr = curr.next
            
#         print(cloneMap[head])