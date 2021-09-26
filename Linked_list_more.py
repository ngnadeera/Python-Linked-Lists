class Node:
    
    """ Node that contain the data and a referance to the next node
    """
    
    data = None
    next_node = None
    
    def __init__ (self,data):
        
        self.data = data
        
    def __repr__(self):
        
        return f"Node Data: <{self.data}>"
    
class Linkedlist:
    """singly linked list
    """
    def __init__(self):
        
        self.head = None
        
    def is_empty (self):
        """ check whether the list is empty 
        """
        
        return self.head == None     #True or False
        
    def length (self):
        """ determine the number of nodes in the l.l
            run in  linear time O(n)
        """
        
        current = self.head     #as a inisitive
        count = 0
        
        while current :
            
            count += 1
            current = current.next_node   #N1.next_node = N2   when it comes to tail. N3.next_node = None false the loop
            
        return count
    
    def node_at_the_index (self,index):
        """ 
        return the node correspond to the index
        """
        position = 0
        if index == 0 :
            return self.head 
        else:
            current = self.head
            while index > position:
                current = current.next_node
                position += 1
            return current
                
            
        
    
    def add(self,data):
        """ add new node which contain data at the head of the list
            run in a constant time O(1)
        """     
        new_node = Node(data)
        new_node.next_node = self.head         
        self.head = new_node                   #just because this change the head and not iterating through the wole loop everytime this runs in a constant time
        
    def search(self,key):
        
        """ search for the first node that contain the key
            return the node or the None if it isn't there
        
            take O(n) time means run in linear time
        """    
        
        current = self.head
        
        while current:
            
            if current.data == key :
                return current 
            
            else:
                
                current = current.next_node
            
        return None
    
    def insert(self,data,index):
        
        """ inserting new node at contaning data at index position
            insertion takes constant time O(1) but finding the data at the 
            insertion position takes linear time O(n)
        
            takes overall O(n) time...
        """
        
        new = Node(data)
        
        if index == 0 :
            self.add(data)
            
        if index > 0 :
            
            current = self.head
            position = index
            
            while position > 1:
                
                current = current.next_node
                position -= 1   
                
            prev_node = current
            next_node = current.next_node
            
            prev_node.next_node = new
            new.next_node = next_node
                
    def remove(self,key):
        
        """ removes node containg data that matches the key
            return a error message if key doesn't exist
        
            takes O(n) time 
        """    

        current = self.head
        found = False
        previous = None
        
        while current and not found:
            
            if current.data == key and current == self.head:
                self.head = current.next_node
                found = True
                return found
            if current.data == key:
                previous.next_node = current.next_node
                found = True
                return found
            
            else:
                previous = current
                current = current.next_node
        print(f"the key {key} wasn't found inside the linked list")        
        
        
            
            
    def pop (self,index):
        
        """ remove node containig data that matches the index 
            return a error if key doesn't exist
        
            run in O(n) time... 
        """
        
        current = self.head
        position = index
        previous = None
         
        count = position
         
        while current and position != 0:
             
             if count == 0:
                 
                 previous.next_node = current.next_node
                 return True
             else:
                 
                 previous = current
                 current = current.next_node
                 count -= 1
         
        if position == 0:
             
             self.head = current.next_node
             return True
        else:
             
             print("index is out of the bound")
                
    
    def __repr__(self):
        
        """ take O(n) times
        """
        
        nodes = []
        current = self.head

        while current :
            
            if current == self.head:
                
                nodes.append(f"[Head: {current.data}]")
            
            elif current.next_node is None :
                
                nodes.append(f"[Tail: {current.data}]")
                
            else:
                
                nodes.append(f"[{current.data}]")
                
            current = current.next_node
            
        return "->".join(nodes)  
    
    