# Data Structure
## Stacks
- Use your Node class from your linked-list data structure
- Create a Class for a Stack which creates an empty Stack when instantiated
    - This class should be aware of a default None value assigned to top when the isntance is created
    - This class should be aware of the len of the stack, which represents the count of Nodes in the stack at any time
    - This class should have the ability to accept an iterable as an argument when instantiated, such as [1, 2, 3, 4], and creates a new Node in the stack for each value in the iterable
    - Define any further magic methods such as len and str to support user functionality and informative responses
    - Define a method called push which takes any value as an argument and adds that value to the top of the stack with an O(1) Time performance
    - Define a method called pop which takes no arguments and removes / returns the Node at the top of the stack
    - Define a method called peek which takes no arguments and returns the Node at the top of the stack
- At no time should an exception or stack trace be show to the end user. Catch and handle any such exceptions and return a printed value or operation which cleanly represents the state and either Stops execution cleanly or provides the user with clear direction and output.
- Every bit of functionality that you have should be tested and documented. As a general standard, you should have three tests for each method or body of functionality in your API.
