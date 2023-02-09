class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
    
        self.answer=set()
        def backTrack(ipAddress,start):
            
            # base case 
            
            if len(ipAddress)==4 and start==len(s):
                self.answer.add(".".join(ipAddress))
                
                return 
            if len(ipAddress)==4 and start!=len(s):
                
                return 
            
            
            for i in range(1,4):
                
                port=s[start:start+i]
                
                
                if port and int(port)<=255 :
                    
                    if len(port)>=2 and port[0]=="0":
                        continue
                    backTrack(ipAddress+[port],min(start+i,len(s)))
            
            
        
        backTrack([],0)
        return list(self.answer)