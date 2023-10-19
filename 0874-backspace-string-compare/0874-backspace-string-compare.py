class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool: 
        # if s[0] == '#' or t[0] == '#':
        #     return False

        def helper(s):
            stack=[]
            for i in s:
                if i != '#':
                    stack.append(i)
                elif stack:
                    stack.pop()
            # print(stack)            
            return "".join(stack)


        x = helper(s)
        y = helper(t)
        return(x==y)    
