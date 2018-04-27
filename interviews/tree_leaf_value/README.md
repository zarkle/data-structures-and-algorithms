# Tree has a specific leaf value?
CF 401 Data Structures Whiteboard Challenge

Mock Interviews

## Challenge
- Identify if any leaf node in a k-ary tree matches the given input value
- The candidate should use a depth first search, to get to the leaf nodes faster than BFS algorithm would allow
- Encourage the candidate to think through which kind of DFS would be the most practical (hopefully, they’ll use pre-order traversal, but dont give too much of a hint)
- The candidate should write a function that accepts a k-ary tree object, and a target value to search for
- If the tree contains a node that is a leaf node, and that nodes value matches the target value, then the function can simply return true and be done
- Stretch Goals:
    - Return a list of all leaf nodes in the tree that match the target value.
    - Delete all nodes in the tree that match the target value, and are leaf nodes.

### Original Instructions
https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-29/interview-02.html
