class Node:
    def __init__(self, value) -> None:
        self.value = value
        #nodes for a BST have left and right nodes
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        #create a pointer to keep track of the first node
        self.root = None
    #insert a new node into the tree
    def insert(self, value) -> bool:
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        #loop down the tree comparing values of current nodes with new_node
        while (True):
            #if the values are equal return false
            if new_node.value == temp.value:
                return False
            #if new_node is less than go left
            if new_node.value < temp.value:
                #if there is nothing to the left set left to new_node
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            #if new_node is greater than go right
            else:
                #if there is nothing to the right set right to new_node
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    #search for a number in the tree
    def contains(self, value):
        #if tree is empty return false
        if self.root == None:
            return False
        temp = self.root
        #loop down tree
        while temp:
            #if value less than current node go left
            if value < temp.value:
                temp = temp.left
            #if cvalue greater than current node go right
            elif value > temp.value:
                temp = temp.right
            #if value equal current node return true
            else:
                return True
        #return false if traversed the whole tree 
        return False
    #find maximum depth of the tree using recursive depth first search
    def max_depth(self, root):
        #base case there is no node for subtree so its length is 0
        if not root:
            return 0
        #if there is a root for subtree then depth is 1 plus maxdepth of
        # its subtrees, each time it recurses it adds one 
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))

print("\n")
tree = BinarySearchTree()
tree.insert(1)
tree.insert(0)
tree.insert(2)
tree.insert(3)
if tree.contains(3):
    print("yes")
    print(tree.max_depth(tree.root))
print("\n")