# -*- coding: utf-8 -*-
'''
Created on Feb 08, 2014

@author: Xufan Du, tctcdtc@gmail.com

'''

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.solve(board)
        
    def solve(self,board):        
        for row in range(0,9):
            for col in range(0,9):
                if board[row][col] == '.':
                    for fillin in range(1,10):
                        board[row][col] = str(fillin)
                        if self.check(board,row,col):
                            if self.solve(board):
                                return True
                    board[row][col]='.'
                    return False        
        return True
                        
    def check(self,board,row,col):
        num = board[row][col]
        #check row
        for i in range(0,9):
            if i==row:
                continue
            if board[i][col]==num:
                return False
        
        #check col
        for i in range(0,9):
            if i==col:
                continue
            if board[row][i]==num:
                return False  
                
        #check grid
        a=row/3*3
        b=col/3*3
        for i in range(0,3):
            for j in range(0,3):
                if a+i==row and b+j==col:
                    continue;
                if num==board[a+i][b+j]:
                    return False
        return True
        
    
if __name__ == '__main__':
    s = Solution()
    n = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
    m=[]
    for nn in n:
        mm=[]
        for nnn in nn:
            mm.append(nnn)
        m.append(mm)
    s.solveSudoku(m)
    for mm in m:
        print mm        
