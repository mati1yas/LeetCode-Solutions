class Solution:
    def allPossibleBST(self, start, end, memo):
        res = []
        if start > end:
            res.append(None)
            return res
        if (start, end) in memo:
            return memo[(start, end)]
        
       
        for i in range(start, end + 1):
            leftSubTrees = self.allPossibleBST(start, i - 1, memo)
            rightSubTrees = self.allPossibleBST(i + 1, end, memo)
            
            
            for left in leftSubTrees:
                for right in rightSubTrees:
                    root = TreeNode(i, left, right)
                    res.append(root)
        
        memo[(start, end)] = res
        return res
    
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        return self.allPossibleBST(1, n, memo)