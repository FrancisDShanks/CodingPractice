# one pass, no extra memory usage and no chages in board
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        cnt = 0
        for i, row in enumerate(board):
            for j, v in enumerate(row):
                if v == '.':
                    continue
                if i > 0 and board[i - 1][j] == 'X':
                    continue                        
                if j > 0 and board[i][j - 1] == 'X':
                    continue
                cnt += 1
        return cnt
                            
                        
