// Author: FrancisDShanks
// Email: tctcdtc@gmail.com

#include<bits/stdc++.h>
using namespace std;

struct candidate{
	string votes;
	int index;
};

bool cmp(const candidate& a,const candidate& b){
	if(a.votes.length()!=b.votes.length()){
		return a.votes.length()>b.votes.length();
	}
	int i=0; 
	while(i<a.votes.length()){
		if(a.votes[i]!=b.votes[i]){
			return a.votes[i]>b.votes[i];
		}
		i++; 
	}
	return a.votes[i]>b.votes[i];
}

int main(){
	int n;
	cin>>n;
	candidate s[n];
	for(int i=0;i<n;i++){
		cin>>s[i].votes;
		s[i].index=i+1;
	}
	sort(s,s+n,cmp);
	cout<<s[0].index<<endl;
	cout<<s[0].votes<<endl;
	return 0;
}
