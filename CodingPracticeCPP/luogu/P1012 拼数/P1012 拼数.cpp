// Author: FrancisDShanks
// Email: tctcdtc@gmail.com
/*
	consider all numbers as string is much straight forward.
	define a cmp function,
	input all a[i] to an array, then sort the string array.
*/

#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
	
bool cmp(string& a,string& b){
	string c = a+b;
	string d = b+a;
	return (c<d);
}

int main(){
	int n;
	cin>>n;
	string a[n];
	for(int i=0;i<n;++i){
		cin>>a[i];
	}
	sort(a,a+n,cmp);
	for(int i=n-1;i>=0;--i){
		cout<<a[i];
	}
	cout<<endl;
	return 0;
} 
