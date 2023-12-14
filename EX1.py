#Arrays and Strings
def reverse_string(input):
    return input[::-1]

def fin_max_min(input):
    #set min and max element to first index in array
    max = input[0]
    min = input[0]
    #loop over array to find the min and max
    for i in input:
        if i > max:
            max = i
        if i < min:
            min = i
    return max,min

def remove_duplicates(input):
    new_list = [input[0]]
    for i in input[1:]:
        if new_list[-1] != i:
            new_list.append(i)
    return new_list



#Linked Lists
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def list_to_linked_list(lst):
    head_node = tmp = Node(0)
    for item in lst:
        tmp.next = Node(item)
        tmp = tmp.next
    return head_node.next


#Write a program to reverse a linked list.
def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


    

def find_middle_element(input):
    slow_ptr = input
    fast_ptr = input
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    return slow_ptr.data

def detectLoop(input):
    s = set()
    while (input):
        if (input in s):
            return True
        s.add(input)
        input = input.next
    return False



#Stacks and Queues
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def put(self, item):
        self.items.insert(0,item)

    def get(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


#Implement a Stack Using Two Queues
class StackUsingQueues:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, data):
        # Enqueue the element to queue1
        self.queue1.put(data)

    def pop(self):
        if self.queue1.size() == 0:
            return None

        # Move elements from queue1 to queue2, leaving one element in queue1
        while self.queue1.size() > 1:
            self.queue2.put(self.queue1.get())

        # Pop the last element from queue1
        item = self.queue1.get()

        # Swap the names of queue1 and queue2
        self.queue1, self.queue2 = self.queue2, self.queue1

        return item

#Implement a Queue Using Two Stacks
class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        # Push elements to stack1
        self.stack1.append(data)

    def dequeue(self):
        if not self.stack2:
            # If stack2 is empty, transfer elements from stack1 to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            return None  # Queue is empty

        return self.stack2.pop()


def is_balanced_parentheses(s):
    stack = []
    for char in s:
        if char in "(":
            stack.append(char)
        elif char in ")":
            if not stack:
                return False  # Unmatched closing parenthesis
            top = stack.pop()
            if (char == ")" and top != "(") :
                return False  # Mismatched opening and closing parenthesis
    return not stack  # True if stack is empty at the end




#Trees and Graphs
#find the lowest common ancestor of two nodes in a binary tree. 
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def lowest_common_ancestor(root, p, q):
    if not root:
        return None

    if root.key == p or root.key == q:
        return root

    left_ancestor = lowest_common_ancestor(root.left, p, q)
    right_ancestor = lowest_common_ancestor(root.right, p, q)

    if left_ancestor and right_ancestor:
        return root
    return left_ancestor if left_ancestor else right_ancestor



#find the shortest path between two nodes in a graph. 
#using Dijkstra's algorithm
def shortest_path(graph, start, end):
    # Initialize distances with infinity for all nodes except the start node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Keep track of visited nodes
    visited = set()

    while len(visited) < len(graph):
        # Find the node with the smallest distance that has not been visited
        current_node = min((node for node in graph if node not in visited), key=lambda node: distances[node])

        # Mark the current node as visited
        visited.add(current_node)

        # Update distances for neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = distances[current_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
    # Return the shortest distance to the end node
    return distances[end]



#Implement a binary search tree and write functions to insert, delete and search for elements.
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if not root:
            return TreeNode(key)

        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)

        return root

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp = self._find_min(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)

        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if not root or root.key == key:
            return root

        if key < root.key:
            return self._search(root.left, key)
        elif key > root.key:
            return self._search(root.right, key)

    def _find_min(self, root):
        while root.left:
            root = root.left
        return root


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)



#Sorting Algorithms
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return None  # Return None if the target is not in the array

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid  # Return the index if the target is found
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return None  # Return None if the target is not in the array



#Calculate the Factorial of a Number Using Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    


