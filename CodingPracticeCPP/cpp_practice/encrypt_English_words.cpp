//英语单词加密
//加密方法，字母后移一位，z变成a
#include <iostream>
#include <string>
using namespace std;

int main(){
	string s;
	cin>>s;
	for(int i=0;i<s.length();i++){
		if(s[i]>='a' && s[i]<='y'){
			s[i] = s[i]+1;
		}	
		else if(s[i]=='z'){
			s[i]='a';
		}
	}
	cout<<s<<endl;
	

	cout<<endl;
	system("pause");
	return 0;
}
