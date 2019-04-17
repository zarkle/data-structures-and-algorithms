# Nearest Value in a Binary Seach Tree
CF 401 Data Structures Whiteboard Challenge

Mock Interviews

## Challenge
Describe to the candidate the following problem:
--
You are working on a team producing estimates of population for some creature, given a complex set of inputs.
Your team keeps records of the simulation runs you've done and their results.

For each new simulation, you are asked to find the previous run with a value nearest to the current result so that you can compare the inputs used.

Write an algorithm that will return this data as quickly as possible.
--

- This problem statement is more general by design. In these kind of problems, it’s important for candidates to properly identify inputs, outputs, and underlying data structures.
- Some implementation constraints:
    - The candidate can assume that the input values will be strictly numeric, but she/he has to ask before the interviewer can state this.
    - The input set of values may contain duplicate values.
    - If the candidate is trying to make a copy of the data, comment on the fact that this might not be an optimal approach, but he/she can decide the input data structure.
- This problem can be approached in several ways:
    - Using a BST as input and performing Binary Search to locate the target value.
        - It’s safe for the candidate to assume that the BST is balanced.
        - __Without providing too many hints, attempt to guide the candidate to a BST if he/she is considering a different data structure.__
        - This solution takes O(lg n) time and uses either O(H) extra space in a recursive search or O(1) extra space in an iterative search.
    - Using a BST as input and perforving a traversal to locate the target value.
        - This solution takes O(n) time and uses O(H) extra space.
    - Using an array as input and checking its elements against the target value.
        - This solution takes O(n) time and uses O(1) extra space.

Considering the following abstract input `1,3,6,4,7,8,10,14,13`

| Input | Output |
|:--|:--|
| `data, 9` | `10` |
| `data, 13` | `13` |
| `data, 0` | `1` |
| `data, 'a'` | `NULL` |

### Original Instructions
https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-19/interview-01.html


#### Final Whiteboard Prompt
- You are on a development team who nedes to track the time it takes each developer to complete a task.
- Identify a data structure that can be used to __store and search__ for these times efficiently.
- Create an algorithm that will use your data structure and a provided time to determine which time in your data structure is nearest to the provided time.
- Sample Data (in hours): 15, 20, 7, 9, 3, 32, 17
