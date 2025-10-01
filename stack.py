#stack is alinear data strucutres  thst follows last in first out print (LIFO)

# operations in aStack
"""
Push , - adds as new element ijn the stack
Pop,  - removes and retrun the top last  element in the stuck
Size,   - checks the size of the stack 
isEmpty  - check weather the stack is empty
Peek - returns the  top last element in the stack
"""
# stack can be implement using arrays or linked list

"""
Stacks can be used to implement undo mechanisms, to revert to previous states, to create algorithms for depth-first search in graphs, or for backtracking.

Stacks are often mentioned together with Queues, which is a similar data structure described on the next page.
"""

stack  =  []

stack.append("A")
stack.append("B")
stack.append("C")
stack.append("D")
stack.append("E")
stack.append("F")
print(stack)
print(stack[-1])
print(stack.pop())


