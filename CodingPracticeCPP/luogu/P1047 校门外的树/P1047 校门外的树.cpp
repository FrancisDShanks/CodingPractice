// Author: FrancisDShanks
// Email: tctcdtc@gmail.com

#include <iostream>
using namespace std;

int main(){
	int l,m;
	int a,b;
	int t=0;
	cin>>l>>m;
	bool arr[l+1]={0};
	for(int i=0;i<m;i++){
		cin>>a>>b;
		for(int j=a;j<=b;j++){
			if(!arr[j]) t++;
			arr[j] = true;
		}
	}
	
	cout<<l+1-t<<endl;

	return 0;
}


