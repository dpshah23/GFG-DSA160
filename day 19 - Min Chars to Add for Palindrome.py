class Solution:
    def minChar(self, s):
        #Write your code here

        def compute_lps(pattern):
            n = len(pattern)
            lps = [0] * n
            length = 0
            i = 1
            
            while i < n:
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        
        reversed_s = s[::-1]
        temp = s + "$" + reversed_s
        lps = compute_lps(temp)
        return len(s) - lps[-1]