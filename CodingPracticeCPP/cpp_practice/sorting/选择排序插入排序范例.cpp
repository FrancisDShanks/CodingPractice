#include <iostream>
using namespace std;

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

void swap(int &a, int &b){
	int tmp = a;
	a = b;
	b = tmp;
}

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
	int arr1[] = {5,3,1,2,4};
	int arr2[] = {5,3,1,2,4};
	int size = 5;
	
	insertion_sort(arr1,size);
	selection_sort(arr2,size);
	for(int i=0;i<size;i++) cout<<arr1[i]<<" ";
	cout<<endl;
	for(int i=0;i<size;i++) cout<<arr2[i]<<" ";


	return 0;
}

