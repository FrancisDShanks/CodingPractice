//大数加法 
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	string a,b;
	cout<<"Input two number a,b(0<a,b<10^200)"<<endl;
	cin>>a>>b;
	reverse(a.begin(),a.end());
	reverse(b.begin(),b.end());
	int m = (a.length()>b.length())?b.length():a.length();
	
	int s=0,r=0;
	int n1,n2;
	vector<char> c;
	int i = 0;
	for(i=0;i<m;i++){
		n1 = a[i] - '0';
		n2 = b[i] - '0';
		s = n1 + n2 + r;
		r = s/10;
		c.push_back(s%10+'0');
	}
	
	if(b.length()>a.length()) a = b;
		
	for(i;i<a.length();i++){
		n1 = a[i] - '0';
		s = n1 + r;
		r = s/10;
		c.push_back(s%10 + '0');
	}
	
	if(r>0){
		c.push_back(r + '0');
	}
		
		
	
	
	reverse(c.begin(),c.end());
	for(vector<char>::iterator it=c.begin();it!=c.end();it++){
		cout<<*it;
	}

	cout<<endl;
	system("pause");
	return 0;
}
