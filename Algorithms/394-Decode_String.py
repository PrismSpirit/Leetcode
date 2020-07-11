class Solution:
    def decodeString(self, s: str) -> str:
        num = ""
        stack = []
        
        for x in s:
            if x.isdigit():
                num += x
            elif x == "[":
                stack.append(num)
                stack.append("[")
                num = ""
            elif x == "]":
                res = ""
                while(stack[-1] != "["):
                    res = stack.pop() + res
                stack.pop()
                stack.append(res * int(stack.pop()))
            else:
                stack.append(x)
        
        return "".join(stack)