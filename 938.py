# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    Y = (lambda f: (lambda x: f(lambda *args: x(x)(*args)))(lambda x: f(lambda *args: x(x)(*args))))
    dfs = lambda f: lambda node , low , high : 0 if node is None else  (node.val if low <= node.val <= high else 0) + f(node.left,low,high) + f(node.right,low,high)
    dfs = Y(dfs)
    return dfs(root,low,high)
