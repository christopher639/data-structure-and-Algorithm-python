class  Stack :
    def __init__(self):
        self.stack = []
    
    def push(self,element):
        self.stack.append(element)
    
    def  pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0 
    
    def size(self):
        return len(self.stack)

# creating a stack 

mystack = Stack()

mystack.push("Q")
mystack.push("w")
mystack.push("e")
mystack.push("r")
mystack.push("t")
print(mystack.stack)
print(mystack.size())
print(mystack.isEmpty())

print(mystack.pop())
