class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        for i in t:
            if i not in d:
               
                return False
            d[i]-=1
            if d[i]==0:
                del d[i]
        return len(d)==0
                       
                    
           
        