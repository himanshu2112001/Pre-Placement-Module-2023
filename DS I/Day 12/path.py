class Solution:
    end_nodes = []
        
    def traversal(self, root):
        if root:
            if root.left:
                root.left.val += root.val
                self.traversal(root.left)

            if root.right:
                root.right.val += root.val
                self.traversal(root.right)
                
            if root.left is None and root.right is None:
                self.end_nodes.append(root.val) 
                
        return None
    
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Leetcode uses the same class instance in between function calls hence,
        # We need to clear this end nodes ...         
        self.end_nodes = []
        self.traversal(root)
        return targetSum in self.end_nodes
