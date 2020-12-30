// Author: FrancisDShanks
// Email: tctcdtc@gmail.com

#include <iostream>
using namespace std;

int main(){
	int n;
	cin >> n;
	int arr[n];
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
	
	for(int i=0;i<n;i++){
		int cnt=0;
		for(int j=0;j<i;j++){
			if(arr[j]<arr[i]) cnt++;	
		}
		cout<<cnt<<" ";
	}


	return 0;
}

