class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int> > &obstacleGrid) {
        vector<vector<int>> v;
		int m = obstacleGrid.size();
		int n = obstacleGrid[0].size();
        vector<int> row(n,0);
        int i,j;
		for(i=0;i<m;i++) v.push_back(row);
        for(i=0;i<m;i++)
		{
			if (obstacleGrid[i][0] == 0)
				v[i][0]=1;
			else{
				for(i=i+1;i<m;i++)
					v[i][0]=0;
			}
		}
        for(i=0;i<n;i++) 
		{
			if (obstacleGrid[0][i] == 0)
				v[0][i]=1;
			else{
				for(i=i+1;i<n;i++)
					v[0][i]=0;
					
				
			}
		}
        
        for(i=1;i<m;i++){
            for(j=1;j<n;j++){
				if(obstacleGrid[i][j]==1) v[i][j]=0;
				else v[i][j]=v[i-1][j]+v[i][j-1];       
            }
        }


        return v[m-1][n-1];
    }
};
