// Author: FrancisDShanks
// Email: tctcdtc@gmail.com

#include <iostream>
using namespace std;
int arr[1000001];

void swap(int& a, int& b){
	int tmp=a;a=b;b=tmp;
}



void qsort(int start, int end){
	if(start>=end) return;
	int pivot=arr[start];
	int i=start+1,j=end;
	while(i<=j){
		while(arr[i]<pivot && i<=j) i++;
		while(arr[j]>pivot) j--;
		if(i<=j) {
			int tmp=arr[i];arr[i]=arr[j];arr[j]=tmp;
			i++;j--;
		}
	}
	int tmp=arr[start];arr[start]=arr[j];arr[j]=tmp;
	if(start<j) qsort(start,j-1);
	if(j<end) qsort(j+1,end);
}


int main(){
	int n;
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
	qsort(0,n-1);
	for(int i=0;i<n;i++){
		cout<<arr[i]<<" ";
	}
	return 0;
	}
