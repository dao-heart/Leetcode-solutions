# Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

## Test the nodes
n1 = Node("Mon")
n2 = Node("Tues")
n1.next = n2
print(n1)

class LinkedList:
    print_list = []
    def __init__(self):
        self.headval = None

    def __repr__(self):
        return "->".join(self.helperFunction(self.headval))

    # IMPROV: Using generator instead of iterator.
    # Recursive traversal and print linked list - O(n)
    def helperFunction(self,node):
        if node:
            self.print_list.append(node.data)
            self.helperFunction(node.next)
        return self.print_list

    # Insert at the front of the linked List - O(1)
    def insertNodeStart(self,data):
        NewNode = Node(data)
        NewNode.next = self.headval
        self.headval = NewNode
    # Insert at the end of the linked list - O(n) transverse using while loop
    def insertNodeEnd(self, data):
        node = self.headval
        NewNode = Node(data)
        if node is None:
            node = NewNode

        while node.next is not None:
            node = node.next
        node.next = NewNode
    # Insert at the middle of the list - O(1) traverse and swap pointers
    def insertNodeMiddle(self, middle_node, new_data):
        if middle_node is None:
            print("The mentioned node is empty")
            return
        NewNode = Node(new_data)
        NewNode.next = middle_node.next
        middle_node.next = NewNode
    # Delete the selected node. Need to traverse the list - O(n)
    def removeNode(self, delete_node):
        node = self.headval
        target_node = self.delete_node(node,delete_node)
        target_node.next = delete_node.next
        delete_node = None
    def del_helper_function(self, node, delete_node):
        if node.next is delete_node:
            retun node
        else:
            self.del_helper_function(node.next, delete_node)





#### Create a Linked List

l1 = LinkedList()
l1.headval = Node("Mon")
l2 = Node("Tues")
l1.headval.next = l2
l2.next = Node("Wed")
l1.insertNodeStart("Sun")
l1.insertNodeEnd("Fri")
l1.insertNodeMiddle(l2.next, "Thu")
print(l1)
