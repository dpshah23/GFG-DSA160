class Solution:
    def myAtoi(self, s):
        # Code here

        s = s.lstrip()
        
        if not s:
            return 0
            
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
            
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            else:
                break
        
        num *= sign
        
        int_min, int_max = -2**31, 2**31 - 1
        if num < int_min:
            return int_min
        elif num > int_max:
            return int_max
            
        
        return num