class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            a, b = b, a
        a = a[::-1]
        b = b[::-1]
        carry = 0
        res = ''
        for i in range(len(a)):
            if i < len(b):
                tmp = int(a[i]) + int(b[i]) + carry
            else:
                tmp = int(a[i]) + carry
            if tmp == 0:
                res += '0'
                carry = 0
            elif tmp == 1:
                res += '1'
                carry = 0
            elif tmp == 2:
                res += '0'
                carry = 1
            elif tmp == 3:
                res += '1'
                carry = 1
        if carry == 1:
            res += '1'
        return res[::-1]
