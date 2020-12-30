#include <bits/stdc++.h>
using namespace std;

void swap(int *array, int pos_i, int pos_j){
	int tmp = array[pos_i];
	array[pos_i] = array[pos_j];
	array[pos_j] = tmp;
}

int partition(int *array, int begin, int end);

//尾递归优化
void quick_sort_tail(int *array, int begin, int end){
	while(begin < end){
		int r = partition(array, begin, end);
		quick_sort_tail(array, begin, r - 1);
		begin = r + 1;
	}
}

//还可以做的优化是三数取中
int partition(int *array, int begin, int end){
	//随机取pivot
	int rand_location = rand() % (end - begin + 1) + begin;
	int key = array[rand_location];
	swap(array, rand_location, end);

	int i = begin - 1;
	for (int j = begin; j < end; ++j){
		if (array[j] <= key){
			i++;
			swap(array, i, j);
		}
	}
	swap(array, i + 1, end);
	return i + 1;
}


int main(){
	int a[] = {4,7,9,3,8,1,5,2,10,6};

	for(int i = 0; i<10; i++){
		cout<<a[i]<<" ";
	}

	quick_sort_tail(a, 0, 9);
	cout<<"\n";

	for(int i=0;i<10;i++){
		cout<<a[i]<<" ";
	}
}
