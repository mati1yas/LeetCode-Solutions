class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        
        related=defaultdict(list)
        
        for account in accounts:
            head=account[1]
            if head not in related:
                related[head]=[]
            for j ,acc2 in enumerate(account):
                
                if  j==0  or j==1 :
                    continue

                related[head].append(acc2)
                related[acc2].append(head)
        
        visited=set()
        def dfs(email):
            
            visited.add(email)
            mergedAccounts.add(email)
            for nbr in related[email]:
                if nbr not in visited:
                    dfs(nbr)
          
        ans=[]
        
        for account in accounts:
            
            if account[1] not in visited:
                mergedAccounts=set()
                dfs(account[1])
                curr=[]
                curr.append(account[0])
                curr.extend(sorted(list(mergedAccounts)))
                ans.append(curr)
        return ans
                
            
        
        
        
                        