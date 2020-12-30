// Author: FrancisDShanks
// Email: tctcdtc@gmail.com

#include <iostream>
#include <vector>
using namespace std;

int main(){
	int n;
	cin>>n;
	vector<int> v;
	while(n!=1){
		v.push_back(n);
		if(n%2==0){
			n/=2;
		}
		else{
			n*=3;
			n+=1;
		}
	}
	v.push_back(1);
	
	for(vector<int>::reverse_iterator it=v.rbegin();it!=v.rend();it++){
		cout<<*it<<" ";
	}
	

	return 0;
}

