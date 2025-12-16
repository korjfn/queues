class Queue:
    def __init__(self):
        self.q = []


    def enqueue(self,element):
        self.q.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "queue is empty"
        return self.q.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty" 
        return self.q[0]
    
    def isEmpty(self):
        return len(self.q) == 0
    
    def size(self):
        return len(self.q)



queue = Queue()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')


print("queue:", queue.q)
print("dequeue", queue.dequeue())
print("peek", queue.peek())
print("IsEmpty", queue.isEmpty())
print("Size", queue.size())