#https://www.educative.io/courses/python-concurrency-for-senior-engineering-interviews/thread-safety

import time
from threading import Thread, Lock

class ThreadCounter:
    
    def __init__(self):
        self.counter = 0

    def increment(self):
        for _ in range(10000):
            self.counter +=1    
            time.sleep()
        print('incremented counter:"',self.counter) 

class ThreadSafeCounter:
    
    def __init__(self):
        self.counter = 0
        self.lock = Lock()

    def increment(self):
        for _ in range(10000):
            self.lock.acquire()
            self.counter +=1    
            time.sleep(0)
            self.lock.release()
        print('incremented counter:"',self.counter)         
class ThreadSafeCheck:
    import sys
    from threading import Thread, Lock

    threadCounter  = ThreadCounter() 
    threadSafeCounter = ThreadSafeCounter()
    if __name__ == '__main__':
        sys.setswitchinterval(0.0005)
        thread_count=5
        threads = [0]*thread_count
        print(f'initialised{threads}')    


        for i in range(thread_count):
            #threads[i]=Thread(target=threadCounter.increment)
            threads[i]=Thread(target=threadSafeCounter.increment)

        for i in range(thread_count):
            threads[i].start()
        
        for i in range(thread_count):
            threads[i].join()

        #if threadCounter.counter !=   50000:
        if threadSafeCounter.counter !=   50000:
            print('Counter not reached target 5000000')
        else:
            print('correct counter')    

threadSafeCheck = ThreadSafeCheck()

        



class UsingDis:
    import dis # dis is to show step by step how compilation is done[read + increment + set]

    def __init__(self):
        self.counter=0
        print(id(self.counter))
        

    def increment(self):
        #global counter
        self.counter += 1
        print(id(self.counter), self.counter)
        global counter
        counter = self.counter+10
        print('global',id(counter),counter)

    

#usingDis = UsingDis()
#usingDis.increment()
#usingDis.increment()


