class Solution:
    def reformatDate(self, date: str) -> str:
        month={"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        
        
        
        d,m,y=date.split(" ")
        nday=""
        for char in d:
            
            if not char.isdigit():
                break
            nday+=char
        
        if int(nday)<10:
            nday="0"+nday
        
        return y+"-"+month[m]+"-"+nday
        
        
        