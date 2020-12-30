// Author: FrancisDShanks
// Email: tctcdtc@gmail.com

#include <iostream>
using namespace std;

int main(){
	int n;
	cin>>n;
	int a[n][n] = {0};
	
	for(int i=0;i<n;i++){
		a[i][0] = 1;
		a[i][i] = 1;
	}
		
	cout<<"1\n";
	for(int i=1;i<n;i++){
		cout<<"1 ";
		for(int j=1;j<i;j++){
			a[i][j] = a[i-1][j-1] + a[i-1][j];
			cout<<a[i][j]<<" ";
		}
		cout<<"1\n";
	} 
	
	return 0;
}

