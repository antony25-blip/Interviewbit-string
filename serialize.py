class Solution:
    # @param A : list of strings
    # @return a strings
    def serialize(self, A):
        a=""
        for i in A:
            a+=i+str(len(i))+"~"
        return a
