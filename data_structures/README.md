# Data Structures and Sorting Algorithms

**Author:** Beverly Pham

## Data Structures

### [Singly Linked-List](./linked-list)

List of values stored in nodes linked to each other in one direction.

A singley linked list is beneficial when creating a to do list. You can remove the items when they are completed without having to alter the entire list. And there is no need to iterate through it from both directions.

#### Constructor:
```python
l = LinkedList(iterable=[])
```
#### Implements the following methods:
- **insert(val):** Add another node to the front of the list.
    - Time complexity: O(1)
- **find(val):** Find the node that has the given value. If present, return True; else return False.
    - Time complexity: O(n)
- **append(val):** Append a node to the end of the linked list.
- **insert_before(val, newVal):** Add a new node with the given newValue immediately before the first value node
- **insert_after(val, newVal):** Add a new node with the given newValue immediately after the first value node
- **kth_from_end(k):** Return the node that is k from the end of the linked list.
- **has_loop()):** Return True if there is a circular reference or loop in the linked list; else return False.
- **len():** Get the size of the LinkedList.
    - Time complexity: O(1)
- **pop():** Remove the first node and return it's value. Raises an IndexError if there are no values to return.
    - Time complexity: O(1)
- **remove(node):** Remove the given node from the LinkedList. Raises a ValueError if the node is not in the list.
    - Time complexity: O(n)
- **display():** Display LinkedList as if it were a tuple literal. Ex: “(12, ‘sam’, 37, ‘tango’)”
    - Time complexity: O(n)


### [Stack](./stack)

Structure for values in a stack where the first item in is the last item out (FILO).

#### Constructor:
```python
s = Stack(iterable=[])
```
#### Implements the following methods:
- **len():** Get the size of the stack.
    - Time complexity: O(1)
- **push(val):** Add another value to the top of the stack. Return the new top value.
    - Time complexity: O(1)
- **pop():** Remove the top node and return it's value. <!-- Raises an IndexError if there are no values to return. -->
    - Time complexity: O(1)
- **peek():** Get the value from the top of the stack without removing it.
    - Time complexity: O(1)


<!-- ### Doubly-Linked-List


List of values stored in nodes linked in two directions.


A doubly linked list is better for keeping a log of information, such as history, this way you can access information from both directions.

#### Constructor:
```python
l = DLL(iterable='list, tuple, or str')
```
#### Implements the following methods:
- **push(val):** Add another value to the front of the list.
    - Time complexity: O(1)
- **pop():** Remove the first node and return it's value. Raises an IndexError if there are no values to return.
    - Time complexity: O(1)
- **remove(val):** Remove the given value from the doubly-linked list. Raises a ValueError if the value is not in the list.
    - Time complexity: O(n)
- **append(val):** Append the value at the tail of the list.
    - Time complexity: O(1)
- **shift():** Remove the last value from the tail of the list and return it. Raises an IndexError if there are no values to return
    - Time complexity: O(1) -->

### [Queue](./queue)

Structure for values in a queue where the first item in is the first out (FIFO).

#### Constructor:
```python
q = Queue(iterable=[])
```
#### Implements the following methods:
- **len():** Get the size of the queue.
    - Time complexity: O(1)
- **enqueue(value):** Add a value to the back of the queue.
    - Time complexity: O(1)
- **dequeue():** Remove the value from the front of the queue and return it. <!-- Raises an IndexError if there are no values to return. -->
    - Time complexity: O(1)
<!-- - **peek():** Get the value from the front of the queue without removing it.
    - Time complexity: O(1) -->

<!-- ### Deque

Structure for values in a deque, double-ended queue.

#### Constructor:
```python
d = Deque(iterable='list, tuple, or str')
```
#### Implements the following methods:
- **append(value):** Add a value to the end of the deque.
    - Time complexity: O(1)
- **appendleft(value):** Add a value to the front of the deque.
    - Time complexity: O(1)
- **pop():** Remove the value from the end of the deque and return it. Raises an IndexError if there are no values to return.
    - Time complexity: O(1)
- **popleft():** Remove the value from the front of the deque and return it. Raises an IndexError if there are no values to return.
    - Time complexity: O(1)
- **peek():** Get the value from the end of the deque without removing it.
    - Time complexity: O(1)
- **peekleft():** Get the value from the front of the deque without removing it.
    - Time complexity: O(1)
- **size():** Get the size of the deque.
    - Time complexity: O(1) -->

<!-- ### Binary Heap

Structure for values in a Binary Heap. A max binary heap is a complete binary tree where each level of the tree is greater than the level below it. A min heap has the lowest values at the top.

