class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        #horizontal counter
        horizontal = 0
        #vertical counter
        vertical = 0
        
        for move in moves:
            if move == 'U':
                vertical += 1
            elif move == 'D':
                vertical -= 1
            elif move == 'L':
                horizontal += 1
            elif move == 'R':
                horizontal -= 1
            else:
                print("Error")
        return False if (horizontal or vertical) else True
    
                    
                
# also can use stacks
# one line version
return (moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R'))