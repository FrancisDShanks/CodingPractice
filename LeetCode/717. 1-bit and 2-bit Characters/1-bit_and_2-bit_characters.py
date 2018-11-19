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
            
