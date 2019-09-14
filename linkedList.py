class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
    
    def getvalues(self):
        return [self.val,self.next]
    
head = point = ListNode(0)
nodes = [2,3,4,7,1,2]

for x in sorted(nodes):
    point.next = ListNode(x)
    point = point.next

print(head.getvalues())
print(head.next)
print(point.getvalues())