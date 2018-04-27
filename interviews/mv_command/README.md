# Given a file/directory structure modeled as a k-ary tree, implement the mv(move) command so that any subtree can be relocated to a target node within the same tree.
CF 401 Data Structures Whiteboard Challenge

Mock Interviews

## Challenge
- Ask the candidate to model the mv command as it’s used on the command line within a file directory.
- Don’t volunteer the the following info, but use it to answer questions, and guide the candidate’s work
    - The command takes 2 arguments: the directory to be moved, followed by the destination folder to move it in to
    - For example: mv ~/projects/301/learn-code-game ~/projects/401
    - Think of this directory structure as modeled as a k-ary tree, where each node is a folder that holds some number of subfolders or files.
    - The candidate does NOT need to write a command line applicaiton!
    - You simply want to see them code up the algorithm for how to move a node from one part of a tree, to another part
    - Input to the function would be 2 node objects: the node to move, and the destination node to attach it to
    - Presume that each node has a property that is a reference back to its parent (otherwise, the candidate would need to search the tree to find the matching node)
    - So, moving a subtree here means:
        - first deleting the reference to the given node from it’s parent’s children array,
        - then attaching the specified node as a child of the destination node
        - finally re-assigning the parent property
- Time Complexity: O(1)
    - Constant time, since it doesn’t matter how many nodes are in the tree, it’s always the same number of steps to relocate one node
- Space Complexity: O(1)
    - No additional space is required, since this is an “in-place” operation

### Original Instructions
https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-29/interview-01.html
