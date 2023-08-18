class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while (temp):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    #start at top and go down layer by layer
    def breadth_first_search(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

    #depth_first_search pre order
    def dfs_pre_order(self):
        results = []
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
        
        traverse(self.root)
        return results
    
    #depth_first_search in order
    def dfs_in_order(self):
        results = []
        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right:
                traverse(current_node.right)
        
        traverse(self.root)
        return results
    
    #depth_first_search post order
    def dfs_post_order(self):
        results = []
        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
            results.append(current_node.value)
        
        traverse(self.root)
        return results
    
    #function for testing if a tree is a valid BST
    def is_valid_bst(self):
        results = self.dfs_in_order()
        for i in range(len(results)-1):
            if results[i] > results[i+1]:
                return False
        return True
    
    #method for finding the kth smallest Node
    # not the greatest approach because it traverses the whole tree
    def kth_smallest(self, k):
        results = []
        def traverse(node):
            if node.left:
                traverse(node.left)
            results.append(node.value)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        if k>len(results):
            return None
        return results.pop(k-1)


bst = BinarySearchTree()
bst.insert(5)
bst.insert(7)
bst.insert(4)
bst.insert(9)
print('\n','BFS',bst.breadth_first_search(),'\n')
print('\n','DFS pre order',bst.dfs_pre_order(),'\n')
print('\n','DFS in order',bst.dfs_in_order(),'\n')
print('\n','DFS post order',bst.dfs_post_order(),'\n')
print('\n','3rd smallest element =',bst.kth_smallest(3))