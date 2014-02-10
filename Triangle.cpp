 //
//Created on Feb 07, 2014
//
//@author: Xufan Du
//

//this is done with extra space O((n+1)(n+1)/2) where n is the number of row in the triangle
class Solution {
public:
    int minimumTotal(vector<vector<int> > &triangle) {
        vector<vector<int>> v(triangle);
		//the last row is v.size()-1, and we start at the second last row
        int row = v.size()-2;
        while(row>=0){
            for(int i=0;i<=row;i++){
                v[row][i] += v[row+1][i]<v[row+1][i+1]?v[row+1][i]:v[row+1][i+1];
            }
            row--;
        }
        return v[0][0];
        
    }
};



//this is done with bonus point
class Solution2 {
public:
    int minimumTotal(vector<vector<int> > &triangle) {
		//initial a vector as copy of the last row
		//which has the size of the number of row of the triangle(also the size of the last row)
        vector<int> v(triangle[triangle.size()-1]);
		//the last row is v.size()-1, and we start at the second last row
        int row = triangle.size()-2;
        while(row>=0){
            for(int i=0;i<=row;i++){
                v[i] = triangle[row][i] + (v[i]<v[i+1]?v[i]:v[i+1]);
            }
            row--;
        }
        return v[0];
    }
};
