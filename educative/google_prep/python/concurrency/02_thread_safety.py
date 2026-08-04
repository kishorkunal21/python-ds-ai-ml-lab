#https://www.educative.io/courses/python-concurrency-for-senior-engineering-interviews/thread-safety

import dis

counter = 0
print(id(counter))

def increment():
    global counter
    counter += 1
    print(id(counter), counter)

increment() 

dis.dis(increment)