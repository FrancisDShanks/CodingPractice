// Author: FrancisDShanks
// Email: tctcdtc@gmail.com

#include <bits/stdc++.h>
using namespace std;

int main(){
	int n;	
	long long pre,cur;
	cin>>n;
	cin>>pre;
	for(int i=1;i<n;i++){
		cin>>cur;
		long long tmp = abs(cur-pre);
		if(tmp<1 || tmp>=n) cout<<"Not jolly"<<endl,exit(0);
		pre = cur;		
	}
	
	cout<<"Jolly"<<endl;
	return 0;
} 
