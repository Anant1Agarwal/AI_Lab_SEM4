class Queue:
    def __init__(self):
        self.items=[]
    
    def enqueue(self,data):
        self.items.append(data)

    def dequeue(self):
            return self.items.pop(0) 

    def is_Empty(self):
        return (len(self.items)==0)
    
    def front(self):
         return self.items[0]

    def size(self):
         return len(self.items)

# def main():
#      my_queue=Queue()
#      my_queue.enqueue(1)
#      my_queue.enqueue(2)
#      my_queue.enqueue(3)
#      print("Queue:", my_queue.items)
#      print("Front:", my_queue.front())
#      print("Dequeue:", my_queue.dequeue())
#      print("Queue size:", my_queue.size())
#      print("Queue:", my_queue.items)

# if __name__ == "__main__":
#     main()