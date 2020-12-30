// 几种解法
// 1. 暴力枚举 O(n^2)
// 2. 递归解法 O(nlogn)	取中点,递归求中点左边的最大子段,中点右边的最大子段,和包括中点的最大子段 
// 3. 动态规划 O(n) 

#include <bits/stdc++.h>
using namespace std;
int main(){
	int n, a;
	cin>>n;
	cin>>a;
	int maxsum = a, sumsofar = a;
	for(int i=2;i<=n;++i){	//子问题的后边界 
		cin>>a;
		// 动态规划 状态转移方程
		// dp[i] = max(dp[i-1] + a[i], a[i])
		// 其中 dp[i]表示的是以i为结尾的最大的子段和,必须包含i
		// dp[i-1] + d[i] 表示以i-1结尾的最大子段和 + a[i] 
		// 与只有a[i]的子段比 
		if(sumsofar + a > a){	 
			sumsofar += a;
		}
		else{
			sumsofar = a;
		}
		if(sumsofar > maxsum) maxsum = sumsofar;	//update maxsum
	}
	cout<<maxsum;
	
	
	return 0;
} 
