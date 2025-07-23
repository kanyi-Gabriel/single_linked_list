# Data Structures and Algorithms
## single_linked_list

### Why Use linked list rather than just use arrays which are less comlex
In arrays, elements are usually stored `contigously in memory`. This means that each element is stored right after the other. When removing or inserting elements in an array elements that intially formed the array has to be shifted up or down based on the operation carried out.
Such operations are time consuming and usually cause problems in real- time systems. To be free from problems associated with array manipulation, data is sored in **linked lists**

##### Where linked lists are used
  - dynamic data storage
  - stacks
  - queues and
  - graph implementation 

In this repository, demonstration of how delete a node that has already been set is demonstrated using `python` programming

#### Time and Space Complexity
`Time Complexity :` O(n) where n is the number of nodes in the linked list

`Best case:` **O(1)** when deleting the head node

`Worst case:` **O(n)** when deleting the last node

**Practical Application**

  `Memory Management:` Dynamic allocation and deallocation
  
  `Cache Implementation:` Removing least recently used items
  
  `Task Scheduling :` Removing completed tasks from queues
  
  `File Systems : `Managing file allocation tables
  
  `Database Systems :` Record management and indexing
  
**Limitations of Linked Lists**

  `Extra Memory :` Each node requires additional memory for the pointer
  
  `No Random Access :` Cannot directly access elements by index

  `Cache Performance :` Poor locality of reference compared to arrays
  
