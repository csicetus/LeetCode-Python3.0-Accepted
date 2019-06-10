# 2019-06-09  Runtime: 36 ms

class Solution:
    def isValid(self, s: str) -> bool:
        
        ###############
        # other sol 1
        
#         stack, valid = [], {')':'(','}':'{',']':'['}
        
#         for st in s:
#             if st in valid:
#                 if not(stack and stack.pop() == valid[st]):
#                     return False
#             else:
#                 stack.append(st)
#         return not stack
    
    
        ###############
        # other sol 2
        
        stack = [' ']
        for c in s:
            if c in '([{':
                stack += c
            elif ord(c) % ord(stack.pop()) > 2:
                    return False
        return stack == [' ']
            
