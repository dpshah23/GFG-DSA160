class Solution:
    def addBinary(self, s1, s2):
        # code here
        
        n1=int(s1,2)
        n2=int(s2,2)
        
        n3=n1+n2
        
        binary_sum = bin(n3)[2:]
        
        return binary_sum
        
