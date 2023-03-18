class BrowserHistory:

    def __init__(self, homepage: str):
        self.history=[homepage]
        self.pointer=0
        
    def visit(self, url: str) -> None:
        
        self.history=self.history[:self.pointer+1]
        self.history.append(url)
        self.pointer+=1
        
        
    def back(self, steps: int) -> str:
        
        pointer=max(0,self.pointer-steps)
        self.pointer=pointer
        return self.history[pointer]
   
    def forward(self, steps: int) -> str:
       
        pointer=min(len(self.history)-1,self.pointer+steps)
        self.pointer=pointer
        return self.history[pointer]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)