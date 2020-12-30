// Author: FrancisDShanks
// Email: tctcdtc@gmail.com
/*
负进制和正进制的原理是一样的，做除法取余，逆向排列就可以。
需要注意的是余数
余数为正时就是直接取余数，
余数为负的时候，要讲商+1，然后余数=除数-商*被除数，使得余数为正
最后输出结果要注意将9之后的余数转换为大写字母
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;

int main(){
	
	int nn,r;
	cin>>nn>>r;
	vector<int> v;
	int n=nn;  //copy of n
	int d,tmp; // quotient, remainder
	
	while(n!=0){
		d = n/r;
		tmp = n%r;
		if (tmp>=0){
			v.push_back(tmp);
			n = d;
		}
		else{  
		//if remainder is negtive
		//add one to quotient 
		//new remainder(positive) = denominator - numerator * new quotient
			d+=1; 
			tmp = n - (d*r);
			v.push_back(tmp);
			n = d;
		}
	}

	printf("%d=",nn);
	vector<int>::reverse_iterator it;
	for(it=v.rbegin();it!=v.rend();it++){
		//cout<<endl<<*it<<endl;
		if(*it<10) cout<<*it;
		else{
			cout<<(char)('A'+(*it-10));  //change number larger than 9 to Letters
		}
	}
	printf("(base%d)",r);

	return 0;
}
