# Buggy - Solve it
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
    # def __repr__(self):
    #     return "Value of Node is {}".format(self.data)

class Double_LL:

    def __init__(self):
        self.headval = None
    # Add the Node in the front of the list
    def push(self, data):
        NewNode = Node(data)
        if self.headval is not None:
            self.headval.prev = NewNode
            NewNode.next = self.headval
        self.headval = NewNode

    # Print the list -> (Need traversal)
    def print_list(self):
        node = self.headval
        self.helperFunction(node)

    # IMPROV: Using generator instead of iterator.
    # Recursive traversal and print linked list - O(n)
    def helperFunction(self,node):
        if node is not None:
            print(node.data)
            self.helperFunction(node.next)


    def insertAfter(self, prev_node,new_data):
        NewNode = Node(new_data)
        if prev_node is None:
            print("This node doesn't exist in DLL")
            return
        NewNode.next = prev_node.next
        prev_node.next = NewNode
        NewNode.prev = prev_node
        if prev_node.next is not None:
            prev_node.next.prev = NewNode
    def append(self, new_data):
        NewNode = Node(new_data)
        if NewNode is None:
            return
        node = self.headval
        while node.next:
            # print(node.data)
            node = node.next
        node.next = NewNode
        NewNode.prev = node

dllist = Double_LL()
dllist.push(12)
dllist.push(62)
dllist.append(9)
dllist.push(8)
dllist.push(62)
dllist.append(45)
dllist.print_list()







# print(dir(Node))
