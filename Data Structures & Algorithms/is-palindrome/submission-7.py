class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitised = ''.join(filter(str.isalnum, s)).lower()
        print(sanitised)
        i = 0
        j = len(sanitised) - 1

        while i < j:
            if sanitised[i] != sanitised[j]:
                return False
            i += 1
            j -= 1
        
        return True