#### Constructor:
```python
h = BinHeap(iterable='list, tuple, or str', is_max_heap=True)
```
#### Implements the following methods:
- **push(val):** Put a new value into the binary heap.
    - Time complexity: O(log(n))
- **pop():** Remove the value from the top of the heap and return it. Raises an IndexError if there are no values to return.
    - Time complexity: O(log(n)) -->

<!-- ##3 Priority Queue

Structure for values in a priorty queue. Items added to the priority queue are given a priority. If not set by the user, priority is set to be the lowest. When removing items, higher priority items are removed before lower priority items.

#### Constructor:
```python
q = PriorityQ()
```
#### Implements the following methods:
- **insert(value, priority=None):** Put a new value into the priority queue. If no priority is given, it is set to be the current minimum priority.
    - Time complexity: O(n)
- **pop():** Remove the highest priority value from the priority queue and return it. Raises an IndexError if there are no values to return.
    - Time complexity: O(log(n))
- **peek():** Get the highest priority value from the priority queue and without removing it. Returns None if these are no values to return.
    - Time complexity: O(1) -->

<!-- ### Graph_1

Structure for values in a graph, which is directed and unweighted. Nodes added to graph have a value. Nodes connected to each other by a pointer are edges. Graph contains edges and nodes. Nodes are unique.

#### Constructor:
```python
g = Graph()
```
#### Implements the following methods:
- **nodes():** Get all nodes in the graph and display them as a list.
    - Time complexity: O(1)
- **edges():** Get all edges in the graph and display them as a list.
    - Time complexity: O(1)
- **add_node(val):** Add a node with a value to the graph.
    - Time complexity: O(1)
- **add_edge(val1, val2):** Add an edge with nodes to the graph.
    - Time complexity: O(1)
- **del_node(val):** Remove the node with the given value from the graph. Also removes all edges connected to the node. Raises an ValueError if the value is not in the graph.
    - Time complexity: O(n<sup>2</sup>)
- **del_edge(val1, val2):** Remove the edge connecting node of val1 to node of val2. Raises an ValueError if the edge is not in the graph.
    - Time complexity: O(1)
- **has_node(val):** Check if the given value is in the graph.
    - Time complexity: O(1)
- **neighbors(val):** Get a list of all nodes the node of the given value connects to. Raises an ValueError if the value is not in the graph.
    - Time complexity: O(n<sup>2</sup>)
- **adjacent(val1, val2):** Check if there is an edge connecting the nodes with given values.
    - Time complexity: O(1)
- **def breadth_first_traversal(start_val):** Get the full visited path of a breadth first traversal. Raises an ValueError if the value is not in the graph.
    - Time complexity: O(n<sup>4</sup>)
- **def depth_first_traversal(start_val):** Get the full visited path of a depth first traversal. Raises an ValueError if the value is not in the graph.
    - Time complexity: O(2<sup>n<sup>2</sup></sup>) -->

<!-- ### Weighted-Graph (weight_graph)

Structure for values in a graph, which is directed and weighted. Nodes added to graph have a value. Nodes connected to each other by a pointer are edges and each edge has a weighted value. Graph contains edges and nodes. Nodes are unique.

#### Constructor:
```python
g = Graph()
```
#### Implements the following methods:
- **nodes():** Get all nodes in the graph and display them as a list.
    - Time complexity: O(n)
- **edges():** Get all edges in the graph and display them as a list.
    - Time complexity: O(n<sup>2</sup>)
- **add_node(val):** Add a node with a value to the graph.
    - Time complexity: O(1)
- **add_edge(val1, val2, weight):** Add an edge with nodes and weight to the graph.
    - Time complexity: O(1)
- **del_node(val):** Remove the node with the given value from the graph. Also removes all edges connected to the node. Raises an ValueError if the value is not in the graph.
    - Time complexity: O(n)
- **del_edge(val1, val2):** Remove the edge connecting node of val1 to node of val2. Raises an ValueError if the edge is not in the graph.
    - Time complexity: O(1)
- **has_node(val):** Check if the given value is in the graph.
    - Time complexity: O(1)
- **neighbors(val):** Get a list of all nodes the node of the given value connects to. Raises an ValueError if the value is not in the graph.
    - Time complexity: O(n)
- **adjacent(val1, val2):** Check if there is an edge connecting the nodes with given values.
    - Time complexity: O(1)
- **def breadth_first_traversal(start_val):** Get the full visited path of a breadth first traversal. Raises an ValueError if the value is not in the graph.
    - Time complexity: O(n<sup>2</sup>)
- **def depth_first_traversal(start_val):** Get the full visited path of a depth first traversal. Raises an ValueError if the value is not in the graph.
    - Time complexity: O(n<sup>2</sup>)
