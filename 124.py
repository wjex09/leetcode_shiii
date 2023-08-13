# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
      self.mx = -1000*1000*1000
      def dfs(node):
        if not node : return 0
        left_mx = max(dfs(node.left),0)
        right_mx= max(dfs(node.right),0)
        self.mx = max(node.val+right_mx+left_mx,self.mx)
        return node.val + max(left_mx,right_mx)

      dfs(root)
      return self.mx
