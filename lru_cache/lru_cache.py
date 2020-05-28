import sys

sys.path.append('../doubly_linked_list')

from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.max_nodes = limit
        self.current_nodes = 0

        self.dll = DoublyLinkedList()
        self.dict = {}


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key not in self.dict:
            return None
        
        node = self.dll.head
        while node is not None:
            if key == node.value[0]:
                self.dll.move_to_front(node)
                break

            node = node.next
        
        return self.dict[key]
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, val):
        if key in self.dict:
            # replace old value with NEW value in dict
            self.dict[key] = val
            # replace old value with NEW value in dll
            ## sets node variable to the first value in the dll ----> to iterate from beginning of the list all the way to the end
            node = self.dll.head
            while node is not None:
                # to check if the selected key matches the stored key in the current node
                if key == node.value[0]:
                    # changes the value in the dll
                    node.value[1] = val
                    # moves the current node to the front
                    self.dll.move_to_front(node)
                    # exits out of the while loop
                    break
                # sets the current node to the next node in the dll
                node = node.next
        else:
            # Check if cache is full
            if self.current_nodes == self.max_nodes:
                # sets the last note in the dll as node
                node = self.dll.tail
                # gets the first value of the node variable ------> which is the key for the key value pair in the cache
                old_key = node.value[0]
                self.dll.remove_from_tail
                # deletes the key value pair in the dict using the old_key value
                del self.dict[old_key]
                self.current_nodes -= 1

            # adds key:value pair in the dict
            self.dict[key] = val
            # adds key:value pair in the dll
            self.dll.add_to_head([key, val])
            self.current_nodes += 1