- **def dijkstra_min(start, end):** Find the shortest path from start to end using Dijkstra's algorithm. Raises value error if node not in graph or start and end do not connect.
    - Time complexity: O(n<sup>2</sup>)
- **def bellman_ford_min(start, end):** Find the shortest path from start to end using the Bellman-Ford algorithm. Raises value error if node not in graph or start and end do not connect.
    - Time complexity: O(n<sup>2</sup>) -->

<!-- ### Binary Search Tree

Structure for values in a Binary Search Tree. Each node has a maximum of two children, where the the left child is 'less' than the parent and the right child is 'greater' than the parent. Duplicate values cannot be added to the tree.

#### Constructor:
```python
t = BST(iterable='list, tuple, or str')
```
#### Implements the following methods:
- **insert(val):** Insert a new value into the Binary Search Tree. Duplicate values are ignored when inserted into the tree.
    - Time complexity: O(n)
- **delete(val):** Delete the given value from the tree. Does nothing if the value is not in the tree.
    - Time complexity: O(n)
- **search(val):** Find the node that contains the given value. Returns None if value is not in the tree.
    - Time complexity: O(n)
- **contains(val):** Check if a value is in the Binary Search Tree.
    - Time complexity: O(n)
- **size():** Get the size of the Binary Search Tree.
    - Time complexity: O(1)
- **depth():** Get the maximum depth of the Binary Search Tree. The depth is the number of levels in the tree. A tree with only one value has a depth of zero.
    - Time complexity: O(1)
- **balance():** Get the balance of the Binary Search Tree. Tree that is deeper on the left than right has positive balance. Tree that is deeper on the right than left has negative balance. Tree that is balanced, with the same depth on left and right, has a balance of zero.
    - Time complexity: O(1)
- **in_order():** Get an in-order traversal generator of the tree. In-order gets values from the tree by traversing the left branch, root, then right branch.
    - Time complexity: O(n)
- **pre_order():** Get an pre-order traversal generator of the tree. Pre-order gets values from the tree by traversing the root, left branch, then right branch.
    - Time complexity: O(n)
- **post_order():** Get an post-order traversal generator of the tree.  Post-order gets values from the tree by traversing the left branch, right branch, then root.
    - Time complexity: O(n)
- **breadth_first():** Get an breadth-first traversal generator of the tree. Breadth-first gets values from the tree by stepping down through the layers of the tree.
    - Time complexity: O(n) -->

<!-- ### Self-Balancing Binary Search Tree

Structure for values in a Self-Balancing Binary Search Tree. Each node has a maximum of two children, where the the left child is 'less' than the parent and the right child is 'greater' than the parent. Duplicate values cannot be added to the tree. Each time an item is added or removed from the tree, it is rebalanced such that the |balance| is no more than 1 at every node.

#### Constructor:
```python
b = BalanceBST(iterable='list, tuple, or str')
```
#### Implements the following methods:
- **insert(val):** Insert a new value into the Binary Search Tree. Duplicate values are ignored when inserted into the tree.
    - Time complexity: O(n)
- **delete(val):** Delete the given value from the tree. Does nothing if the value is not in the tree.
    - Time complexity: O(n)
- **search(val):** Find the node that contains the given value. Returns None if value is not in the tree.
    - Time complexity: O(log(n))
- **contains(val):** Check if a value is in the Binary Search Tree.
    - Time complexity: O(log(n))
- **size():** Get the size of the Binary Search Tree.
    - Time complexity: O(1)
- **depth():** Get the maximum depth of the Binary Search Tree. The depth is the number of levels in the tree. A tree with only one value has a depth of zero.
    - Time complexity: O(1)
- **balance():** Get the balance of the Binary Search Tree. Tree that is deeper on the left than right has positive balance. Tree that is deeper on the right than left has negative balance. Tree that is balanced, with the same depth on left and right, has a balance of zero.
    - Time complexity: O(1)
- **in_order():** Get an in-order traversal generator of the tree. In-order gets values from the tree by traversing the left branch, root, then right branch.
    - Time complexity: O(n)
- **pre_order():** Get an pre-order traversal generator of the tree. Pre-order gets values from the tree by traversing the root, left branch, then right branch.
    - Time complexity: O(n)
- **post_order():** Get an post-order traversal generator of the tree.  Post-order gets values from the tree by traversing the left branch, right branch, then root.
    - Time complexity: O(n)
- **breadth_first():** Get an breadth-first traversal generator of the tree. Breadth-first gets values from the tree by stepping down through the layers of the tree.
    - Time complexity: O(n) -->

<!-- ### Hash Table

