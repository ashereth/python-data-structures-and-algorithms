class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

#implementation of a stack using a LL
class Stack:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next
    #add to the top of the stack
    def push(self, value):
        new_node = Node(value)
        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
    #pop from top of stack
    def pop(self):
        if not self.top:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp

print('STACK\nbefore popping')
stack = Stack(0)
stack.push(1)
stack.push(2)
stack.print_stack()
print('\n')
print(stack.pop().value)
print('\nafter popping')
stack.print_stack()
print('\n')

#implementation of a queue using a LL
class Queue:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.length = 1
        self.first = new_node
        self.last = new_node
    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next
    def enqueue(self, value):
        new_node = Node(value)
        if not self.first:
            self.first  = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
    def dequeue(self):
        # queue is empty return None
        if not self.first:
            return None
        temp = self.first
        #if the queue has one item set first and last to none
        if self.first == self.last:
            self.first = self.last = None
        else:
            self.first = temp.next
            temp.next = None
        self.length -= 1

        return temp



queue = Queue(1)
queue.dequeue()
queue.enqueue(1)
print('QUEUE\n')
queue.print_queue()
print('\n')

