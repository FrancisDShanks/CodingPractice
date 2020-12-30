//输入数字N，和K。求N转换为K进制是什么
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
	int n;
	int k;
	cout<<"Input a number n:";
	cin>>n;
	
	cout<<"Input a number k:";
	cin>>k;
	
	vector<char> r;
	int d;
	
	while(n>0){
		int t = n%k;
		char c;
		if(t>=0 and t<=9){
			c = t + '0';
		}
		else if(t<=35){
			c = (t - 10) + 'A';
		}
		else{
			cout<<"Can not handle this K!"<<endl;
			return 0;
		}
		r.push_back(c);
		n = n / k;
	}
	
	reverse(r.begin(),r.end());
	//for(vector<char>::iterator it=r.begin(); it!=r.end();it++){
	for(auto it : r){
		//cout<<*it;
		cout<<it;
	}
	
	
	return 0;
}
