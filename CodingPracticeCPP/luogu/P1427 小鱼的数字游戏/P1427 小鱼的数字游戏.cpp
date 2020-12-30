// Author: FrancisDShanks
// Email: tctcdtc@gmail.com

#include <iostream>
#include <vector>
using namespace std;

int main(){
	int tmp;
	cin>>tmp;
	vector<int> arr;
	while(tmp!=0){
		arr.push_back(tmp);	
		cin>>tmp;	
	}
	vector<int>::reverse_iterator rit;
	for(rit=arr.rbegin();rit!=arr.rend();rit++)
		cout<<*rit<<" ";


	return 0;
}

