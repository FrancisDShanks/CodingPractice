// Author: FrancisDShanks
// Email: tctcdtc@gmail.com
#include <iostream>
using namespace std;

int main(){
	int n,tmp,cnt=0;
	cin>>n;
	bool bucket[1000]={0}; // use bool type is enough 
	for(int i=0;i<n;i++){
		cin>>tmp;
		if(!bucket[tmp]) cnt+=1;
		bucket[tmp] = true;
	}
	
	cout<<cnt<<endl;
	for(int i=1;i<1001;i++){
		if(bucket[i]) cout<<i<<" ";
	}
	
	return 0;
}
