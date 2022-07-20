class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        ## Approach 1
        def dfs(node, temp):
            if not node : return
            temp.val = node.val
            
            if node.left != None :
                temp.right = TreeNode()
            
            if node.right != None :
                temp.left = TreeNode()
            
            dfs(node.left, temp.right)
            dfs(node.right, temp.left)
        
        
        dummy = TreeNode()
        dfs(root, dummy)
        
        if not root : return
        return dummy
