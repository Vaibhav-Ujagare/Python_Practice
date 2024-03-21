class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self,key):
        hash=0
        for char in key:
            hash+=ord(char)
        return hash % self.MAX
        
    def __getitem__(self,index):
        h = self.get_hash(index)
        for elem in self.arr[h]:
            if elem[0] == index:                
                return elem[1]
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        Found = False
        for index,value in enumerate(self.arr[h]):
            if len(value) == 2 and value[0] == key:
                self.arr[h][index] = (key,val)
                Found = True
        if not Found:
            self.arr[h].append((key,val))




if __name__=="__main__":
    t = HashTable()
    
    t['march 6'] = 322
    t['march 17'] = 3221
    t['march 26'] = 32

    print(t['march 26'])