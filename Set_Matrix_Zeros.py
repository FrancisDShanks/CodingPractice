# -*- coding: utf-8 -*-
'''
Created on Feb 08, 2014

@author: Xufan Du, tctcdtc@gmail.com

'''

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        l = []
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if matrix[i][j] == 0:
                    l.append((i,j))
        
        for i in l:
            for row in range(0,len(matrix)):
                matrix[row][i[1]]=0
            for col in range(0,len(matrix[0])):
                matrix[i[0]][col]=0
