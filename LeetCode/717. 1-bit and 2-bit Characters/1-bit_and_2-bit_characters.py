class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits) == 1:
            return True

        index = 0
        while index < len(bits)-1:
            if bits[index] == 0:
                index += 1
            else:
                index +=2
        if index == len(bits):
            return False
        else:
            return True
            
            
            
# optimized version
class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """

        index = 0
        while index < len(bits)-1:
            index += bits[index] + 1
                
        return not (index == len(bits))
            

# another algorithm
# check from the tail-1 to the head
# count all one's appeared, if meet an zero, stop the checking
# because there is no '01' bits, so the 0 must be a one-bit or a part of a '10' bits,
# on matter which situation, we just care about '11111....1110' in the tail which decide the result
# if the count of ones can be divided by 2, all 1's are part of '11' bits, so return true, the last 0 is isolated,
# else return false, because there is one '1' is along, the tail must be a '10' bit.
class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = len(bits)-2
        cnt = 0
        while i >= 0:
            if bits[i]==1:
                cnt += 1
            else:
                break
            i -= 1
        return cnt % 2 == 0
