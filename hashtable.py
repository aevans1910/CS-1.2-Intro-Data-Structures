#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size of 8"""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.length_of_hashtable = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(n) because n is the size of the buckets aray and we just
        have to loop over them"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for my_key, my_value in bucket.items():
                all_keys.append(my_key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n) because n is the size of the buckets aray and we just
        have to loop over them"""
        all_values = []
        # Loop through all buckets
        for bucket in self.buckets:
            # Collect all values in each bucket
            for my_key, my_value in bucket.items():
                all_values.append(my_value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(n) because n is the size of the buckets aray and we just
        have to loop over them"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: because n is the size of the buckets aray and we just
        have to loop over them"""
        count = 0
        # Loop through all buckets
        for bucket in self.buckets:
            # Count number of key-value entries in each bucket
            for key, value in bucket.items():
                count += 1
        return count

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: because n is the size of the buckets aray and we just
        have to loop over them"""

        return self.length_of_hashtable

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: O(1) because we just need to check and see if a node 
        already exists in the bucket, it is therefore constant time"""
        # Find bucket where given key belongs
        bucket = self.buckets[self._bucket_index(key)]
        
        if bucket != None:
            for my_key, my_value in bucket.items():
                # Check if key-value entry exists in bucket
                if my_key == key:
                    return True
            return False
                
    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: O(1) because we only need to find and get the value of a given
        key, it therefore runs on constant time"""
        # Find bucket where given key belongs
        bucket = self.buckets[self._bucket_index(key)]

        for my_key, my_value in bucket.items():
            # Check if key-value entry exists in bucket
            if my_key == key:
                # If found, return value associated with given key
                return my_value
        # Otherwise, raise error to tell user get failed
        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: O(1) because we only need to find and then replace a
        given key, this therefore runs on constant time"""
        # Find bucket where given key belongs
        bucket = self.buckets[self._bucket_index(key)]

        if self.contains(key):
            for my_key, my_value in bucket.items():
                # Check if key-value entry exists in bucket
                if my_key == key:
                     # If found, update value associated with given key
                    bucket.delete((my_key, my_value))
                    bucket.append((key, value))
        # Otherwise, insert given key-value entry into bucket
        else: 
            bucket.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Running time: O(1) because we only need to find the given node and
        delete it, it therefore runs on constant time"""
        # Find bucket where given key belongs
        bucket = self.buckets[self._bucket_index(key)]

        if self.contains(key):
            for my_key, my_value in bucket.items():
                # Check if key-value entry exists in bucket
                if my_key == key:
                    # If found, delete entry associated with given key
                    bucket.delete((my_key, my_value))
        # Otherwise, raise error to tell user delete failed
        else:
            raise KeyError('Key not found: {}'.format(key))
    
    

def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))
    

if __name__ == '__main__':
    test_hash_table()
