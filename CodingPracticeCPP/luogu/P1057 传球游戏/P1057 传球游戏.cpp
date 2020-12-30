// Author: FrancisDShanks
// Email: tctcdtc@gmail.com

#include <iostream>
using namespace std;

void print_array(const int a[] , int size){
	for(int i=0;i<size;i++){
		cout<<a[i]<<endl;
		
	}	
}
int main(){

	int a[] = {1,2,3,4,5};
	print_array(a,5);

	return 0;
}

