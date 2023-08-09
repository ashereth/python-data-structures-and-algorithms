class MaxHeap:
    def __init__(self) -> None:
        #initialize with an empty list to store the heap
        self.heap = []

    #returns the index of the left child of an index
    def _left_child(self, index):
        return 2 * index +1

    #returns the index of the right child
    def _right_child(self, index):
        return 2 * index + 2
    
    #returns the index of the parent
    def _parent(self, index):
        return (index -1) // 2
    
    #swaps the values at 2 indexs
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    
    #helper method for remove
    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap) and 
                    self.heap[left_index] > self.heap[max_index]):
                max_index = left_index

            if (right_index < len(self.heap) and 
                    self.heap[right_index] > self.heap[max_index]):
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
        
    #insert a value into the heap
    def insert(self, value):
        self.heap.append(value)
        #keep track of current index
        current = len(self.heap) - 1
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            #swap current and its parent and change current index
            self._swap(current, self._parent(current))
            current = self._parent(current)
    
    #remove top item from heap
    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        #get the top value of the heap
        max_value = self.heap[0]
        #swap the first and last element and them remove the last element
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_value
#given an array of nums and an integer k return the kth smallest
# number within the array 
def find_kth_smallest(nums, k):
    heap = MaxHeap()
    #add all the nums to the heap
    for num in nums:
        heap.insert(num)
    #while the size of the heap is greater than k
    # keep removing elements 
    while len(heap.heap) > k:
        heap.remove()
    #return the item that is left on top of the heap
    return heap.remove()


    
print('\n')
heap = MaxHeap()
heap.insert(5)
heap.insert(50)
heap.insert(23)
heap.insert(26)
heap.remove()
print(heap.heap)
print('\n')