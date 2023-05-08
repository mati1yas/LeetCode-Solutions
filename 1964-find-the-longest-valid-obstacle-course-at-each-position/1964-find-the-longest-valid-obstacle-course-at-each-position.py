class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        
        
        subsequence=[]
        
        answer=[]
        
        for i in range(len(obstacles)):
            
            num = obstacles[i]
            insertionPoint = bisect_right(subsequence,num)
            
            if insertionPoint>=len(subsequence):
                
                subsequence.append(num)
                
            
            else:
                
                subsequence[insertionPoint] = num
                
            answer.append(insertionPoint+1)
        
        return answer