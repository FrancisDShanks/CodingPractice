# stupid solution didn't use DP - failed with TLE error
class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        pos = (self.separate(num))
        result = []
        for p in pos:
            cal = self.calculate(p)
            if cal is not None and cal == target:
                result.append(p)
        return result

    def separate(self, n):
        result = []
        if n:
            result.append(n)
            for separator in range(1, len(n)):
                # separator separate the string to substring num[:separator] and num[separator:]
                left = n[:separator]
                right = self.separate(n[separator:])

                for i_right in right:
                    result.append(left + '+' + i_right)
                    result.append(left + '-' + i_right)
                    result.append(left + '*' + i_right)
        return result

    def calculate(self, equation):
        dig = ''
        nums = []
        ops = []
        for q in equation:
            if q.isdigit():
                dig += q
            else:
                if len(dig) > 1 and dig[0] == '0':
                    return None
                nums.append(int(dig))
                ops.append(q)
                dig = ''
        if len(dig) > 1 and dig[0] == '0':
            return None
        nums.append(int(dig))

        index = 0
        while index < len(ops):
            if ops[index] == '*':
                nums[index] = nums[index] * nums[index + 1]
                del(nums[index + 1])
                del(ops[index])
            else:
                index += 1

        r = nums[0]
        for index in range(len(ops)):
            if ops[index] == '+':
                r += nums[index + 1]
            else:
                r -= nums[index + 1]
        return r
