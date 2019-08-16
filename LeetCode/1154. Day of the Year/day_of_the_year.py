class Solution:
    def dayOfYear(self, date: str) -> int:
        days_of_month = [31,28,31,30,31,30,31,31,30,31,30,31]
        y, m, d = date.split('-')
        # check the leak year
        # notice even the year is a leak year but month is 1st or 2nd, no nead to add 1 more day
        ret = 1 if ((int(y) % 400 == 0) or (int(y) % 4 == 0 and int(y) % 100 != 0)) and int(m) > 2 else 0
        for i in range(1, int(m)):
            ret += days_of_month[i - 1]
        return ret + int(d)
