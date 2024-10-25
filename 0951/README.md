
# Flip Equivalent Binary Trees - Problem Reference

### Problem Statement

Given two binary trees, `root1` and `root2`, determine if they are *flip equivalent*. A binary tree is *flip equivalent* to another if we can make one tree identical to the other by flipping any number of nodes (swapping their left and right subtrees).

### Example

```plaintext
Input: root1 = [1, 2, 3, 4, 5, 6, None, None, None, 7, 8], 
       root2 = [1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7]
Output: true
Explanation: We flipped nodes at values 1, 3, and 5.
```

---

### Steps to Solve
#### 1. Understand Binary Trees

 - **Binary Tree**: A data structure with nodes, where each node has at most two children, typically called left and right.
 - **Flip Operation**: Swapping the left and right children of a node.

#### 2. Recursive Approach to Check Flip Equivalence


The core idea is to compare nodes of `root1` and `root2` recursively by following these checks:

 1. **Base Case**: If both nodes are `None`, they are equivalent.
 2. **Mismatch Case**: If only one node is `None` or the values of the nodes differ, the trees are not flip equivalent.
 3. **Recursive Check**: To determine equivalence, check two cases:
   - **No Flip**: Recursively compare `root1.left` with `root2.left` and `root1.right` with `root2.right`.
   - **Flip**: Recursively compare `root1.left` with `root2.right` and `root1.right` with `root2.left`.

This way, we can determine if both trees can become identical after a series of flip operations.