#Generate All Permutations of a String Using Recursion
def generate_permutations(s):
    if len(s) == 1:
        return [s]

    result = []
    for i in range(len(s)):
        current_char = s[i]
        remaining_chars = s[:i] + s[i + 1:]
        partial_permutations = generate_permutations(remaining_chars)

        for perm in partial_permutations:
            result.append(current_char + perm)

    return result


#hash table and write functions to insert, delete, and search for elements.
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (existing_key, _) in enumerate(self.table[index]):
                if existing_key == key:
                    # Update value if key already exists
                    self.table[index][i] = (key, value)
                    return
            self.table[index].append((key, value))

    def delete(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for i, (existing_key, _) in enumerate(self.table[index]):
                if existing_key == key:
                    del self.table[index][i]
                    return

    def search(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for existing_key, value in self.table[index]:
                if existing_key == key:
                    return value
        return None
    


#Check if a Given Number is Even or Odd Using Bit Manipulation:
def is_even_or_odd(number):
    # Check the least significant bit (LSB)
    # If LSB is 0, the number is even; otherwise, it's odd
    if number & 1 == 0:
        return "Even"
    else:
        return "Odd"
    

#Find the Number of Set Bits in a Given Integer Using Bit Manipulation
def count_set_bits(number):
    count = 0
    while number:
        count += number & 1
        number >>= 1
    return count


# time and space complexities of the sorting algorithms
'''
Bubble Sort:
Time Complexity:
 O(n^2) in the worst-case scenario, where n represents the quantity of elements.
Each iteration through the array involves the comparison and swapping of adjacent elements.
Space Complexity: O(1).
Bubble sort is an in-place sorting algorithm that doesn't necessitate additional space in proportion to the input size.

Merge Sort:
Time Complexity: O(n log n) in all situations. The divide-and-conquer approach results in log n recursive calls, and each call entails merging in linear time.
Space Complexity: O(n).
Merge sort demands extra space relative to the input size for the temporary arrays applied in merging.

Quicksort:
Time Complexity: O(n^2) in the worst-case scenario, but averages O(n log n). The partitioning process is fundamental to quicksort's efficiency.
Space Complexity: O(log n) due to its recursive nature. Quicksort is an in-place sorting algorithm; however, the recursive call stack consumes space proportionate to the logarithm of the input size.

Recursive Programs:

Factorial Calculation:
Time Complexity: O(n). The function engages in n recursive calls, and each call entails operations of constant time.
Space Complexity: O(n). The depth of the recursive call stack correlates with n.

Generating Permutations:
Time Complexity: O(n!) since there are n! permutations of an n-element string.
Space Complexity: O(n). The depth of the recursive call stack is proportional to n, and each recursive call requires O(n) additional space for the partial permutations.


'''

def can_reach_target(n, m, grid, start, target, k):
    def dfs(x, y, moves_left):
        if not (0 <= x < n and 0 <= y < m):
            return False  # Out of bounds

        if grid[x][y] == 1:
            return False  # Cell contains a rock

        if visited[x][y][moves_left]:
            return False  # Already visited with the same moves left

        if moves_left == 0 and (x, y) != target:
            return False  # Ran out of moves, and not at the target

        if (x, y) == target:
            return True  # Reached the target

        visited[x][y][moves_left] = True

        # Explore in four directions
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            if dfs(x + dx, y + dy, moves_left - 1):
                return True

        return False

    visited = [[[False] * (k + 1) for _ in range(m)] for _ in range(n)]
    return dfs(start[0], start[1], k)


# implementation of a Logger class using the Singleton pattern in Python
class Logger:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            # Initialize any necessary attributes here
            cls._instance.log_entries = []
        return cls._instance

    def log_request(self, request):
        # Log the request
        log_entry = f"Request: {request}"
        self.log_entries.append(log_entry)
        print(log_entry)

    def log_response(self, response):
        # Log the response
        log_entry = f"Response: {response}"
        self.log_entries.append(log_entry)
        print(log_entry)

    def get_log_entries(self):
        # Get all log entries
        return self.log_entries
    
