# Given the root of a binary tree where each node represents the number of splits in a leaf of a Monstera plant, 
# return the number of Monstera leaves 🍃 that have an odd number of splits.

# Evaluate the time complexity of your function. Define your variables and provide a 
# rationale for why you believe your solution has the stated time complexity.

# Note: The term leaf in this problem refers to the plant leaf 🍃 of a Monstera plant, not the type of node leaf nodes which are nodes with no children.

from collections import deque

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)


def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def count_odd_splits(root):
    if not root:
        return 0
    if root.val % 2 == 1:
        return 1 + count_odd_splits(root.left) + count_odd_splits(root.right)
    return count_odd_splits(root.left) + count_odd_splits(root.right) 

# Example Usage:

# """
#       2
#      / \
#     /   \
#    3     5
#   / \     \
#  6   7     12
# """

# Using build_tree() function included at top of page
values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

print(count_odd_splits(monstera))
print(count_odd_splits(None))

# Example Output:



# You have just purchased a new houseplant and are excited to add it 
# to your collection! Your collection is meticulously organized using a Binary Search Tree (BST)
#  where each node in the tree represents a houseplant in your collection, and houseplants are organized alphabetically by name (val).

# Given the root of your BST collection and a new houseplant name, insert a new node with value 
# name into your collection. Return the root of your updated collection. If another plant with name already exists in the tree,
#  add the new node in the existing node's right subtree.

# Evaluate the time complexity of your function. Define your variables and provide a rationale for
# why you believe your solution has the stated time complexity. Assume the input tree is 
# balanced when calculating time complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def add_plant(collection, name):
    pass

# Example Usage:

# """
#             Money Tree
#         /              \
# Fiddle Leaf Fig    Snake Plant
# """

# Using build_tree() function at the top of page
values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(add_plant(collection, "Aloe"))

# Example Output:

# ['Money Tree', 'Fiddle Leaf Fig', 'Snake Plant', 'Aloe']

# Explanation: 
# Tree should have the following structure:
#            Money Tree
#         /              \
#  Fiddle Leaf Fig   Snake Plant
#    /
#  Aloe

