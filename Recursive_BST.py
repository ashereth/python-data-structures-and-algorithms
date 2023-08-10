#Binary Search Tree using recursive methods
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
    #implimentation of recursive insert (wont be called directly)
    def __r_insert(self, current_node, value):
        #if we reached the end of the tree create a new node and return it
        if current_node == None:
            return Node(value)
        #based on current node value set the left or right nodes using this function
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        #if the current node value is equal to value just return the node
        return current_node

    #function that calls recursive insert
    def r_insert(self, value):
        #check if BST is empty and if so set the root
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    #implimentation of recursive contains (wont be called directly)
    def __r_contains(self, current_node, value):
        #base case node is None
        if current_node == None:
            return False
        #other base case the values match
        if value == current_node.value:
            return True
        #if value is less than current value call function on left node
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        #if value is greater than current value call function on right node
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        
    #this is the function that will be called and it calls the __r_contains funtion starting at the root
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    
    #implimentation of recursive delete (wont be called directly)
    def __delete_node(self, current_node, value):
        if current_node == None:
            return None
        #if value less than or greater than current value walk down tree
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        # if value is equal to current value
        else:
            #if node is a leaf node
            if current_node.left == None and current_node.right == None:
                #set current node to left by returning none
                return None
            #if there is a right node but not a left node replace current node with right node
            elif current_node.left == None:
                current_node = current_node.right
            #if there is a left node but not a left node replace current node with left node
            elif current_node.right == None:
                current_node = current_node.left
            else:
                #get the minimum value of the right subtree and set current value 
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                #call delete method on right subtree using subtree minimum
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node
    
    #this is the function that will be called and it calls the __delete_node funtion starting at the root
    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)

    #helper method used by delete node to find the minimum node below a certain node
    def min_value(self, current_node):
        # if there is a left node call this function on it
        if current_node.left is not None:
            return self.min_value(current_node.left)
        #if there isnt a left node return the current value
        return current_node.value

    
print('\n')
bns = BinarySearchTree()
bns.r_insert(4)
bns.r_insert(5)
bns.r_insert(2)
bns.delete_node(2)
print(bns.min_value(bns.root))
if bns.r_contains(5):
    print('yes')
print('\n')