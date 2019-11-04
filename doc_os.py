import threading 
import timeit

class CircularBuffer(object):

    def __init__(self, max_size=10):
       
        self.buffer = [None] * max_size
        self.head = 0
        self.tail = 0
        self.max_size = max_size

    def __str__(self):
       
        items = ['{!r}'.format(item) for item in self.buffer]
        return '[' + ', '.join(items) + ']'

    def size(self):
       
        if self.tail >= self.head:
            return self.tail - self.head
        return self.max_size - self.head - self.tail

    def is_empty(self):
        
        return self.tail == self.head

    def is_full(self):
        
        return self.tail == (self.head-1) % self.max_size

    def enqueue(self, item):
        
        if self.is_full():
            #raise OverflowError
            print("Full")
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size
        print(self.tail)

    def front(self):
        
        return self.buffer[self.head]

    def dequeue(self):
       
        if self.is_empty():
            #raise IndexError
            print("Full")
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.max_size
        return item


if __name__ == "__main__":
        # creating thread
    cb = CircularBuffer(1000)
    start = timeit.timeit()
    for index in range(0,999):
        t1 = threading.Thread(target=cb.enqueue("one")) 
        t2 = threading.Thread(target=cb.enqueue("two")) 
        # starting thread 1 
        t1.start() 
        # starting thread 2 
        t2.start()
            
        # wait until thread 1 is completely executed 
        t1.join() 
        # wait until thread 2 is completely executed 
        t2.join() 

            # Examples
        print(cb)
    print("Empty: {}".format(cb.is_empty()))
    print("Full: {}".format(cb.is_full()))
    end = timeit.timeit()
    print(end - start)
    
