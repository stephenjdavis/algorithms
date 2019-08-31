# A Node is an item in a linked list. The node simply contains data (what the item actually is) and references 
# to the relative previous and next nodes.
class Node:
    def __init__(self, data): 
        # Value of the node.
        self.data = data 
        # Next node reference
        self.next = None
        # Pevious node reference.
        self.prev = None
        return

# The head property is a reference to the first node in the list, the tail property is a reference to the last node 
# in the list. The list has no "previous" or "next" pointer properties.
class LinkedList:
    def __init__(self):
        # Beginning of the list.
        self.head = None
        # End of the list.
        self.tail = None
        return

    def push(self, node):
        '''Adds a single node to the end of the list. It's all about setting or updating reference values.
        NOTE: 
        If this is the only node in the list, all we are setting are the list's .head and .tail properties.
        We don't change the node's .prev or .next from None, because they should still be None.

        When adding to a list that already contains nodes, there are three properties in total that need to be updated 
        with new values, 
        1.) The current tail node's .next property... Currently equal to None --> Set it to our new node. 
        (Because our new node will be the current node's .next)
        2.) The new node's .prev property... Currently equal to None. --> Set to the current tail node. 
        (Because the current tail will be our new node's .prev)
        3.) The list's .tail property... Currently equal to the current tail node. --> Set to the new node.'''
        # Create node object.
        node = Node(node)

        # If this list is empty, this node passed as the argument will be set as the first node.
        if self.head == None:
            self.head = node

        # If the list is not empty, the node is added as the last node...
        else:
            # Set the current tail node's .next property value (currently None) to the new node.
            # NOTE: Keep in mind this is not the list's property, this is the current tail node's property.
            self.tail.next = node 
            # Set the new node's .prev property to the current tail node.
            node.prev = self.tail
        
        # Now we can update the tail as the new node.
        self.tail = node
            
        return

    def get_count(self):
        '''The total number of nodes in the list'''
        # We start at the first node...
        linked_node = self.head
        # ... and a counter variable.
        count = 0

        # While the node still has a next value other than None, 
        # we continue resetting the position varable to the next node
        # and add 1 to the counter.
        while (linked_node):
            count += 1
            linked_node = linked_node.next
        return count

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.push('nailed')
    linked_list.push(100)
    linked_list.push('100%')
    linked_list.push('it')
    print('Node count: ', linked_list.get_count())
    print(linked_list.head.data, linked_list.tail.data)
    print(linked_list.tail.prev.data)

 
