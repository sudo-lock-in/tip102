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


# You have a trailing ivy plant represented by a binary tree. 
# You want to take a cutting to start a new plant using the rightmost vine in the plant. Given the root of the plant, return a list
# with the value of each node in the path from the root node to the rightmost leaf node. 
# If there is no right child, return only the root node value (the rightmost path in this case is just the root node).

# Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has
# the stated time complexity. Assume the input tree is balanced when calculating time complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
    path = []
    curr = root
    if not curr.right:
        path.append(curr.val)
        return path
    while curr:
        path.append(curr.val)
        curr = curr.right
    # path.append(curr.right.val)
    return path


# Example Usage:

# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """
ivy1 = TreeNode("Root", 
                 TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
# """
#       Root
#       /  
#     Node1
#     /
#   Leaf1  
# """



ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


# print(right_vine(ivy1))
# print(right_vine(ivy2))




# You have a large overgrown Magnolia tree that's in desperate need of some pruning. Before you can prune the tree, 
# you need to do a full survey of the tree to evaluate which sections need to be pruned.

# Given the root of a binary tree representing the magnolia, return a list of the values of each node using a postorder traversal. 
# In a postorder traversal, you explore the left subtree first, then the right subtree, and finally the root. Postorder traversals 
# are often used when deleting nodes from a tree.

# Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your 
# solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

# def survey_tree(root):
#     path = []
#     leftTrav = root
#     rightTrav = root

#     while leftTrav:
#         path = []
#         leftTrav = leftTrav.left
#         if leftTrav:
#             path.append(leftTrav.val)

#     while rightTrav:
#         path = []
#         rightTrav = rightTrav.right
#         if rightTrav:
#             path.append(rightTrav.val)
#     path.append(root.val)
#     return path

#     # while curr:
#     #     if curr.left:
#     #         curr = curr.left
#     #         path.append(curr.val)
#     #     curr = root
#     #     elif curr.right:
#     #         curr = curr.right
#     #         path.append(curr.val)
        
#     return path

#bradshaw's answer 
def survey_tree(root):
    # Base case: if the current node is empty, return an empty list
    if not root:
        return []
    # Recursively traverse the left subtree, then the right subtree,
    # and combine them with the current node's value at the end.
    return survey_tree(root.left) + survey_tree(root.right) + [root.val]


# Example Usage:

# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """

magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

print(survey_tree(magnolia))

# Example Output:

# ["Leaf1", "Node1", "Leaf2", "Leaf3", "Node2", "Root"]




