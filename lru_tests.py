from lru import LRUCache


def run_tests():
    # Test case 1: Testing cache with capacity 2
    print("Test Case 1: Testing cache with capacity 2")
    cache = LRUCache(2)
    cache.put(1, "One")
    cache.put(2, "Two")
    print("Cache after inserting (1, 'One'), (2, 'Two'):", cache.cache)
    print("Get key 1 from cache:", cache.get(1))  # Expected output: "One"
    print("Cache after get operation:", cache.cache)
    cache.put(3, "Three")  # The cache is full, so "Two" will be evicted
    print("Cache after inserting (3, 'Three') and evicting key 2:", cache.cache)
    # Expected output: -1, as key 2 is no longer in the cache
    print("Get key 2 from cache:", cache.get(2))

    print("\n------------------------------------\n")  # Separator line

    # Test case 2: Testing cache with capacity 3
    print("Test Case 2: Testing cache with capacity 3")
    cache = LRUCache(3)
    cache.put("A", 1)
    cache.put("B", 2)
    cache.put("C", 3)
    print("Cache after inserting keys 'A', 'B', 'C':", cache.cache)
    print("Get key 'A' from cache:", cache.get("A"))  # Expected output: 1
    print("Cache after get operation:", cache.cache)
    cache.put("D", 4)  # The cache is full, so "B" will be evicted
    print("Cache after inserting key 'D' and evicting key 'B':", cache.cache)
    # Expected output: -1, as key "B" is no longer in the cache
    print("Get key 'B' from cache:", cache.get("B"))
    print("Get key 'D' from cache:", cache.get("D"))  # Expected output: 4

    print("\n------------------------------------\n")  # Separator line

    # Test case 3: Testing cache with capacity 1
    print("Test Case 3: Testing cache with capacity 1")
    cache = LRUCache(1)
    cache.put("X", 100)
    print("Cache after inserting key 'X':", cache.cache)
    print("Get key 'X' from cache:", cache.get("X"))  # Expected output: 100
    print("Cache after get operation:", cache.cache)
    cache.put("Y", 200)  # The cache is full, so "X" will be evicted
    print("Cache after inserting key 'Y' and evicting key 'X':", cache.cache)
    # Expected output: -1, as key "X" is no longer in the cache
    print("Get key 'X' from cache:", cache.get("X"))
    print("Get key 'Y' from cache:", cache.get("Y"))  # Expected output: 200

    print("\n------------------------------------\n")  # Separator line

    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
