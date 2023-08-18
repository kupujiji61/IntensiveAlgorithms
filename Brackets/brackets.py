class Solution:
    from collections import deque
    def isValid(self, s: str) -> bool:
        d = deque()
        d.append(s[0])
        
        for i in range(1, len(s)):
            d.append(s[i])
            if len(d) >= 2:
                if d[-1] == ")":
                    if d[-2] == "(":
                        d.pop()
                        d.pop()
                elif d[-1] == "]":
                    if d[-2] == "[":
                        d.pop()
                        d.pop()
                elif d[-1] == "}":
                    if d[-2] == "{":
                        d.pop()
                        d.pop()
                
        if len(d) == 0:
            return True
        else:
            return False
