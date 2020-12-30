// Author: FrancisDShanks
// Email: tctcdtc@gmail.com
//��Ҫ�������������mԶ�������ֵķ�Χn
//��ȻӦ���ü�������

#include<bits/stdc++.h>
using namespace std;
int main(){
	int arr[1000]={0};
	int n,m,tmp;
	scanf("%d %d",&n,&m);
	for(int i=0;i<m;++i){
		scanf("%d",&tmp);
		arr[tmp]+=1;
	}
	for(int i=1;i<=n;++i){
		if(arr[i]==0) continue;
		for(int j=0;j<arr[i];++j){
			printf("%d ",i); 
		} 
	}
	printf("\n");
	return 0;
} 
