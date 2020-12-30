// Author: FrancisDShanks
// Email: tctcdtc@gmail.com
#include<bits/stdc++.h>
using namespace std;

struct student{
	int id;
	int yw;
	int sx;
	int yy;
	int sum;
	
	bool operator <(const student& s) const{
		if(this->sum != s.sum){
			return this->sum > s.sum;
		}
		else if(this->yw != s.yw){
			return this->yw > s.yw;
		}
		return this->id < s.id;
	} 
};

int main(){
	int n,tmp;
	cin>>n; 
	student s[n];
	for(int i=0;i<n;++i){
		cin>>s[i].yw>>s[i].sx>>s[i].yy;
		s[i].id=i+1;
		s[i].sum=s[i].yw+s[i].sx+s[i].yy;		
	}
	sort(s,s+n);
	for(int i=0;i<5;i++) printf("%d %d\n",s[i].id,s[i].sum);
	return 0;
	}