Structure for items in a hash table. A hash table stored values under keys. It hashes the key using the hashing function to get a number and stores the value under that number, making for easy retrieval.

#### Constructor:
```python
h = HashTable(size, hashing)
```
#### Implements the following methods:
- **set(key):** Set the value to the key in the hash table. Adds the key if it is not in the table. Replaces the value if it is already in the table. Raises a TypeError for non-string keys.
    - Time complexity: O(k) - where k is the number of collisions for the hash value
- **get(key):** Get the value stored with the given key. Raises a TypeError for non-string keys. Raises KeyError for a key not in the hash table.
    - Time complexity: O(k) - where k is the number of collisions for the hash value

#### Available functions in the module:
- **additive_hash(value):** Get the hash value by adding up the ASCII values of the characters in a string. Raises a TypeError for a non-string value.
- **fnv_hash(value, offset=2166136261, prime=16777619):** Get the hash value using the Fowler-Noll-Vo method. Default is the 32-bit version. The initial hash value is the FNV offset basis. For each byte in the input, the hash is multiplied by the FNV prime, then XOR with the byte from the input. Raises a TypeError for a non-string value. -->

<!-- ### Trie Tree

Structure for values in a Trie tree. Stores strings as individual character nodes. Each string starts with a '*' node and ends with a '$' node. Only characters that are not in the tree in the string order are added to the tree. When characters different from those already in the tree are added, a new branch is added at the node where the difference occurs.

#### Constructor:
```python
t = Trie(iterable='list or tuple')
```
#### Implements the following methods:
- **insert(string):** Insert the given string into the Trie tree. Duplicate characters are ignored. Raises a TypeError if given a non-string value.
    - Time complexity: O(k) - where k is the length of the string
- **contains(string):** Check if the given string is in the Trie tree. Raises a TypeError if given a non-string value.
    - Time complexity: O(k) - where k is the length of the string
- **size():** Get the number of words in the Trie tree.
    - Time complexity: O(1)
- **remove(string):** Remove the given string from the Trie tree. Raises a TypeError if given a non-string value. Raises a ValueError if the string is not in the tree.
    - Time complexity: O(k) - where k is the length of the string
- **traversal(start):** Get an depth-first traversal generator of the Trie tree. Starting traversal from an empty string returns a traversal of the entire Trie tree. Starting with a non-empty string will yield only the children as individual letters. Raises a TypeError if given a non-string value.
    - Time complexity: O(n) -->

<!-- ## Sorting Algorithms
All sorting algorithms will sort a list of comparable items in ascending order.

Each module can be run from the command line for a synopsis of the efficiency of the algorithm in best, average, and worst case scenarios of varying lengths.
```bash
$ cd data-structures/src/sorting_algorithms
sorting_algorithms $ python (algorithm to run).py
```

### Bubble Sort

Repeatedly iterates through the list swapping adjacent values if they are not in the correct order. Continues looping until the list is sorted.
 - **Time complexity:** O(n<sup>2</sup>)

[![Bubble Sort](https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif)](https://en.wikipedia.org/wiki/Bubble_sort)

### Insertion Sort

Iterates forward through the list moving each value into place by checking it against the values before it.
 - **Time complexity:** O(n<sup>2</sup>)

[![Insertion Sort](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)](https://en.wikipedia.org/wiki/Insertion_sort)

### Merge Sort

Halve a list repeatedly into the smallest possible pieces, then sort them. Compare each pair of pieces to each other one element at a time, merging them into a larger, sorted piece. Completed when both halves of the list are merged back together.
 - **Time complexity:** O(nlog(n))

[![Merge Sort](https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif)](https://en.wikipedia.org/wiki/Merge_sort)

### Quick Sort

Partition a list into two pieces repeatedly by selecting a pivot value and rearranging the elements such that all values less than the pivot are before it and those greater are after. Each partition is partitioned until the list is completely sorted.
 - **Time complexity:** O(nlog(n))

[![Quick Sort](https://upload.wikimedia.org/wikipedia/commons/9/9c/Quicksort-example.gif)](https://en.wikipedia.org/wiki/Quicksort)

## Resources

- **Wikipedia:** [Binary Heap](https://en.wikipedia.org/wiki/Binary_heap)
- **GeeksForGeeks:** [Bellman-Ford](http://www.geeksforgeeks.org/dynamic-programming-set-23-bellman-ford-algorithm/)
- **YouTube:** [Dijkstra's algorithm](https://www.youtube.com/watch?v=5GT5hYzjNoo)
- **Eternally Confuzzled:** [List of hashing functions](http://www.eternallyconfuzzled.com/tuts/algorithms/jsw_tut_hashing.aspx) -->
