
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Helper function to build a binary tree from a list representation (level order traversal)
def build_tree(nodes):
    if not nodes or nodes[0] is None:
        return None

    # Initialize the root of the tree
    root = TreeNode(nodes[0])
    queue = deque([root])
    index = 1

    # Process nodes level by level
    while queue and index < len(nodes):

        print("Queue:", [node.val if node else None for node in queue])

        current = queue.popleft()

        # Assign left child
        if index < len(nodes) and nodes[index] is not None:
            current.left = TreeNode(nodes[index])
            queue.append(current.left)
        index += 1

        # Assign right child
        if index < len(nodes) and nodes[index] is not None:
            current.right = TreeNode(nodes[index])
            queue.append(current.right)
        index += 1

    return root


# LEETCODE Soulution class
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False
        
        # Recursive comparison of trees
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or \
               (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
    


# Test locally with sample inputs
if __name__ == "__main__":
    # sample input -- 1
    tree1 = [1, 2, 3, 4, 5, 6, None, None, None, 7, 8]
    tree2 = [1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7]

    # sample input -- 2
    # tree1 = []
    # tree2 = [1]
    
    # Build the binary trees from the list
    root1 = build_tree(tree1)
    root2 = build_tree(tree2)
    
    # Create Solution object and check if trees are flip equivalent
    solution = Solution()
    result = solution.flipEquiv(root1, root2)
    
    print(f"Are the trees flip equivalent? {result}")
