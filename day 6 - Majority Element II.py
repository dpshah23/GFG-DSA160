class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.

        avg=len(arr)//3
        
        votes={}
        
        for i in arr:
            if i in votes.keys():
             
                votes[i]+=1
            
            else:
                votes[i]=1
        
        majority=[]        
        for candidate,count in votes.items():
            if count > avg:
                majority.append(candidate)
                
        return sorted(majority)
