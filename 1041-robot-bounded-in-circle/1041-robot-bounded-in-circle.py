class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        
        x,y =0,0
        curDir="n"
        
        
        for i in range(4):
            for inst in instructions:
                
                if inst=="L":

                    if curDir=='n':                  

                        curDir='w'
                    elif curDir=='s':
                        curDir='e'                   

                    elif curDir=='e':
                        curDir='n'

                    elif curDir=='w':
                        curDir='s'


                elif inst=="R":
                    if curDir=='n':                  

                        curDir='e'
                    elif curDir=='s':
                        curDir='w'                   

                    elif curDir=='e':
                        curDir='s'

                    elif curDir=='w':
                        curDir='n'

                elif inst=='G':
                    if curDir=='n':                  


                        y+=1
                    elif curDir=='s':
                        y-=1                   

                    elif curDir=='e':
                        x+=1

                    elif curDir=='w':
                        x-=1

            if x==0 and y==0:
                return True
        
        return False
                
                
            