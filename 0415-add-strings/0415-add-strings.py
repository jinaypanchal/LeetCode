class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = list(num1)
        n2 = list(num2)
        carry = 0
        res = ""
        i = len(n1) - 1
        j = len(n2) - 1
        while i >= 0 and j >= 0:
            # print(int(n1[i]))
            temp = str(int(n1[i]) + int(n2[j]) + carry)
            # res = temp + res
            if len(temp) > 1:
                res = temp[-1] + res
                carry = int(temp[0])
            else:
                res = temp + res
                carry = 0
            i-=1
            j-=1

        while i >= 0:
            ti = str(int(n1[i]) + carry)
            if len(ti) > 1:
                res = ti[-1] + res
                carry = int(ti[0])
            else:
                res = ti + res
                carry = 0
            i-=1
            # res = ti + res
            # i-=1
        
        while j >= 0:
            tj = str(int(n2[j]) + carry) 
            if len(tj) > 1:
                res = tj[-1] + res
                carry = int(tj[0])
            else:
                res = tj + res
                carry = 0
            j-=1
            # res = tj + res
            # j-=1
        if carry:
            res = str(carry) + res
        
        return res



        # print(n1)
        # return str(int(num1) + int(num2))
        