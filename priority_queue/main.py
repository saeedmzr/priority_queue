from priority_queue import PriorityQueue

a = PriorityQueue()

a.append("one", 1)
a.append("two", 2)
a.append("three", 3)
a.append("highest", 38)
a.append("second high", 22)
a.append("ten", 10)
a.append("nine", 9)

print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
