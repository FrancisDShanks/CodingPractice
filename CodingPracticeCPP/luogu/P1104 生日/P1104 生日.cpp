// Author: FrancisDShanks
// Email: tctcdtc@gmail.com

#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

struct peo{
	string name;
	int y;
	int m;
	int d;
	int index;
	bool operator < (const peo& p) const{
		if(this->y!=p.y) return this->y<p.y;
		if(this->m!=p.m) return this->m<p.m;
		if(this->d!=p.d) return this->d<p.d;
		else return this->index>p.index;
	}
};

int main(){
	int n;
	cin>>n;
	peo p[n];
	for(int i=0;i<n;i++){
		cin>>p[i].name;
		cin>>p[i].y;
		cin>>p[i].m;
		cin>>p[i].d;
		p[i].index=i; 
	}
	sort(p,p+n);
	for(int i=0;i<n;++i) cout<<p[i].name<<endl;
	return 0;
}
