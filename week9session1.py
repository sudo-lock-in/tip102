from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

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

class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

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

#  You have entered your bakery into a cake baking competition and for your entry have decided build a complicated pyramid shape cake,
#  where different sections have different numbers of tiers. Given the root of a binary tree cake where each node represents a different 
#  section of your cake, return the maximum number of tiers in your cake.

# The maximum number of tiers is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated 
# time complexity. Assume the input tree is balanced when calculating time complexity.

class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def max_tiers(cake):
    if not cake:
        return 0
    def height(cake):
        if not cake:
            return 0
        if not cake.left:
            return 1 + height(cake.right)
        if not cake.right:
            return 1 + height(cake.left)
        return 1 + height(cake.left) + height(cake.right)
    leftDepth = height(cake.left)
    rightDepth = height(cake.right)
    # if not leftDepth:
    #     return rightDepth
    # if not rightDepth:
    #     return leftDepth
    return max(leftDepth, rightDepth)

# Example Usage:

"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""
# Using build_tree() function included at top of page
cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

# print(max_tiers(cake))


def can_fulfill_order(inventory, order_size):
    if not inventory:
        return order_size == 0
    # if not inventory.right:
    #     return can_fulfill_order(inventory.left, order_size - inventory.val)
    # if not inventory.left:
    #     return can_fulfill_order(inventory.right, order_size - inventory.val)
    return can_fulfill_order(inventory.left, order_size - inventory.val) or can_fulfill_order(inventory.right, order_size - inventory.val)

quantities = [5,4,8,11,None,13,4,7,2,None,None,None,1]
baked_goods = build_tree(quantities)
# print(can_fulfill_order(baked_goods, 22))
# print(can_fulfill_order(baked_goods, 2))


class TreeNode():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def zigzag_icing_order(cupcakes):
    order = []
    if not cupcakes:
        return order
    queue = deque([cupcakes]) # puts it as list to be iterable
    left_to_right = True
    while queue:
        level = deque()
        lvl_size = len(queue)
        for _ in range(lvl_size):
            node = queue.popleft()
            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        order.extend(level)
        left_to_right = not left_to_right # swaps the order
    return order

flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
cupcakes = build_tree(flavors)
# print(zigzag_icing_order(cupcakes))



