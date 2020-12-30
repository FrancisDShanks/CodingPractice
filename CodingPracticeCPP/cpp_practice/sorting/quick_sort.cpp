#include <bits/stdc++.h>
using namespace std;
int SIZE = 30;

void swap(int& a, int& b ){
    int tmp = a;
    a = b;
    b = tmp;
} 

void print_array(const int a[], int size){
    for(int i=0;i<size;i++) cout<<a[i]<<" ";
    cout<<endl;
}

int partition(int *a, int begin, int end){
    int pivot = a[begin];
	int i = begin+1, j = end;

    while (i <= j){
        while(a[i] < pivot && i <= j) i++;
        while(a[j] > pivot) j--;
        if(i<=j) swap(a[i++],a[j--]);
    }
    swap(a[begin],a[j]);
    return j;
}

void quick_sort(int *a, int begin, int end){
    if(begin<end){
        int p = partition(a, begin, end);
        quick_sort(a, begin, p-1);
        quick_sort(a,p+1,end);
    }
}


int main(){
    int a[SIZE];
    for(int i=0;i<SIZE;i++) a[i]=rand()%(2*SIZE);
    print_array(a,SIZE);
    quick_sort(a,0,SIZE-1);
    print_array(a,SIZE);
    return 0;
}
