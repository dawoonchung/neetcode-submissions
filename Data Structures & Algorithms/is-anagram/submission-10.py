class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False

        sentinel_s = dict()
        sentinel_t = dict()

        for i in range(len(s)):
            _s = s[i]
            _t = t[i]

            if _s in sentinel_s:
                sentinel_s[_s] += 1
            else:
                sentinel_s[_s] = 1

            if _t in sentinel_t:
                sentinel_t[_t] += 1
            else:
                sentinel_t[_t] = 1
            
        for k in sentinel_s.keys():
            if not k in sentinel_t:
                return False
            if sentinel_s[k] != sentinel_t[k]:
                return False
        
        return True

        # return sorted(s) == sorted(t)