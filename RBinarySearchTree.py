class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class RBinarySearchTree:
    def __init__(self):
        self.root = None


    def __r_insert(self, current_node, value):
        if current_node == None: 
            return Node(value)   
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value) 
        return current_node    
 

    def r_insert(self, value):
        if self.root == None: 
            self.root = Node(value)
        self.__r_insert(self.root, value)  


    def __r_contains(self, current_node, value):
        if current_node == None: 
            return False      
        if value == current_node.value:
            return True 
        if value < current_node.value:
            return self.__r_contains(current_node.left, value) 
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
 
 
    def r_contains(self, value):

        return self.__r_contains(self.root, value)


    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value


    def __r_delete_node(self, current_node, value):
        if current_node == None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node


    def r_delete_node(self, value):
        self.root = self.__r_delete_node(self.root, value)


    def BFS(self):
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
    

    def DFSPreorder(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results


    def DFSPostOrder(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)
        return results


    def DFSInOrder(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results


    def is_valid_bst(self):
        mylist = self.dfs_in_order()
        return all(mylist[i] <= mylist[i+1] for i in range(len(mylist) - 1))



    def getTargetCopy(self, original, cloned, target):

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
            if current_node.value == target.value:
                return current_node
            
            return None

        return traverse(cloned)
    

tree = RBinarySearchTree()

tree.r_insert(7)
tree.r_insert(4)
tree.r_insert(3)
tree.r_insert(6)
tree.r_insert(19)