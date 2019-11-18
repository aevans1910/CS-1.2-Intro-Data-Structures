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
        #Loop through all nodes and count one for each
        count = 0
        current = self.head  

        while current.next is not None:  
            current = current.next
            count += 1
        
        print(count)
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        # Create new node to hold given item
        # Append node after tail, if it exists
        if self.head == None:
            new_node = Node(item)
            self.head = new_node

        if self.head != None:
            current = self.head  
            while current.next is not None:  
                current = current.next
            new_node = Node(item)
            current.next = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) because in each case there is only one thing to check 
        and therefore to iterate over"""
        # Create new node to hold given item
        # Prepend node before head, if it exists
        if self.head == None:
            new_node = Node(item)
            self.head = new_node

        if self.head != None:
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
        # Loop through all nodes to find item where quality(item) is True
        # Check if node's data satisfies given quality function
        if self.head == None:
            return NotImplemented

        if self.head != None:
            current = self.head
            while current.next != None:
                if (current.data == quality):
                    return current.data
                current = current.next

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        current = self.head
        saved_previous = None

        while current.next != None:
            if current.data == item:
                if saved_previous == None:
                    self.head = current.next

                    if current.next == None:
                        self.tail = saved_previous

                elif current.next == None:
                    saved_previous.next = None
                    self.tail = saved_previous

                else:
                    saved_previous.next = current.next

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
