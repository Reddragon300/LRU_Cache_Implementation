# LRU Cache Implementation

This repository contains an implementation of an LRU (Least Recently Used) cache in Python. The LRU cache is designed to have O(1) time complexity for both read and write operations.
### Solves Problem:
- Design an LRU (Least Recently Used) cache with O(1) time complexity for both read and write operations.

## Implementation Details

The LRU cache implementation consists of two main components:
- `lru.py`: Contains the implementation of the LRUCache class and the Node class used for the doubly linked list.
- `lru_tests.py`: Contains test cases to verify the correctness and functionality of the LRUCache implementation.

The LRUCache class utilizes a combination of a hash map and a doubly linked list to achieve constant-time access and efficient eviction of the least recently used items. The hash map provides quick lookup of cache entries, while the doubly linked list keeps track of the order of recently accessed items.

## How to Use

1. Clone the repository to your local machine:
```bash
   git clone https://github.com/Reddragon300/lru-cache.git
```
2. Navigate to the repository directory:
```Bash
cd lru-cache
```
3. Run the test cases:
```Bash
python lru_tests.py
```
4. View the test results and the output generated by the LRU cache implementation.


## Additional Information
- The `run_tests` function in `lru_tests.py` contains several test cases that cover different scenarios, such as cache capacity limitations, inserting new items, retrieving items, and eviction of the least recently used items.
- The debug statements within the test cases provide insights into the program's execution and the state of the cache after each operation.
- The implementation strives to maintain code readability, utilize appropriate data structures, and follow best practices.
  
Feel free to explore the code and test cases to gain a deeper understanding of the LRU cache concept and its implementation.

Please note that this implementation serves as an example to demonstrate my understanding of the LRU cache concept and my Python programming skills. It is not intended for production use.

If you have any questions or feedback, feel free to reach out.

Happy coding!
