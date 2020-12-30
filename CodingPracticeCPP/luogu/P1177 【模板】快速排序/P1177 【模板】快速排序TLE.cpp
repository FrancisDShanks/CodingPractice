// Author: FrancisDShanks
// Email: tctcdtc@gmail.com
#include <stdio.h>
using namespace std;
int a[1000001];

void swap(int& a, int& b){
	int tmp=a;a=b;b=tmp;
}

void print_array(int arr[], int start, int end){
	for(int i=start;i<=end;i++){
		printf("%d ",a[i]);
	}
	printf("\n");
}

int partition(int arr[], int start, int end){
	int pivot=arr[start];
	int i=start+1,j=end;
	while(i<=j){
		while(arr[i]<pivot && i<=j) i++;
		while(arr[j]>pivot) j--;
		if(i<=j) swap(arr[i++],arr[j--]);
	}
	swap(arr[start],arr[j]);
	return j;
}


void qsort(int arr[], int start, int end){
	if(start>=end) return;
	int p = partition(arr,start,end);
	qsort(arr,start,p-1);
	qsort(arr,p+1,end);
}


int main(){
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		scanf("%d",&a[i]);
	}
	qsort(a,0,n-1);
	print_array(a,0,n-1);
	return 0;
	}
