class Queue:
    def __init__(self):
        self.queue_list = []

    def size(self):
        return len(self.queue_list)

    def is_empty(self):
        return self.size() == 0

    def front(self):
        if self.is_empty():
            print("Empty Queue")
            return None
        return self.queue_list[0]

    def back(self):
        if self.is_empty():
            print("Empty Queue")
            return None
        return self.queue_list[-1]

    def enqueue(self, data):
        self.queue_list.append(data)

    def dequeue(self):
        if self.is_empty():
            print("Underflow.")
            return None
        front = self.front()
        self.queue_list.remove(front)
        return front


if __name__ == "__main__":
    queue = Queue()

    print("queue.enqueue(2);")
    queue.enqueue(2)
    print("queue.enqueue(4);")
    queue.enqueue(4)
    print("queue.enqueue(6);")
    queue.enqueue(6)
    print("queue.enqueue(8);")
    queue.enqueue(8)
    print("queue.enqueue(10);")
    queue.enqueue(10)

    print("Dequeue(): " + str(queue.dequeue()))
    print("Dequeue(): " + str(queue.dequeue()))

    print("front(): " + str(queue.front()))
    print("back(): " + str(queue.back()))

    print("queue.enqueue(12);")
    queue.enqueue(12)
    print("queue.enqueue(14);")
    queue.enqueue(14)

    while queue.is_empty() is False:
        print("Dequeue(): " + str(queue.dequeue()))

    print("is_empty(): " + str(queue.is_empty()))
