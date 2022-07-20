class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res, lvl = [], [root]
        while root and lvl:
            res.append([n.val for n in lvl])            
            lvl = [child for n in lvl for child in (n.left, n.right) if child]
        return ress
