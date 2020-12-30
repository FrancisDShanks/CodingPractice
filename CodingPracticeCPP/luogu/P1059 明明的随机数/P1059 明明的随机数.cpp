// Author: FrancisDShanks
// Email: tctcdtc@gmail.com
/*
C++的话用set做比较简单
*/

#include <iostream>
#include <set>
using namespace std;

int main(){
	int n,tmp;
	cin>>n;
	set<int> s;
	for(int i=0;i<n;i++){
		cin>>tmp;
		s.insert(tmp);
	}
	
	cout<<s.size()<<endl;
	set<int>::iterator it;
	for(it=s.begin();it!=s.end();it++){
		cout<<*it<<" ";
	}
	
	return 0;
}
