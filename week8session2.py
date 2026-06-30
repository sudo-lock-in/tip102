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

# print(count_odd_splits(monstera))
# print(count_odd_splits(None))



class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         


def find_flower(inventory, name):
    if not inventory:
        return False
    if inventory.val == name:
        return True
    return find_flower(inventory.left, name) if name < inventory.val else find_flower(inventory.right, name)


values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
garden = build_tree(values)

# print(find_flower(garden, "Lilac"))  
# print(find_flower(garden, "Sunflower")) 


def non_bst_find_flower(root, name):
    if root is None:
        return False
    
    if root.val == name:
        return True

    return non_bst_find_flower(root.left, name) or non_bst_find_flower(root.right, name)


# Compare your solution to find_flower() in Problem 2 to the following solution. Discuss with your group: How is the code different? Why?
# >We traverse through all nodes in this one while in problem 2 we use a binary search
# What is the time complexity of non_bst_find_flower()? How does it compare to the time complexity of find_flower() in Problem 2?
# >The time complexity is O(N). The time complexity of problem 2 is O(log N) 
# How would the time complexity of find_flower() from Problem 2 change if the tree inventory was not balanced? 
# >It would become O(N) if the height equals the amount of nodes. Since it is technically going by O(H) where H is height

values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree(values)


# print(non_bst_find_flower(garden, "Lilac"))  
# print(non_bst_find_flower(garden, "Sunflower"))  




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
    if not collection:
        return TreeNode(name)
    if name >= collection.val:
        collection.right = add_plant(collection.right, name)
    else:
        collection.left = add_plant(collection.left, name)
    return collection    

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
# print_tree(add_plant(collection, "Aloe"))

# Example Output:

# ['Money Tree', 'Fiddle Leaf Fig', 'Snake Plant', 'Aloe']

# Explanation: 
# Tree should have the following structure:
#            Money Tree
#         /              \
#  Fiddle Leaf Fig   Snake Plant
#    /
#  Aloe

class TreeNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key      # Plant rarity
        self.val = value      # Plant name
        self.left = left
        self.right = right


def sort_plants(collection):
    output = []
    # inorder is left -> root -> right
    # postorder is left -> right -> root
    # preorder is root -> left -> right
    def inorder(collection, output):
        if collection:
            inorder(collection.left, output)
            output.append((collection.val, collection.key))
            inorder(collection.right, output)
        return output
    return inorder(collection, output)


values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
collection = build_tree(values)

# print(sort_plants(collection))



class TreeNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key      # Plant price
        self.val = val      # Plant name
        self.left = left
        self.right = right

def pick_plant(inventory, budget):
    output = []
    # inorder is left -> root -> right
    # postorder is left -> right -> root
    # preorder is root -> left -> right
    def inorder(inventory, output, budget):
        if inventory:
            inorder(inventory.left, output, budget)
            if inventory.val < budget:
                output.append((inventory.key))
            inorder(inventory.right, output, budget)
        if output:
            return output[-1]
        return None
    return inorder(inventory, output, budget)

values = [(50, "Fiddle Leaf Fig"), (25, "Monstera"), (70, "Snake Plant"), (15, "Aloe"), 
            (40, "Pothos"), (60, "Fern"), (80, "ZZ Plant")]
inventory = build_tree(values)

# print(pick_plant(inventory, 50)) 
# print(pick_plant(inventory, 25)) 
# print(pick_plant(inventory, 15)) 

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def remove_plant(collection, name):
    if not collection:
        return None
    # Find the node to remove
    if collection.val > name:
        collection.left = remove_plant(collection.left, name)
    elif collection.val < name:
        collection.right = remove_plant(collection.right, name)
    else:
    # If the node has no children
        # Remove the node by setting parent pointer to None
        if not collection.right and not collection.left:
            return None
    # If the node has one child
        # Replace the node with its child
        if not collection.right:
            return collection.left
        elif not collection.left:
            return collection.right
    # If the node has two children
        # Find the inorder predecessor 
    # To find the inorder predecessor, we can follow the following steps:
    # If the node has a left subtree, the predecessor is the rightmost (largest) node in the left subtree.
    # If the node doesn't have a left subtree, you traverse upwards to find the deepest ancestor for which the given node lies in the right subtree.
        def rightmost(collection):
            curr = collection
            while curr.right:
                curr = curr.right
            return curr
        pre = rightmost(collection.left)
        # Replace the node's value with inorder predecessor value
        collection.val = pre.val
        # Remove inorder predecessor
        collection.left = remove_plant(collection.left, pre.val)
    # Return root of updated tree
    return collection
  
    

    
# Using build_tree() function at the top of page
values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(remove_plant(collection, "Pilea"))

