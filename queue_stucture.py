class Queue:
    def __init__(self):
        self.queue = [] 
    
    def enqueue(self,data):
        self.queue.append(data)
    

    def isEmpty(self):
        return len(self.queue) == 0
    
    def get_queue_data(self) :
        if self.isEmpty():
            return "Queue is empty"
        return self.queue
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        self.queue.pop(0)
        return "Element has been dequeued"
    def peek(self):
        if self.isempty():
            return "Queue is empty"
        return self.queue[0]
    def size(self):
        return len(self.queue)

queue_elements  =  ["A","B","C","D","E","F","G","H","I","J","K"]
myQueue = Queue()
for element in  queue_elements:
    myQueue.enqueue(element)
print(myQueue.get_queue_data())
print(myQueue.size())
print(myQueue.dequeue())
print(myQueue.size())
    
        
