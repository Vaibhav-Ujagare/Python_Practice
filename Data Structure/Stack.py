class Stack:
    def __init__(self,Data=None,Next=None):
        self.Data = Data
        self.Next = Next
        self.head=None

    def push(self,data):    
        node = Stack(data,self.head)        
        self.head=node        
    
    def get_lenght(self):
        itr = self.head
        count = 0
        while itr:
            itr= itr.Next
            count+=1
        return count
    
    def pop(self):
        top = self.head.Data
        self.head = self.head.Next
            
        return top

    def peek(self):
        return self.head.Data

    def print(self):
        itr=self.head
        while itr:
            print(itr.Data)
            itr=itr.Next

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    # s.print()
    print(s.pop())
    s.push(4)
    s.print()