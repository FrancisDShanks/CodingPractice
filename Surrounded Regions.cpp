//
//Created on April 21, 2014
//
//@author: Xufan Du
//

//iteration
//pass leedcode oj
class Solution {
public:
    void solve(vector<vector<char>> &board) {
        if(board.empty()||board[0].empty()) return;
        int x = board.size();
        int y = board[0].size();
        queue<int> qx;
        queue<int> qy;
        
        for(int j=0;j<y;j++){
            if(board[0][j]=='O') {qx.push(0);qy.push(j);}
            if(board[x-1][j]=='O') {qx.push(x-1);qy.push(j);}
        }
        for(int j=0;j<x;j++){
            if(board[j][0]=='O') {qx.push(j);qy.push(0);}
            if(board[j][y-1]=='O') {qx.push(j);qy.push(y-1);}
        }
        
        while(!qx.empty()){
            int i=qx.front();
            int j=qy.front();
            qx.pop();
            qy.pop();
            board[i][j] = 'Y';
            if(i>0 && board[i-1][j]=='O') {qx.push(i-1);qy.push(j);}
            if((i<board.size()-1) && board[i+1][j]=='O') {qx.push(i+1);qy.push(j);}
            if(j>0 && board[i][j-1]=='O') {qx.push(i);qy.push(j-1);}
            if((j<board[0].size()-1) && board[i][j+1]=='O') {qx.push(i);qy.push(j+1);}
        }

        for(int i=0;i<x;i++)
            for(int j=0;j<y;j++)
                if(board[i][j]=='O')
                    board[i][j]='X';
        for(int i=0;i<x;i++)
            for(int j=0;j<y;j++)
                if(board[i][j]=='Y')
                    board[i][j]='O';
        return;
            
    }
};


//recursion
//runtime error for large case in leetcode oj
class Solution {
public:
    void solve(vector<vector<char>> &board) {
        if(board.empty()||board[0].empty()) return;
        int x = board.size();
        int y = board[0].size();
        for(int j=0;j<y;j++){
            if(board[0][j]=='O') toy(board,0,j);
            if(board[x-1][j]=='O') toy(board,x-1,j);
        }
        for(int j=0;j<x;j++){
            if(board[j][0]=='O') toy(board,j,0);
            if(board[j][y-1]=='O') toy(board,j,y-1);
        }
            

            
        
        
        for(int i=0;i<x;i++)
            for(int j=0;j<y;j++)
                if(board[i][j]=='O')
                    board[i][j]='X';
        for(int i=0;i<x;i++)
            for(int j=0;j<y;j++)
                if(board[i][j]=='Y')
                    board[i][j]='O';
        return;
    }
        
        
    void toy(vector<vector<char>> &board,int i,int j){
        board[i][j] = 'Y';
        if(i>0 && board[i-1][j]=='O') toy(board,i-1,j);
        if((i<board.size()-1) && board[i+1][j]=='O') toy(board,i+1,j);
        if(j>0 && board[i][j-1]=='O') toy(board,i,j-1);
        if((j<board[0].size()-1) && board[i][j+1]=='O') toy(board,i,j+1);
        return;
    }
    

};
