#include <iostream>
#include <vector>
#include <algorithm>

using std::cout;
using std::endl;


//insert sort
//STL vector version 
void insertion_sort(std::vector<int> &v){
	std::vector<int>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		std::vector<int>::iterator key = std::upper_bound(v.begin(),it,*it);
		std::rotate(key,it,it+1);
	}
}

//insert sort
//C++ array version
void insertion_sort(int arr[], int size){
	int tmp,i,j;
	for(i=1;i<size;i++){
		tmp = arr[i];
		j = i-1;
		while(j>=0 && tmp<arr[j]){
			arr[j+1] = arr[j];
			j--;
		}
		arr[j+1] = tmp;
	} 
}

int main(){
	int a[] = {8,2,9,4,6,10,5,3,1,7};
	insertion_sort(a,10);
	for(int i=0;i<10;i++) cout<<a[i];
	
	cout<<endl;
	
	std::vector<int> b = {8,2,9,4,6,10,5,3,1,7};
	insertion_sort(b);
	for(std::vector<int>::iterator it=b.begin();it!=b.end();it++){
		cout<<*it;
	}
	

	return 0;
}

