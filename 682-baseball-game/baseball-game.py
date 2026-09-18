class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record=[]
        for i in operations:
            if i=="D":
                record.append(record[-1]*2)
            elif  i=="+":
                record.append(record[-1]+record[-2])
            elif i=="C":
                record.pop()
            else:
                record.append(int(i))  
        return sum(record)  

                
            

        