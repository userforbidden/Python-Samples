# Python, you can use the deque class of the collections module 
from collections import deque

#Initialize a new deque 
queue = deque()
#Add 2 to the end of the deque
queue.append(2)
#Add 4 to the front of the deque
queue.appendleft(4)
# Look at the end of the deque and print it 
print("End of Queue {}".format(queue[-1]))
# Look at the front of he deque and print it 
print("Front of Queue {}".format(queue[0]))
# remove from the end of deque
queue.pop()
# remove from the front of deque
queue.popleft()