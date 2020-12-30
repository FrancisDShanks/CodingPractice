// Author: FrancisDShanks
// Email: tctcdtc@gmail.com

//用快排partition的思路做可以AC
#include<bits/stdc++.h>
using namespace std;
int arr[5000001]; 

void swap(int& a,int& b){
	int s=a;
	a=b;
	b=s;
}

void partition(int arr[], int left, int right, int k){
	int pivot = arr[left];
	int i=left+1,j=right;
	while(i<=j){
		while(arr[i]<pivot and i<=j) ++i;
		while(pivot<arr[j]) --j;
		if(i<=j) swap(arr[i++],arr[j--]);
	}
	swap(arr[left],arr[j]);
	
	if(j==k){
		printf("%d\n",arr[j]);
		exit(0);
	}
	if(k<j) partition(arr, left, j-1, k);
	if(j<k) partition(arr, j+1, right, k);	
}

int main(){
	int n,k;
	scanf("%d %d",&n,&k);
	if(k>=n) return 0;
	for(int i=0;i<n;++i) scanf("%d", &arr[i]);
	partition(arr,0,n-1,k);
	return 0;
} 
