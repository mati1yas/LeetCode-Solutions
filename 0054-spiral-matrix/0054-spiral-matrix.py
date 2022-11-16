class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        top=0
        bottom=len(matrix)-1
        right=len(matrix[0])-1
        left=0
        
        elements=[]
        
        col=0
        row=0
        count=0
        pattern=0
        while len(elements)<len(matrix)*len(matrix[0]):
            
            if pattern==0:
                while col<=right:
                    elements.append(matrix[row][col])
                    print('fortt',row,col)
                    col+=1
                    pattern=1
                top+=1
                col-=1
                row+=1
                
                
            if pattern==1:
            
                while row<=bottom:
                    elements.append(matrix[row][col])
                    print('down',row,col)
                    row+=1
                    pattern=2
                row-=1
                col-=1
                right-=1
                
            if pattern==2:
                while col>=left:
                    elements.append(matrix[row][col])
                    print('back',row,col)
                    col-=1
                    pattern=3
                col+=1
                row-=1
                bottom-=1
                
            if pattern==3:
                while row>=top:
                    elements.append(matrix[row][col])
                    print('up',row,col)
                    row-=1
                    pattern=0
                row+=1
                left+=1
                col+=1
            count+=1
                
        return elements
                
            