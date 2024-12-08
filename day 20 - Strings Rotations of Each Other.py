#User function Template for python3

class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
            #code her
        if len(s1) != len(s2) or len(s1) == 0:
            return False

        if s2 in (s1 + s1):
            return True
        return False