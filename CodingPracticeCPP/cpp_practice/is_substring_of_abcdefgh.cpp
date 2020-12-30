//判断输入字符串是否是"abcdefgh"的子串 
#include <iostream>
#include <string> 
using namespace std;

int main(){
	string str="abcdefgh";
	string s1;
	cout<<"Input a string, try if it is a substring of 'abcdefg'"<<endl;
	cin>>s1;
	size_t pos = str.find(s1);
	if(pos != string::npos){
		cout<<"It is a SubString";
	}
	else{
		cout<<"It is Not a SubString";
	}
	return 0;
} 
