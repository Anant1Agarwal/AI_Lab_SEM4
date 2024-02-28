from simpleStack import Stack

class Queue:
    def __init__(self):
        self.stack1=Stack()
        self.stack2=Stack()

    def enqueue(self,data):
        self.stack1.push(data)
 
    def dequeue(self):
        if not self.stack2.is_empty():
            return self.stack2.pop()
        else:
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        
        return self.stack2.pop()
    
    def is_Empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()

def main():
     my_queue=Queue()
     my_queue.enqueue(1)
     my_queue.enqueue(2)
     my_queue.enqueue(3)
     print("Queue:", my_queue.stack1.items)
    #  print("Front:", my_queue.front())
     print("Dequeue:", my_queue.dequeue())
     print("Dequeue:", my_queue.dequeue())
    #  print("Queue size:", my_queue.size())
     print("Queue:", my_queue.stack2.items)

if __name__ == "__main__":
    main()