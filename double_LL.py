class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    #method for printing out the DLL
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    #add a node to list
    def append(self, value):
        #make a new node to be added
        new_node = Node(value)
        # if DLL is empty set head and tail to new_node
        if not self.head:
            self.head = new_node
            self.tail = new_node
        #otherwise add new_noded to the tail
        else:
           self.tail.next = new_node
           new_node.prev = self.tail
           self.tail = new_node 
        self.length += 1
        return True
    #method for removing node from the end
    def pop(self):
        temp = self.tail
        #if DLL is empty return None 
        if not temp:
            return temp
        #if DLL has one element set head and tail to none
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            #otherwise move tail back and then get rid 
            # of pointers to and from final element
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    #remove first element of DLL
    def prepend(self, value):
        new_node = Node(value)
        #if DLL is empty set head and tail to new_node
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:#otherwise add new_node to front and set head to new_node
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    #pop the first element
    def pop_first(self):
        temp = self.head
        #if DLL is empty return None
        if not temp:
            return temp
        #if DLL has one element set head and tail to none
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # otherwise move head forward and remove pointers between first element and head
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    #get a node at a certain index
    def get(self, index):
        #make sure index is within range
        if index < 0 or index >= self.length:
            return None
        #if the index we are getting is closer to the
        #  tail then start there and go backwards
        if index > self.length / 2:
            temp = self.tail
            for _ in range(self.length - index - 1):
                temp = temp.prev
        #if the index we are getting is closer to the head
        # then start at head and go forwards 
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        return temp
    #set a vlue of a certain node given an index
    def set_value(self, index, value):
        #get the node we want to change
        temp = self.get(index)
        #if temp is not None set its value
        if temp:
            temp.value = value
            return True
        #if temp is none return False
        return False
    #insert a new node at a given index
    def insert(self, index, value):
        #make sure index is within range
        if index > self.length or index < 0:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index-1)
        after = before.next
        new_node.next = after
        new_node.prev = before
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True
    #remove a node at a given index
    def remove(self, index):
        #make sure index is in range
        if index < 0 or index >= self.length:
            return False
        #if index is 0 call pop_first
        if index == 0:
            return self.pop_first()
        temp = self.get(index)
        #if temp is at end of DLL call pop
        if temp == self.tail:
            return self.pop()
        # set the pointers of the nodes before and after
        # to point to eachother and remove pointers on temp 
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.prev = temp.next = None
        self.length -= 1
        return temp
    #swap the value of the first and last nodes
    def swap_first_last(self):
        if self.length == 0:
            return False
        tailtemp = self.tail.value
        self.tail.value = self.head.value
        self.head.value = tailtemp
        return True

print('\n')
DLL = DoublyLinkedList(1)
DLL.append(2)
DLL.prepend(0)
DLL.remove(3)
DLL.print_list()
print('\n')
print(DLL.get(0).value)