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


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_balanced(display):
    def balance(display):
        if not display:
            return True, 0
        leftB, leftH = balance(display.left)
        rightB, rightH = balance(display.right)
        balanced = rightB and leftB and abs(leftH - rightH) <= 1
        height = max(leftH, rightH) + 1 # plus one for current node
        return balanced, height
    balanced, _ = balance(display)
    return balanced




"""
      🎂
     /  \
   🥮   🍩
       /  \  
     🥖    🧁

"""
# Using build_tree() function included at top of page
baked_goods = ["🎂", "🥮", "🍩", None, None, "🥖", "🧁"] 
display1 = build_tree(baked_goods)

"""
          🥖
         /  \
       🧁    🧁
       /       \  
      🍪       🍪
     /           \
    🥐           🥐  

"""
baked_goods = ["🥖", "🧁", "🧁", "🍪", None, None, "🍪", "🥐", None, None, "🥐"]
display2 = build_tree(baked_goods)


# print(is_balanced(display1)) 
# print(is_balanced(display2))  



def sum_each_days_orders(orders):
    summed = []
    if not orders:
        return summed
    queue = deque([orders])
    while queue:
        lvl_size = len(queue)
        lvl_sum = 0
        # level = deque()
        for _ in range(lvl_size):
            node = queue.popleft()
            lvl_sum += node.val
            # level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        # summed.append(sum(level))
        summed.append(lvl_sum)
    return summed


"""
      4
     / \
    2   6
   / \  
  1   3
"""

# Using build_tree() function included at top of page
order_sizes = [4, 2, 6, 1, 3]
orders = build_tree(order_sizes)

# print(sum_each_days_orders(orders))


def sweet_difference(chocolates):
    diff = []
    queue = deque([chocolates])
    while queue:
        lvl_size = len(queue)
        mini = queue[0].val
        maxi = queue[0].val
        for _ in range(lvl_size):
            node = queue.popleft()
            if node.val > maxi:
                maxi = node.val
            if node.val < mini:
                mini = node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        diff.append(abs(mini - maxi))
    return diff
        


"""
  3
 / \
9  20
   / \
  15  7
"""
# Using build_tree() function included at top of page
sweetness_levels1 = [3, 9, 20, None, None, 15, 7]
chocolate_box1 = build_tree(sweetness_levels1)

"""
    1
   / \
  2   3
 / \   \
4   5   6

"""
sweetness_levels2 = [1, 2, 3, 4, 5, None, 6]
chocolate_box2 = build_tree(sweetness_levels2)

# print(sweet_difference(chocolate_box1))  
# print(sweet_difference(chocolate_box2))  



# skipped to 6 because i find it interesting
class TreeNode():
     def __init__(self, order, left=None, right=None):
        self.val = order
        self.left = left
        self.right = right

def find_next_order(order_tree, order):
    if not order_tree:
        return None
    queue = deque([order_tree])
    while queue:
        lvl_size = len(queue)
        for i in range(lvl_size):
            node = queue.popleft()
            if node == order:
                if i == lvl_size - 1:
                    return None
                else:
                    return queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return None
            
"""
        Cupcakes
       /       \ 
   Macaron     Cookies      
        \      /      \
      Cake   Eclair   Croissant
"""
cupcakes = TreeNode("Cupcakes")
macaron = TreeNode("Macaron")
cookies = TreeNode("Cookies")
cake = TreeNode("Cake")
eclair = TreeNode("Eclair")
croissant = TreeNode("Croissant")

cupcakes.left, cupcakes.right = macaron, cookies
macaron.right = cake
cookies.left, cookies.right = eclair, croissant

next_order1 = find_next_order(cupcakes, cake)
next_order2 = find_next_order(cupcakes, cookies)
print(next_order1.val)
print(next_order2)