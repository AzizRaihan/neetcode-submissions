class TimeMap:
    hm={}
    y=0

    def __init__(self):
        self.hm={}
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hm:
            self.hm[key].append((value,timestamp))
        else:
            self.hm[key]=[(value,timestamp)]


    

       



        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hm:
            return ""
        else:
            l=0
            r=len(self.hm[key])-1
            y=""
            while (l<=r):
                m=(l+r)//2
                x=self.hm[key][m][1]
                if x==timestamp:
                    return self.hm[key][m][0]
                elif (x<timestamp):
                    l=m+1
                    y=self.hm[key][m][0]
                elif (x>timestamp):
                    r=m-1
        return y


                

           
         

            



        
