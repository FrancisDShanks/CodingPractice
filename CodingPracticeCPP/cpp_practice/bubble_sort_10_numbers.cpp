//十个数字冒泡排序
#include <iostream>
using namespace std;

int main(){
	int a[10];
	for(int i=0;i<10;i++){
		printf("Input %dth number:",i+1);
		cin>>a[i];
	}
	
	cout<<"10 numbers are:"<<endl;
	for(int i=0;i<10;i++){
		cout<<a[i]<<" ";
	}
	cout<<endl;
	
	
	for (int i=0; i<10;i++){
		for(int j=i;j<10;j++){
			if(a[i]>a[j]){
				int tmp = a[j];
				a[j] = a[i];
				a[i] = tmp;
			}
		}
	}
	
	cout<<"10 numbers after sorting are:"<<endl;
	for(int i=0;i<10;i++){
		cout<<a[i]<<" ";
	}
	
	return 0;
}
