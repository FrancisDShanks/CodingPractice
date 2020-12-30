// Author: FrancisDShanks
// Email: tctcdtc@gmail.com
#include<bits/stdc++.h>
using namespace std;

struct vol{
	int num;
	int score;
	
	bool operator <(const vol& a) const{
		if(this->score==a.score) return this->num<a.num; //sort number from small to large
		return this->score>a.score; //sort score from large to small
	}
};

int main(){
	int n,m,line;
	cin>>n>>m;
	vol a[n];
	m=m*1.5;
	for(int i=0;i<n;i++) cin>>a[i].num>>a[i].score;
	sort(a,a+n);
	
	line=a[m-1].score;//be careful about the index here:m-1 
	int i=0,cnt=0;
	//run scan once to count the people meet the requirement
	while(i<n){
		if(a[i].score>=line){
			i++;
			cnt++;
		}
		else break;
	}
	printf("%d %d\n",line,cnt);
	
	i=0;
	//run scan again to print data
	while(i<n){
		if(a[i].score>=line){
			printf("%d %d\n",a[i].num,a[i].score);
			i++;
		}
		else break;
	}
	return 0;
}
