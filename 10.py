class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None  # You can raise an exception or handle this differently if needed

    def is_empty(self):
        return len(self.items) == 0

    def __iter__(self):
        # The iterator should return elements in LIFO order, so we reverse the list.
        return iter(reversed(self.items))

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack Elements (LIFO order):")
for item in stack:
    print(item)

popped_item = stack.pop()
print("Popped Item:", popped_item)

# After popping an item, the remaining elements in the stack
print("Stack Elements after popping:")
for item in stack:
    print(item)
