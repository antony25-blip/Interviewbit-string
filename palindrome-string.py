class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        cleaned=''.join(char.lower() for char in A if char.isalnum())
        return 1 if cleaned == cleaned[::-1] else 0
        
