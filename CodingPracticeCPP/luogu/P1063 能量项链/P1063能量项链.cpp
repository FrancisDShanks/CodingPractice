// 环状-区间动态规划问题
// 状态转移方程为  
// dp[i][j] = max(dp[i][j], dp[i][k]+dp[k+1][j]+cost);
// 其中cost 为 a[i]*a[k+1]*a[j+1]
// 这里比较绕,i,j中间取k, [i,k]得头为a[i],尾为a[k+1],因为第k个珠子的头为k,尾为k+1
// [k+1,j] 的头为k+1,尾为j+1  (不是j)
// 因为是环状,采用割环的思路,将长度为n的环割为长度为2n-1的链
// 所以三层循环,
// 第一层是区间长度p,从2取到n
// 第二层是区间起点遍历i,从1到 i+p-1<=2*n-1, 左边表示尾部,长度为p,取头去尾所以是 i+p-1, 左边是链长度 2*n-1
// 第三层是区间中间点的遍历k, 从i 到 j-1 

#include <bits/stdc++.h>
using namespace std;
int main(){
	int n,a[201];
	cin>>n;
	for(int i=1;i<=n;++i){
		cin>>a[i];
		a[i+n] = a[i];
	}
	
	int dp[201][201];
	memset(dp,0,sizeof(dp));
	
	for(int p=2;p<=n;++p){
		for(int i=1;i+p-1<2*n;++i){
			int j=i+p-1;
			for(int k=i;k<j;++k){
				int cost = a[i]*a[k+1]*a[j+1];
				dp[i][j] = max(dp[i][j], dp[i][k]+dp[k+1][j]+cost);
			}
		}
	}
	
	// 最后结果是长度为n的取法中的值最大的一种 
	int maxp=-1;
	for(int i=1;i<=n;++i){
		if(maxp < dp[i][i+n-1]) maxp = dp[i][i+n-1];
	}
	cout<<maxp;
	
	return 0;
}
