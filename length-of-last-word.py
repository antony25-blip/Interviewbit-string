class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        flag=0
        for i in range(len(A)):
            if A[i]!=" ":
                flag+=1
            elif A[i]==" "and i<len(A)-1 and A[i+1]!=" ":
                flag=0
        return flag
  
