from array import array


class PriorityQueue:
    def __init__(self):
        self.items = []
        self.priorities = {}

    def append(self, item, priority=0):
        self.items.append(item)
        self.priorities[item] = priority

    def max_item(self, input_array: dict):
        max_priority = max(input_array.values())
        key = 0
        for (k, v) in input_array.items():
            if v == max_priority:
                key = k
                break
        return key, max_priority

    def pop(self):
        max_priority = self.max_item(self.priorities)
        self.priorities.pop(max_priority[0])
        self.items.remove(max_priority[0])
        return max_priority[0]


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
