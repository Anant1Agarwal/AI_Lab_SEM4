class Stack:
    def __init__(self):
        self.items=[]
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            print("Stack is Empty. Dont have anything to pop!")
    
    def peek(self):
        return self.items[-1] if self.items else None
    
    def is_empty(self):
        return len(self.items)==0
    
    def size(self):
        return len(self.items)
# another way of writing
# return self.items.pop() if self.items else None
    
# def main():
#     my_stack=Stack()

#     my_stack.push(1)
#     my_stack.push(2)
#     my_stack.push(3)

#     print("Stack is:",my_stack.items)
#     print("Peek:",my_stack.peek())
#     print("Pop:",my_stack.pop())
#     print("Stack size:",my_stack.size())

# if __name__=="__main__":
#     main()