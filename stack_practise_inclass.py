class Stack :
    def __init__(self):
        self.stack = []
    
    def push(self,element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
    
    def isEmpty(self):
        return len(self.stack) ==0 
    
    def size(self):
        return len(self.stack)
    
    
mystack  = Stack()
mystack.push("window-1")
mystack.push("window-2")
mystack.push("window-3")
mystack.push("window-4")
mystack.push("window-5")

print(mystack.stack)
print(mystack.isEmpty())


  