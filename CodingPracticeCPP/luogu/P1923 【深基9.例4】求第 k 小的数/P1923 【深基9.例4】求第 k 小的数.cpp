// Author: FrancisDShanks
// Email: tctcdtc@gmail.com

#include<bits/stdc++.h>
using namespace std;
//用优先队列做，TLE
int main(){

	int n,k,tmp;
	cin>>n>>k;
	if(k>=n) return 0;
	k+=1;
	if(k<=n/2){
		priority_queue<int> q;
		for(int i=0;i<n;++i){
			cin>>tmp;
			if(q.size()>=k){
				if(tmp<q.top()){
					q.pop();
					q.push(tmp);
				}
			}
			else{
				q.push(tmp);
			}
		}
		printf("%d\n",q.top());
	}
	else{
		k=n-k+1;
		priority_queue<int,vector<int>,greater<int> > q;
		for(int i=0;i<n;++i){
			cin>>tmp;
			if(q.size()>=k){
				if(tmp>q.top()){
					q.pop();
					q.push(tmp);
				}
			}
			else{
				q.push(tmp);
			}
		}
		printf("%d\n",q.top());	
	}

	return 0;
} 
