class Solution:
    def isValid(self, s: str) -> bool:
        while any(p in s for p in ['()', '[]', '{}']):
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
        
        return s == ''