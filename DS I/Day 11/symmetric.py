class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def check(left, right):
            if not left and not right:
                return True
            
            if not left or not right:
                return False
            
            if left.val == right.val:
                check_left = check(left.left, right.right)
                check_right = check(left.right, right.left)
                return check_left and check_right
            
            return False
    
        return check(root.left, root.right)
