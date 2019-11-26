#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        count = 0
        current = self.head  

        if self.head == None:
            return 0
        #While there are still more nodes after the one we are currently on
        count = 1
        while current.next is not None: 
            #Move to the next node, add 1 to the counter 
            current = current.next
            count += 1
        
        
        
        print(count)
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) because there is a reference to the tail and there is
        no looping through anything"""
        #If there are no nodes yet, create one
        if self.head == None:
            new_node = Node(item)
            self.head = new_node
            self.tail = new_node

        elif self.head != None:
            current = self.tail
            #While there are still nodes after the one we are currently on,
            #append the next node to the one we are currently on
            new_node = Node(item)
            current.next = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) because in each case there is only one thing to check 
        and therefore to iterate over"""
        # Create new node to hold given item
        if self.head == None:
            new_node = Node(item)
            self.head = new_node
            self.tail = new_node

        # Prepend node before head, if it exists
        elif self.head != None:
            new_node = Node(item)
            old_head = self.head
            self.head = new_node
            self.head.next = old_head

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) If there is no head, then there is only one
        thing to check and iterate over.
        Worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        #If there are no nodes, return empty
        if self.head == None:
            return NotImplemented

        if self.head != None:
            current = self.head
            # Loop through all nodes
            while current != None:
                # Check if node's data satisfies given quality function
                if (quality(current.data)):
                    return current.data
                current = current.next

    def replace(self, item_replacing, value_replacing):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) If there is no head, then there is only one
        thing to check and iterate over, or if we are replacing the head
        Worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item"""
        #If there are no nodes, return empty
        if self.head == None:
            return NotImplemented

        if self.head != None:
            current = self.head
            # Loop through all nodes
            while current != None:
                # Check if node's data satisfies given quality function
                if current.data == item_replacing:
                    current.data = value_replacing
                    return

                current = current.next

            #If item we want to replace isn't found
            raise ValueError('Item not found: {}'.format(item_replacing))

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) if there is nothing in the linked list or if
        we are deleting the head node
        Worst case running time: O(n) because in the best case scenario, there are
        no nested loops and if statements take constant time"""
        #If there are no nodes
        if self.length() == 0:
            raise ValueError('Item not found: {}'.format(item))
        
        current = self.head
        saved_previous = None

        #Until there are no more nodes after the one we are currently on
        while current != None:
            #If the one we are currently on is the one we are looking for
            if current.data == item:
                if current.next != None:
                    if saved_previous != None:
                        saved_previous.next = current.next
                    elif saved_previous == None:
                        self.head = current.next
                    current.next = None
                    return
                elif current.next == None:
                    if saved_previous != None:
                        saved_previous.next = None
                        self.tail = saved_previous
                    elif saved_previous == None:
                        self.head = None
                        self.tail = None
                    return
            saved_previous = current
            current = current.next
        raise ValueError('Item not found: {}'.format(item))              

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:') 
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

        print('\nTesting prepend:')
    for item in ['A', 'B', 'C']:
        print('prepend({!r})'.format(item))
        ll.prepend(item)
        print('list: {}'.format(ll))

    print('length: {}'.format(ll.length()))

    print(ll.find ('a'))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))

if __name__ == '__main__':
    test_linked_list()
