class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameSubTree(root,subroot,notSame):
            if root is None and subroot is None:
                return notSame
            if notSame or root is None or subroot is None or root.val != subroot.val:
                notSame = True
                return notSame
            
            notSame = sameSubTree(root.left,subroot.left,notSame)
            notSame = sameSubTree(root.right,subroot.right,notSame)
            return notSame
        
        def helper(node,targetNode,result):
            if node is None or result:
                return result
            if node.val == targetNode.val:
                if not sameSubTree(node,targetNode,None):
                    result = True
            result = helper(node.left,targetNode,result)
            result = helper(node.right,targetNode,result)  
            return result
        return helper(root,subRoot,False)