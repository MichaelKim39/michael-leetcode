
"""
Q - https://leetcode.com/problems/add-binary/

Given two binary strings a and b, return their sum as a binary string.
No leading zeros.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        carry = 0

        # Left pad smaller string with 0s
        if len(a) > len(b):
            b = '0'*(len(a)-len(b)) + b
        elif len(b) > len(a):
            a = '0'*(len(b)-len(a)) + a
        print(a, b)

        # Binary sum for one bit returning [bit, carry]
        def decToBin(dec):
            if dec == 3:
                return [1, 1]
            if dec == 2:
                return [0, 1]
            else:
                return [dec, 0]

        for i in range(1, len(a)+1):
            [bit, carry] = decToBin(int(a[-i]) + int(b[-i]) + carry)
            result = str(bit) + result

        if carry == 1:
            result = '1' + result

        return result


sol = Solution()
print(sol.addBinary('1010', '1011'))
