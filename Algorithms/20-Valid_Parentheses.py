class Solution:
    def isValid(self, s: str) -> bool:
        a = list()
        valid = 0
        
        for x in s:
            print(x)
            if x == '(':
                a.append("a")
                valid += 1
            elif x == ')':
                valid -= 1
                if not a:
                    break
                if(a[-1] == 'a'):
                    a.pop(-1)
            elif x == '{':
                a.append("b")
                valid += 1
            elif x == '}':
                valid -= 1
                if not a:
                    break
                if(a[-1] == 'b'):
                    a.pop(-1)
            elif x == '[':
                a.append("c")
                valid += 1
            elif x == ']':
                valid -= 1
                if not a:
                    break
                if(a[-1] == 'c'):
                    a.pop(-1)

        if valid < 0:
            return False
        elif a:
            return False
        else:
            return True