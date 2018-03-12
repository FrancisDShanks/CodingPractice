class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1,n+1):
            if (i%3 == 0 and i%5 == 0):
                res.append("FizzBuzz")
            elif (i%3 == 0):
                res.append("Fizz")
            elif (i%5 == 0):
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
                
        
# simple switch problem
# elegant one-line solution
#	note the use of string or string
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return ['Fizz' * (not i%3) + 'Buzz' * (not i%5) or str(i) for i in range(1,n+1)]

