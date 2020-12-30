# Author: FrancisDShanks
# Email: tctcdtc@gmail.com
# AC
# take use of <map> feature
# ordered key - hash value to store appears

#include <iostream>
#include <map>
using namespace std;

int main(){

	int n;
	cin>>n;
	int number;
	map<int, int> m;
	for(int i=0;i<n;i++){
		cin>>number;
		m[number]++;
	}
	
	for(map<int,int>::iterator it=m.begin();it!=m.end();it++){
		cout<<it->first<<" "<<it->second<<endl;
	}

	return 0;
}
}

