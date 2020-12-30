//两个输入数的最小公倍数
#include <iostream>
using namespace std;

int main(){
	int m;
	int n;
	cout<<"Input n:";
	cin>>n;
	cout<<"Input m:";
	cin>>m;
	
	int lcm;
	lcm = (n>m)?n:m;
	do{
		if(lcm%n==0 && lcm%m==0){
			cout<<"LCM:"<<lcm;
			break;
		}
		lcm++;
	}while(true);
	
	return 0;
}
