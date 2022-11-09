class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
        self.dict={
            0:1,
            1:2,
            2:4,
            3:8,
            4:16,
            5:32,
            
        }
        if turnedOn==0:
            return ['0:00']
        
        if turnedOn>=9:
            return []
        self.ans=[]
        def generate(hBits,mBits):
            hBitsComb=list(combinations([0,1,2,3],hBits))
            mBitsComb=list(combinations([0,1,2,3,4,5],mBits))
            time=[]
            for hb in hBitsComb:
                
                hours=0
                for h in hb:
                    hours+=self.dict[h]
                
                if hours>11:
                    continue
                for mb in  mBitsComb:
                    
                    minutes=0
                    for m in mb:
                        minutes+=self.dict[m]
                    
                    if minutes>59:
                        continue
                    if minutes<10:
                        minutes="0"+str(minutes)
                    else:
                        minutes=str(minutes)
                    time.append(str(hours)+":"+minutes)
                    
            
            
            time.sort()
            self.ans.extend(time)
            
            
        
        
        h,m=0,turnedOn
        
        while h<=turnedOn:
            
            generate(h,m-h)
            h+=1
        # self.ans.sort()
        return self.ans