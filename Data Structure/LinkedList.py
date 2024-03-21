class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
        self.head = None

    def insert_at_begning(self,data):
        node = Node(data,self.head)
        self.head=node

    def print(self):
        itr = self.head
        llstr = ''
        while itr:
            suffix = ""
            if itr.next:
                suffix = "-->"
            llstr+=str(itr.data)+suffix
            itr=itr.next
        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        itr = self.head
        while itr.next:
            itr=itr.next
        itr.next = Node(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    def insert_at(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        elif index == 0:
            self.insert_at_begning(data)
        else:
            itr = self.head
            count = 0
            while itr:
                if count == index -1:
                    node = Node(data,itr.next)
                    itr.next = node
                    break
                itr = itr.next
                count+=1

    def remove_at(self,index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        elif index == 0:
            self.head = self.head.next
        else:
            itr = self.head
            count = 0
            while itr:
                if count == index - 1:
                    itr.next = itr.next.next
                    break
                itr = itr.next
                count+=1
    
    def insert_bulk_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self,data_after,data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert,itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self,data):
        itr = self.head
        llstr=''
      
        while itr: 
            suffix="-->"            
            if itr.data != data:                                 
                llstr+=str(itr.data)+suffix          
                suffix=""                 
            itr = itr.next
        
        print(llstr)

            
        

if __name__ == '__main__':
    root = Node()
    root.insert_bulk_values(["a","b","v"])
    root.print()
    root.remove_by_value("v")
    print(root.get_length())