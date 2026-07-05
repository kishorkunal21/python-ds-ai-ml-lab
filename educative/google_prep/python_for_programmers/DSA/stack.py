class Stack:
    
    def __init__(self):
        self.item = []
        
        
    def peek(self):
        return self.item[-1]

    def pop(self):
        popped = self.item[-1]
        print(self.item)
        self.item = self.item[:len(self.item)-1]
        print("Popped : ",popped, 'Stack : ',self.item)
        return popped

    def push(self, num):
        self.item.append(num)
        print('Added : ',self.item)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("peek",stack.peek())
stack.pop()
stack.pop()
stack.pop()
stack.pop()

