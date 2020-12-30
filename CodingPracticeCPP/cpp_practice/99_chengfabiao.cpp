//99乘法表
#include <iostream>
using namespace std;

int main(){
	for(int i=1;i<10;i++){
		for(int j=i;j<10;j++){
			cout<<i<<'*'<<j<<'='<<i*j<<"\t";
		}
		cout<<endl;
	}
	
	return 0;
}
