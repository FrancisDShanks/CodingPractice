//1/1+1/2+......1/n求和 
#include <iostream>
using namespace std;

int main(){
	int n = 0;
	double sum = 0;
	while(n<3 || n>1000){
		cout<<"Input n(2<n<1000):";
		cin>>n;
	}
	for(int i=1;i<=n;i++){
		sum = sum + 1 / (double)i;
	}
	//cout<<sum;
	printf("%.2f",sum); 
	
	return 0;
} 
