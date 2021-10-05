# Python Basic Data Structures
## Array
Python's list is internally implemented as an array. Access an element by an index is O(1).

### Indexing
Negative indices are also allowed. A handy way to access the last element is:
```
>>> a = [1, 2, 3]
>>> a[-1]
3
```
Subarray slicing indices are left-inclusive and right-exclusive. For example
```
>>> a = [0, 10, 20, 30, 40, 50]
>>> a[2:5] # element from index 2 to index 4 (cuz right exclusive, 5-1=4)
[20, 30, 40]
```
This is very important. Mishandling the right-exclusivity is a common source of error in coding interview problems such as two-pointer problems.

There's also a shorthand for slicing from element 0. For example:
```
>>> a = [0, 10, 20, 30, 40, 50]
>>> a[:2]
[0, 10]
```
and slicing until
```
>>> a = [0, 10, 20, 30, 40, 50]
>>> a[2:]
[20, 30, 40, 50]
```
A note on right-exclusivity. Array and list indices are left inclusive and right exclusive in most languages including Python and Java. The reason for this design is up for speculation. According to a stackover flow post, Python inventor Guido Van Rossum was quoted as saying "I was swayed by the elegance of half-open intervals. Especially the invariant that when two slices are adjacent, the first slice's end index is the second slice's start index is just too beautiful to ignore. For example, suppose you split a string into three parts at indices i and j -- the parts would be a[:i], a[i:j], and a[j:]." For our practical purposes in solving coding problems, we often have to deal with edge cases such as an empty list. And this notation becomes convenient because to represent an empty array we can write a[i:i] instead of the more awkward ar[i:i-1].

In general, to iterate through a list, for loop is easier to reason than while since there's no condition to manage that could skip elements. You can also use enumerate to get both index and element at the same time.
```
>>> nums = [0, 10, 20, 30, 40, 50]
>>> for i, num in enumerate(nums):
...     print(i, num)
...
0 0
1 10
2 20
3 30
4 40
5 50
```
## Linked List
Python doesn't have a built-in linked list. Normally at an interview, you'll be given a definition like this
```
class LinkedListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
```
append to end is O(1).

finding an element is O(N).

Besides problems that specifically ask for linked lists, you don't normally define and use linked list. If you need a list with O(1) append you can use the built-in list, and if you want O(1) for both prepend and append you can use the built-in deque.

## Stack
Python's list also doubles as a stack. For a list l = []

push: append, O(1)

pop: pop,O(1)

size: len(l), O(1)

top: l[0], O(1)

Stack is arguably the most magical data structure in computer science. In fact, with two stacks and a finite-state machine you can build a Turing Machine that can solve any problem a computer can solve.

Recursion and function calls are implemented with stack behind the scene. We'll discuss this in the recursion review module.

## Queue
Python's collections.deque is a double-ended queue, which means you can push and pop an element from either end in constant time. In the coding interviews, this is what we normally use when we need a queue. For a deque q = deque()

enqueue: q.append, O(1)

dequeue: q.popleft(), O(1). Note that it's pop*left*. pop is also supported but it's for getting element at the end of the double-ended queue.

size: len(q), O(1)

In coding interviews, we see queues most often in breath-first search. We'll also cover monotonic deque where elements are sorted inside the deque that is useful in solving some advanced coding problems.

## Hash Table
Python's dict is an implementation of the hash table. For a dictionary d = {},

get using a key: d[key], O(1)

set a key, value: d[key] = value, O(1)

remove a key: del d[key], O(1)

It's worth mentioning that these are average case time complexity. A hash table's worse time complexity is actually O(N) due to hash collision and other things. For the vast majority of the cases and certainly most coding interviews, the assumption of constant time lookup/insert/delete is valid.

Use a hash table if you want to create a mapping from A to B. Many starter interview problems can be solved with a hash table.

For counting things, python has a convenient class Counter.

## Hash Set
Python's set is an implementation of hash set. It's useful in answering the existence queries in constant time. For a set s = set(),

is a in set s: a in s, O(1)

adding a to set: s.add(a), O(1). Duplicates will be discarded.

removing a from set: s.remove(a), O(1). Does nothing if a is not in a set.

Hash set is useful when you only need to know existence of a key. Example use cases include DFS and BFS on graphs.

## Tree
Python does not have built-in tree support. Normally at an interview, you'd be given the following implementation for binary tree.
```
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```
For n-nary trees:
```
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []
```