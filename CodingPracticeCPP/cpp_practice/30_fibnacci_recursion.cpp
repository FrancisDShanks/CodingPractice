//输出前30个斐波拉契数，要求递归 
#include <iostream>
using namespace std;

const int AMOUNT = 30;
int a[AMOUNT+1];

int fib(int n){
	if(a[n]!=0) return a[n];
	if (!a[n-1]) a[n-1] = fib(n-1);
	if (!a[n-2]) a[n-2] = fib(n-2);
	a[n] = a[n-1] + a[n-2];
	return a[n];
}
	
int main(){
	
	a[1] = 1;
	a[2] = 1;
	for(int i=3;i<=AMOUNT;i++) a[i]=0;
	
	a[AMOUNT] = fib(AMOUNT);
	for(int i=1;i<=AMOUNT;i++){
		cout<<a[i]<<endl;
	}
	
	return 0;
}
