class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        
        def traverse(root):
            if root is None:
                return
            traverse(root.left)
            traverse(root.right)
            result.append(root.val)
        
        traverse(root)
        
        return result
