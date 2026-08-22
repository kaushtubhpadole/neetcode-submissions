class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_l=sorted(list(s))
        t_l=sorted(list(t))
        if s_l == t_l:
            return True
        else:
            return False