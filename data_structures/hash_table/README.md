## Data Structures
### Hash Tables
- Create a HashTable class, which when instantiated is aware of the following attributes:
    - max_size: defaults to 1024
    - buckets: defaults to a Python list()
        - This list structure should be instantiated with a size of max_size, where each element is a LinkedList
- Define the following methods on your HashTable class:
    - hash_key: which accepts a string argument only, and returns a hashed value representing a single bucket location in your hash table
    - set: which accepts a key and value as arguments. The key will be used to as the hashed location for identifying a bucket. The value will be the actual data stored in the LinkedList as a new Node in that location.
        - Note: This implies that your hash table will handle collisions using separate chaining.
    - get: which accepts a key and returns the value at that given key, using the key as an assumed value within the Node of the Linked List.
    - remove: which accepts a key and removes the given Node from the Linked List at that bucket.
        - You are welcome to modify this removal method to include functionality for removing the complete list, but this is not required.

Write at least three unit tests for each function that you define as part of this assignment.
