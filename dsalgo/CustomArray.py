import ctypes

class CustomArray:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.__make_array(self.size)
        
    def __len__(self):
        return self.n  
    
    # print 
    def __str__(self):
        result = ''
        for i in range(self.n):
            result += str(self.A[i])+','
        return '[' + result[:-1] + ']'
    
    # get index 
    def __getitem__(self, index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return 'Index out of range'
    
    # delete 
    def __delitem__(self, index):
        if 0 <= index < self.n:
            for i in range(index, self.n-1):
                self.A[i] = self.A[i+1]
            self.n -= 1
    
    def remove(self, item):
        index = self.find(item)
        self.__delitem__(index)
    
    def insert(self, index, item):
        if self.n == self.size:
            self.__resize(self.size + 4)

        for i in range(self.n, index, -1):
            self.A[i] = self.A[i-1]
        self.A[index] = item
        self.n += 1
        
    def clear(self):
        self.n = 0
        self.size = 1
    
    def pop(self):
        if self.n == 0:
            return "Empty List"
        self.n -= 1
        return self.A[self.n]
    
    def find(self, item):
        for i in range(self.n-1):
            if self.A[i] == item:
                return i
        return "No such item"
        
    def append(self, item):
        if self.n == self.size:
            self.__resize(self.size + 4)
        # append 
        self.A[self.n] = item
        self.n = self.n + 1
    
    def __resize(self, new_capacity):
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        # copy the content of A to B
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        
    # Static array create by ctypes 
    def __make_array(self, capacity):
        return (capacity * ctypes.py_object)()


arr = CustomArray()

arr.append("hello")
arr.append("world")
arr.append(1)
arr.append(2)



print(arr)
arr.remove('world')
arr.remove(1)
print(arr)
