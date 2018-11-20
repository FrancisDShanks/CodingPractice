class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s = []
        for i in tokens:
            # there is a bug in first try
            # if i='-11', then isnumeric will be false
            # because str.isnumeric() can not handle negative numder
            # for this problem, +-*/ all only have length of one, and negative number must have length larger than one(negative mark and digits)
            # so it's easy to handle here
            if len(i)>1 or i.isnumeric():
                s.append(int(i))
            else:
                tmp2 = s.pop()
                tmp1 = s.pop()
                if i == '+':
                    tmp = tmp1 + tmp2
                elif i == '-':
                    tmp = tmp1 - tmp2
                elif i == '*':
                    tmp = tmp1 * tmp2
                elif i == '/':
                    tmp = int(tmp1 / tmp2)
                s.append(tmp)
        
        return s.pop()
