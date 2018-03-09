# Francis Du - tctcdtc@gmail.com
# using Divided and conquer - recursion.
#       dynamic programming - record all temporary equation already built.
#                           - record all current calculated result.
#   Notice:
#           1. take care of case like '05', '00'.
#           2. * operation has a higher priority than +\- operation.
#           3. the first number in the equation don't has no operator.
class Solution:
    def __init__(self):
        self.result = []

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.result = []
        self.separate(num, target, '', 0, 0)
        return self.result

    def separate(self, num, target, temp, cursum, prenum):
        """
        :param num: string: current string of digits 
        :param target: int: target sum
        :param temp: string: current built equation
        :param cursum: int: current calculated result
        :param prenum: int: last calculated number
        :return: 
        """
        if len(num) == 0 and cursum == target:
            self.result.append(temp)
            return

        for separator in range(1, len(num) + 1):
            # separator separate the string to substring num[:separator] and num[separator:]
            left = num[:separator]
            if len(left) > 1 and left[0] == '0':
                return

            right = num[separator:]
            if len(temp) == 0:
                self.separate(right, target, left, int(left), int(left))
            else:
                self.separate(right, target, temp + '+' + left, cursum + int(left), int(left))
                self.separate(right, target, temp + '-' + left, cursum - int(left), -1 * int(left))
                self.separate(right, target, temp + '*' + left, cursum - prenum + prenum * int(left), prenum * int(left))
        return
