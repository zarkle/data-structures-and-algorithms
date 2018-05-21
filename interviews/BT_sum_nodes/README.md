# Estimate water usage for a given sprinkler system
CF 401 Data Structures Whiteboard Challenge

Mock Interviews

## Challenge
- Actual code is required for a complete answer
- Avoid utilizing any of the built-in methods available in your language.
- Ask the candidate to write a function to calculate the water usage for a sprinkler system schematic provided.
    - The sprinkler system is made of an inlet and a number of connected sprinkler heads that spray water.
    - Each single spinkler head has a T connection that can be connected to 0, 1, or 2 other sprinklers.
    - There are no connected loops in the system. That is, any given sprinkler head is connected to one other spinkler where water comes from (or the inlet), and potentially some downstream heads.
    - Each sprinkler head is configured for a certain amount of output, each potentially different, in millileters per minute.
    - Distance between sprinkler heads is irrelevant.
    - The function should be able to start at any given sprinkler, and return the water used from that point on in the system.
- Start by directing the candidate to decide in what flexible format they want the schematic to be provided.
    - What data sctructure best models the described system?
        - The best representation is a binary tree, where the first sprinkler fed from the inlet is the root.
        - Each node `value` is the water output that sprinkler head is configured for.
        - Note: This is NOT a BST (so higher/lower values can be anywhere), and there is no guarantee that the tree will be balanced.
- Then the candidate should write a function that recieves a binary tree, and figures out the total about of output of the system.
    - This means summing the node values across the whole tree
- This problem can be approached in several ways:
    - Every node needs to be visited to add them all up.
    - This means the whole tree needs to be traversed.
        - So any solution for `n` nodes should require `O(n)` time and use `O(1)` extra space.
    - The candidate may choose breath-first traversal
        - This can take more code to implement
    - The preferred solution is a recursive depth-first traversal
        - At each node, return the output for the node you are on, added to the total usage for each child node.
        - The code becomes very expressive:
            - `total = value + totalUsage(leftChild) + totalUsage(rightChild)`

### Example
| Input `(value, leftBranch, rightBranch)` | Output: total usage |
|--|--|
| `(35, (41, (33,,), (52,,) ), (59, (30, ,), (44, ,)))` | `294`|

### Original Instructions
https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-43/interview-01.html

