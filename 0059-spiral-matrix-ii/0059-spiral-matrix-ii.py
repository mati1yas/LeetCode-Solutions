class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        res  = [[0] *n for _ in range(n)]
        
        row , col= 0,0
        pattern=0
        count=1
        up_bound=0
        down_bound = n-1
        left_bound = 0
        right_bound = n-1
        while count<(n*n+1):
            
            if pattern==0:
                if col>right_bound:
                    up_bound+=1
                    col-=1
                    pattern=1
                    count-=1
                else:
                    res[row][col]=count
                    count+=1
                    col+=1
            if pattern==1:
                if row>down_bound:
                    row-=1
                    right_bound-=1
                    pattern=2
                    count-=1
                else:
                    res[row][col]=count
                    count+=1
                    row+=1
            if pattern==2:
                if col<left_bound:
                    down_bound-=1
                    col+=1
                    pattern=3
                    count-=1
                else:
                    res[row][col]=count
                    count+=1
                    col-=1
            if pattern==3:
                if row<up_bound:
                    left_bound+=1
                    row+=1
                    pattern=0
                    count-=1
                else:
                    res[row][col]=count
                    count+=1
                    row-=1
        return res


