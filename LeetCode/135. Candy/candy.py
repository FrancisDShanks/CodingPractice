# this problem is a dynamic programming problem
# two loops:
# first loop from left to right, make sure every child has one more candy than the left one if the child has a higher rate
# second loop from right to left, do the same thing
# I made a mistake in my first submission like this:
# c[i-1] = c[i] + 1
# I didn't realize the value if c[i-1] get from the first loop may be overwriten in the second loop
# the correct algorithm should be:
# c[i-1] = max(c[i-1],c[i]+1)

class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        c = [1] * len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                c[i] = c[i-1] + 1
        for i in range(len(ratings)-1,0,-1):
            if ratings[i-1] > ratings[i]:
                c[i-1] = max(c[i-1],c[i] + 1)
        return sum(c)
