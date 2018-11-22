# a classic DFS problem with backtracking

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def helper(board, word, path, i, j):
            if (i,j) in path or (board[i][j]!= word[0]):
                return False
            path.add((i,j))
            if len(word)==1:
                return True
            if i-1>=0 and helper(board,word[1:],path,i-1,j):
                return True
            if i+1<len(board) and helper(board,word[1:],path,i+1,j):
                return True
            if j-1>=0 and helper(board,word[1:],path,i,j-1):
                return True
            if j+1<len(board[0]) and helper(board,word[1:],path,i,j+1):
                return True
            path.remove((i,j))
            return False
        
        if not board or not board[0] or not word:
            return false
        
        q = set()
        for i in range(len(board)):
            for j in range(len(board[0])):           
                if helper(board,word,q,i,j):
                    return True
        return False
        
