class Solution:
    # @param A : list of strings
    # @return a string
    def longestCommonPrefix(self, A):
        prefix = A[0]
        if len(A)==1:
            return prefix
        for i in A:
            for j in range(len(i)):
                if j >= len(prefix):
                    prefix = prefix[:j]
                    break
                if i[j] != prefix[j]:
                    prefix = prefix[:j]
                    break
                if j+1>=len(i):
                    prefix = prefix[:j+1]
        return prefix
