class BSTree:  # Binary Search Tree

    def __init__(self):
        self.root = None

    def depth(self):
        if self.root == None:
            return 0
        else:
            return self.root.maxDepth()  # use BSNode maxDepth function
    	
    def __str__(self):
        if self.root == None:
            return "EmptyBSTree"
        else:
            return self.root.__str__()

    # insert new values into the tree (move from BSNode to BSTree)
    def insert(self, val):
        if self.root == None:
            self.root = BSNode(val)
        else:
            self._insert(val, self.root)
	
    def _insert(self, newVal, node):
        if newVal < node.value:
            if node.left == None:
                node.left = BSNode(newVal)
            else:
                self._insert(newVal, node.left)
				
        elif newVal > node.value:
            if node.right == None:
                node.right = BSNode(newVal)
            else:
                self._insert(newVal, node.right)
	

    def sort(self):
        if self.root != None:
            return self.root.sort_value() # use BSNode sort_value function
        else:
            return "EmptyBSTree"


class BSNode:  # Binary Search Tree Node

    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

    def __str__(self):
        return self.strIndent('')

    def strIndent(self, ind):
        """Makes text-based print of tree"""
        outputString = ''
        if self.left == None and self.right != None:
            outputString = outputString + ind + ' [none]\n'
        if self.left != None:
            outputString = outputString + self.left.strIndent(ind + ' ')
        outputString = outputString + ind + self.value + '\n'
        if self.right == None and self.left != None:
            outputString = outputString + ind + ' [none]\n'
        if self.right != None:
            outputString = outputString + self.right.strIndent(ind + ' ')
        return outputString


    # maximum depth of the tree
    def maxDepth(self):
        # if both subtrees are empty
        if self.left == None and self.right == None:
            return 1

        # if the left subtree is empty
        elif self.left == None:
            return self.right.maxDepth() + 1

        # if the right subtree is empty
        elif self.right == None:
            return self.left.maxDepth() + 1

        # if neither subtree is empty
        else:
            return max(self.left.maxDepth(), self.right.maxDepth()) + 1

    def sort_value(self):
        sorted_values = []
        if self.left:
            sorted_values.extend(self.left.sort_value())
        sorted_values.append(self.value)
        if self.right:
            sorted_values.extend(self.right.sort_value())
        return sorted_values


def treeSort(alist):
    treeSort= BSTree()
    for item in alist:
        treeSort.insert(item)
    return treeSort.sort()


tree = BSTree()
#tree.root = BSNode(7)
for i in [7, 98, 78, 6, 5, 47, 23]:
    tree.insert(i)
print(tree.sort())
print(tree.depth())
print(treeSort([4,5,7,8,1,2,8]))




