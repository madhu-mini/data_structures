class Stack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        return self.size() == 0

    def top(self):
        if self.is_empty():
            print("Empty Stack.")
            return None
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, element):
        self.stack_list.append(element)

    def pop(self):
        if self.is_empty():
            print("Underflow")
            return None
        return self.stack_list.pop()


if __name__ == "__main__":
    stack = Stack()
    for i in range(5):
        stack.push(i)
    print("top(): " + str(stack.top()))
    for x in range(5):
        print(stack.pop())
    print("is_empty(): " + str(stack.is_empty()))
