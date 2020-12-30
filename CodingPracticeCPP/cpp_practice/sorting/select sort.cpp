#include <iostream>
#include <vector>
#include <algorithm>

using std::cout;
using std::endl;

void swap(int& a, int& b){
	int tmp = a;
	a = b;
	b = tmp;
}

//insert sort
//STL vector version 
void insertsort(std::vector<int> &v){
	std::vector<int>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		std::vector<int>::iterator key = std::upper_bound(v.begin(),it,*it);
		std::rotate(key,it,it+1);
	}
}

//select sort
//C++ array version
void selection_sort(int arr[], int size){
	int i,j,min;
	for(i=0;i<size-1;i++){
		min = i;
		for(j=i+1;j<size;j++){
			if(arr[min] > arr[j]) min = j;
		}
		swap(arr[min],arr[i]);		
	}	
}

int main(){
	int a[] = {8,2,9,4,6,10,5,3,1,7};
	select_sort(a,10);
	for(int i=0;i<10;i++) cout<<a[i];
	
	cout<<endl;
	
	std::vector<int> b = {8,2,9,4,6,10,5,3,1,7};
	insertsort(b);
	for(std::vector<int>::iterator it=b.begin();it!=b.end();it++){
		cout<<*it;
	}
	

	return 0;
}

