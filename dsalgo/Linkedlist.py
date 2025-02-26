class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        
        

class Linkedlist:
    def __init__(self):
        self.head = None
        self.n = 0
        
    # magic len() 
    def __len__(self):
        return self.n
    
    # magic print() 
    def __str__(self):
        current = self.head
        result = ""
        while current != None:
            result+= str(current.data) + ' -> '
            current = current.next
        return result[:-3] 
    
    # insert node 
    def insert_head(self, value):
        new_node = Node(value) #new node create
        new_node.next = self.head #create connection with head
        self.head = new_node #current head is new node
        self.n += 1
    
    # append node
    def append(self, value):
        new_node = Node(value)
        current = self.head
        if current == None: # execute this when no item in LL
            self.head = new_node
            self.n += 1
            return
        
        while current.next != None: # execute this when already have item
            current = current.next
        current.next = new_node
        self.n += 1
        
    def insert_after(self, after, value):
        new_node = Node(value)
        current = self.head
        while current != None:
            if current.data == after:
                break 
            current = current.next
        if current != None: # execute when while loop got a value and break while
            new_node.next = current.next
            current.next = new_node
            self.n +=1
        else:
            print("Item not found") 
            
    def clear(self):
        self.head = None   
        self.n = 0

    def delete_head(self):
        if self.head == None:
            return "Empty List"
        self.head = self.head.next
        self.n -= 1
    
    def pop(self):
        current = self.head
        if current == None:
            return 
        if current.next == None:
            self.delete_head()
            return 
        while current.next.next != None:
            current = current.next
        
        # current is 2nd last item
        current.next = None
        self.n -= 1
    
    def remove(self, value):
        current = self.head
        if self.head == None:
            return print("Empty Linked list") 
        if current.data == value:
            self.delete_head()
            return
        while current.next != None:
            if current.next.data == value:
                break
            current = current.next
        if current.next == None:
            print("Not Found") 
        else:
            current.next = current.next.next
            self.n -= 1
    def search(self, item):
        current = self.head
        position = 0
        while current != None:
            if current.data == item:
                return position
            position += 1
            current = current.next
        return "Not Found"
    def reverse(self):
        prev_node = None #doing for maintain loop
        current_node =self.head #doing for maintain loop

        while current_node != None:
            print(current_node.data, "current node")
            next_node = current_node.next #doing for maintain loop
            current_node.next = prev_node #reversing
            prev_node = current_node #doing for maintain loop
            current_node = next_node #doing for maintain loop
        self.head=prev_node
    
    def __getitem__(self, index):
        current = self.head
        position = 0
        while current != None:
            if position == index:
                return current.data
            position += 1 
            current = current.next
        return "Index error "
ll = Linkedlist()


ll.append(10)
ll.append(20)
ll.append(30)

ll.reverse()
print(ll)