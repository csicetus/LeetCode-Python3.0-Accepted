# 2019-06-04  Runtime: 76 ms

class Solution(object):
    def newStr(self, s):
        newStr = ""
        if len(s) == 0:
            return ""
        newStr += "%"
        for i in range(0, len(s)):
            newStr += "#" + s[i]
        newStr += "#$"
        return newStr
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxLen = 0
        C = 0
        R = 0        
        centerPos = 0
        T = self.newStr(s)
        P = {}
        
        for i in range(1, len(T) - 1):
            i_mirror = 2 * C - i
            if i < R:
                P[i] = min(R - i, P[i_mirror])
            else:
                P[i] = 0

        
            while (T[i + P[i] + 1] == T[i - P[i] - 1]):
                P[i] += 1
            
            if i + P[i] > R:
                R = i + P[i]
                C = i
            
        for i in range(1, len(T) - 1):
            if maxLen < P[i]:
                maxLen = P[i]
                centerPos = i
        
        start = (centerPos - maxLen) / 2
        return s[start: start + maxLen]
