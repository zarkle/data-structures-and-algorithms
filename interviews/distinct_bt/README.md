# Find distinct values in a binary tree
CF 401 Data Structures Whiteboard Challenge

Mock Interviews

## Challenge
- Actual code is required for a complete answer
- Avoid utilizing any of the built-in methods available in your language. Standard- library data structures are acceptable.
- Ask the candidate to write a function to list out the distinct values in a given binary tree.
- This problem can be approached in several ways:
    - At each node, compare against all other nodes
        - Traverse to each node in the tree, and search the entire tree to see if the current value is repeated at any other node.
        - If no other node with the same value is found, store the current node value in a results list.
        - This solution takes O(n2) time (since it visits every node, and might look at every other node at each visit) and uses O(1) extra space (since it does not rely on any other data structures.
    - Use a hash to record values seen.
        - While traversing the whole tree, bring along a hashtable.
        - At each node, check to see if the value is already a key in the hashtable.
            - If it is, increment the value at that key (count occurances).
            - If it is not, set a value of 1 with a key of the node’s value.
        - When done traversing the whole tree, iterate through the hash values and remove any key-value pair that has a value higher than 1.
        - This solution takes O(n) time (since it traverses the tree once, and the hashtable once: O(2n)) and uses O(n) space for the hashtable.
- Be sure the candidate explains the Big O of their solution, and justifies their answer.

### Original Instructions
https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-44/interview-01.html
