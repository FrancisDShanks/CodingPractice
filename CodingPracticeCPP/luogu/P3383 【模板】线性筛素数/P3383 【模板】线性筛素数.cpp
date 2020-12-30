// Author: FrancisDShanks
// Email: tctcdtc@gmail.com

#include <bits/stdc++.h>
using namespace std;
//最后用scanf和printf过的
//如果用cin，哪怕加了优化还是TLE

int main(){ 
	int n,q;
	cin>>n>>q;
	int *p;
	bool *v;
	v = new bool[n+1];
	memset(v,false,sizeof(v));
	p = new int[n+1];
	memset(p,0,sizeof(p));
	
	//int p[n]={0};
	//bool v[n]={0};
	int k;
	int cnt=0;
	
	for(int i=2;i<n;i++){
		if(!v[i]) p[cnt++]=i;
		for(int j=0;j<cnt && p[j]*i<=n;j++){
			v[p[j]*i] = true;
			if(i%p[j]==0) break;
		}
	}
	
	for(int i=0;i<q;i++){
		scanf("%d",&k);
		//if(k<1) return 0;
		printf("%d\n",p[k-1]);
	}
	
	return 0;
}
