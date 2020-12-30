//n,错排问题
//n封信装入n个信封，全装错的可能方式
//f(n) = (n-1)(f(n-2)+f(n-1))
#include <iostream>
using namespace std;

int main(){
	int n;
	cout<<"Input a positive number N:";
	cin>>n;
	
	int n1=0;
	int n2=1;
	int n3=0;
	int i = 3;
	if(n==2){
		cout<<1;
		return 0;
	}
	while(i<=n){
		n3 = ((i-1)*n1 + (i-1)*n2);
		n1=n2;
		n2=n3;
		i++;
	}
	cout<<n3;
	
	
	
	return 0;
		
} 
