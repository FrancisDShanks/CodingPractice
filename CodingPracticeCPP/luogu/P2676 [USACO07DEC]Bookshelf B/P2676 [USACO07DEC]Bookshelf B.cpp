// Author: FrancisDShanks
// Email: tctcdtc@gmail.com

#include<iostream>
#include<algorithm> 
using namespace std;
bool cmp(const int& a,const int& b) {return a>b;}
int main(){
	int n,b;
	cin>>n>>b;
	int a[n];
	for(int i=0;i<n;i++){
		cin>>a[i];
	}
	sort(a,a+n,cmp);
	int cnt=0,i=0;
	while(b>0 && i<n){
		b-=a[i++];
		cnt++;
	} 
	cout<<cnt<<endl;
	return 0;
}
