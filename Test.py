from EX1 import *


def test_fun(fun_name, input):
    print('input = ',input)
    print('output = ',fun_name(input))
    print()   


print("Arrays and Strings")
print("reverse a string in place")
test_fun(reverse_string,'abcdefg')

print('find the maximum and minimum elements in an array')
test_fun(fin_max_min,[123,34,2,45,6,2,54,7,0,21,5])

print('remove duplicates from a sorted array')
test_fun(remove_duplicates,[1,1,2,2,3,3,7,8,8,9,9])



print("Linked Lists")

def print_linked_list(input):
    while input:
        print(input.data, end=" ")
        input = input.next


list_ex1 = [1,3,12,54,523,1235,6,7,89,109,3,5,7]
linked_list_head = list_to_linked_list(list_ex1)

# Print the reversed linked list
print("Old Linked list")
print_linked_list(linked_list_head)

# Reverse the linked list
new_linked_list_head = reverse_linked_list(linked_list_head)

print("")
print("NEW Linked list")
print_linked_list(new_linked_list_head)

print("")
print("middle element")
print(find_middle_element(new_linked_list_head))


if not detectLoop(new_linked_list_head):
    print("No Cycle detected")

# Introduce a cycle for demonstration purposes
print("")
print("Adding a cycle to the list")
new_linked_list_head.next.next.next.next = new_linked_list_head
if  detectLoop(new_linked_list_head):
    print("Cycle detected")


print("")
print("")
print("Stacks and Queues")
print("")
print("stack using two queues")
stack = StackUsingQueues()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 2

print("")
print("queue using two stacks")
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2

print("")
print("check if a given string of parentheses is balanced")
# Example usage:
expression = "(())(()())))"
print(expression)
print(is_balanced_parentheses(expression))  # Output: True

expression = "((((((()))))))"
print(expression)
print(is_balanced_parentheses(expression))  # Output: False


print("Trees and Graphs:")
# Assuming the following binary tree:
#       3
#      / \
#     5   1
#    / \ / \
#   6  2 0  8
#     / \
#    7   4
print("Assuming the following binary tree:")
print("       3")
print("     5   1")
print("   6  2 0  8")
print("    7   4")
print("")
print("")
print("")
print("")

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

print("lowest_common_ancestor for 2, 0")
ancestor = lowest_common_ancestor(root, 2, 0)
print("Lowest Common Ancestor:", ancestor.key)  # Output: 3


print("")


# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

print(graph)
start_node = 'A'
end_node = 'D'
print("start_node = 'A'")
print("")

result = shortest_path(graph, start_node, end_node)
print(f"The shortest path from {start_node} to {end_node} is: {result}")