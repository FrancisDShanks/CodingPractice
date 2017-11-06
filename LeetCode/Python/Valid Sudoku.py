# -*- coding: utf-8 -*-
'''
Created on Feb 19, 2014

@author: Xufan Du, tctcdtc@gmail.com

'''

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    
    
    def isValidSudoku(self, board):
        
        row = [{} for i in range(0,9)]
        colum = [{} for i in range(0,9)]

        #check rows and colums
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]=='.':continue
                if row[i].has_key(board[i][j]):
                    return False 
                else:
                    row[i][board[i][j]]=0
                    
                if colum[j].has_key(board[i][j]):
                    return False 
                else:
                    colum[j][board[i][j]]=0
            
        #now, check all grids
        for i in [0,3,6]:
            for j in [0,3,6]:
                if self.validgrid(board,i,j)==False: return False
        
        return True
    

                
        
    def validgrid(self,board,r,c):
        #grids
        gr={}
        for i in range(r/3*3,r/3*3+3):
            for j in range(c/3*3,c/3*3+3):
                if board[i][j]=='.':
                    continue
                if gr.has_key(board[i][j]):
                    return False
                else:
                    gr[board[i][j]]=0
        
        
        return True
