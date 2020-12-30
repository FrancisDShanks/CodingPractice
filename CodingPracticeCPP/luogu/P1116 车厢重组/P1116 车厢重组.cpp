// Author: FrancisDShanks
// Email: tctcdtc@gmail.com

#include<iostream>
using namespace std;
//void pa(int *a,int n){
//	for(int i=0;i<n;i++){
//		cout<<a[i]<<" "; 
//	}
//	cout<<endl; 
//}
int main(){
	int n,cnt=0;
	cin>>n;
	int a[n];
	
	for(int i=0;i<n;i++){
		cin>>a[i];
	}

	for(int i=0;i<n-1;i++){
		int m=0,index=0;
		//this loop is used to find the max number in range [0,n-i)
		for(int j=0;j<n-i;j++){
			if(a[j]>m) m=a[j],index=j;
		}
		
		//than swap the max number to place n-i
		//one step by one step and record all swaps
		for(int j=index;j<n-i-1;j++){
			int tmp=a[j];
			a[j]=a[j+1];
			a[j+1]=tmp;
			cnt++;
			}

		}
	
	cout<<cnt;
	return 0;
}
