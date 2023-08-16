#example of how to think of a linked list
head = {
    "value": 1,
    "next": {
        "value": 2,
        "next": {
            "value": 3,
            "next": {
                "value": 4,
                "next": None
            }
            
        }
    }
}
#print(head['next']['next']['value'])

#####################################
""" LL class """

#use whenever need to create a node for LL
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value) -> None:
        #create a node using the passed value
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    #create a new node at end
    def append(self, value):
        #create a new node to go at end
        new_node = Node(value)
        #if there is no head make head and tail point to new_node
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            # set the next value of the tail node equal to new_node
            self.tail.next = new_node
            self.tail = new_node
        #increase length of LL
        self.length += 1
        #dont need to return true but can for use with insert
        return True
    
    #remove from the end of the linked list and return node removed
    def pop(self):
        #if LL is empty return None
        if self.head == None:
            return None
        temp = self.head
        pre = self.head
        #increment temp and pre until temp gets to last node and pre is at pointer to last node
        while temp.next != None:
            pre = temp
            temp = temp.next
        #set tail to pre and tail.next to None
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        #if all nodes have been removes set tail and head to none
        if self.length == 0:
            self.head = None
            self.tail = None
        #dont need to return true but can for use with insert
        return temp

    #create new node at beginning
    def prepend(self, value):
        #create a new node
        new_node = Node(value)
        #if there is no head make head and tail point to new_node
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:#point new_node.next to head and then set head of LL to be new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    #remove the first element and return it
    def pop_first(self):
        #if LL is empty return None
        if self.length == 0:
            return None
        # set temp
        temp = self.head
        #move head up one
        self.head = self.head.next
        #set temp.next to None
        temp.next = None
        self.length -= 1
        #if LL is empty set tail to None
        if self.length == 0:
            self.tail = None
        return temp

    #return a Node at a specific index
    def get(self, index):
        #make sure index is within range
        if index < 0 or index >= self.length:
            return None
        # iterate down the LL index number of times and return node it ends on
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        #use our get method to set the correct node and make sure it isnt None
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    #create new node and insert at given index
    def insert(self, index, value):
        #make sure index is within range
        if index < 0 or index > self.length:
            return False
        #if index == 0 add it to start
        if index == 0:
            return self.prepend(value)
        #add to end 
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    # remove an item at a certain index
    def remove(self, index):
        #make sure it is in bounds
        if index < 0 or index >= self.length:
            return None
        #check edge cases
        if index == self.length-1:
            return self.pop()
        if index == 0:
            return self.pop_first()
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    #reverse the linked list
    def reverse(self):
        #switch head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    #method to check if the LL loops
    def has_loop(self):
        slow = self.head
        fast = self.head.next
        #increment the fast one twice and the slow one once and if they ever meet then there was a loop
        while fast and fast.next:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next
        #if you traverse the whole LL then there is not a loop
        return False
    
    #reverse the LL between 2 indices
    def reverse_between(self, m, n):
    # Return if the list is empty or has one node
        if self.length <= 1:
            return
    
        # Create a dummy node and set it before head
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
    
        # Move prev to the node at index m-1
        for _ in range(m):
            prev = prev.next
    
        # Set current to the node at index m
        current = prev.next
    
        # Reverse the sublist between indices m and n
        for _ in range(n - m):
            # Set temp to the next node to be reversed
            temp = current.next
            # Detach temp and connect current to next node
            current.next = temp.next
            # Place temp at the beginning of the reversed section
            temp.next = prev.next
            # Connect temp to the part before the reversed section
            prev.next = temp
    
        # Update the head of the list if necessary
        self.head = dummy.next
    
    #merge two LL into a sorted LL
    def merge(self, other_list):
        other_head = other_list.head
        dummy = Node(0)
        current = dummy
        c1 = self.head
        c2 = other_head
        while c1 and c2:
            if c1.value < c2.value:
                current.next = c1
                current = current.next
                c1 = c1.next
            else:
                current.next = c2
                current = current.next
                c2 = c2.next
        while c1:
            current.next = c1
            current = current.next
            c1 = c1.next
        while c2:
            current.next = c2
            current = current.next
            c2 = c2.next
        self.head = dummy.next
        self.length += other_list.length
        if self.tail.value < other_list.tail.value:
            self.tail = other_list.tail
        return

#returns the node that is k away from the end
def find_kth_from_end(ll, k):
    #start 2 nodes at beginning
    slow = fast = ll.head
    #move fast node k moves ahead making sure that it never goes past the LL
    for _ in range(k):
        if fast == None:
            return None
        fast = fast.next
    # increment both until the end and return the slow one because it will be k nodes before the fast one
    while fast:
        slow = slow.next
        fast = fast.next
    return slow
        
        

my_linkedlist = LinkedList(4)
my_linkedlist.append(3)
my_linkedlist.prepend(1)
my_linkedlist.print_list()
print("\n")
my_linkedlist.insert(2, 20)
my_linkedlist.remove(2)
my_linkedlist.reverse()
print("\n")
my_linkedlist.print_list()
print("\n")
print(find_kth_from_end(my_linkedlist, 1).value)