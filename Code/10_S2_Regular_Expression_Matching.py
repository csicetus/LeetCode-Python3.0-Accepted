# 2019-06-06  Runtime: 2284 ms

class Solution(object):
    def isMatch(self, s: str, p: str) -> bool:
        return self.func(s, 0, p, 0)
    
    def func(self, s: str, x: int, p: str, y: int):        
        if y == len(p):
            return x == len(s)
        if x > len(s):
            return False
        
        if y < len(p) - 1 and p[y + 1] == '*':
            return (self.isThisMatch(s, x, p, y) and self.func(s, x + 1, p, y)) or self.func(s, x, p, y + 2) 
            
        if self.isThisMatch(s, x, p, y):
            return self.func(s, x + 1, p, y + 1)
            
        return False
            
    def isThisMatch(self, s: str, x: int, p: str, y: int):
        if x == len(s) or y == len(p):
            return False
        
        return p[y] == '.' or s[x] == p[y]
