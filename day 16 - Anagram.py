#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        #code here
        
        s1=sorted(s1)
        s2=sorted(s2)
        
        return s1==s2