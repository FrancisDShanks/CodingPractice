// Author: FrancisDShanks
// Email: tctcdtc@gmail.com

#include<iostream>
using namespace std;
int main(){
	int n,m=0,s=1,tmp,pre;
	cin>>n>>pre;
	for(int i=1;i<n;i++){
		cin>>tmp;
		if(pre+1==tmp) s++;
		else{
			if(m<s) m=s;
			s=1;
		}
		pre=tmp;	
	}
	if(m<s) m=s;
	cout<<m;
	return 0;
} 
