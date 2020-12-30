// Author: FrancisDShanks
// Email: tctcdtc@gmail.com

#include <iostream>
#include <queue> 
using namespace std;
//用队列维护一个滑动窗口，大小为m
//维护一个m长度数列的和，窗口滑动时：
//减去队列头，出队列；加上新输入的，入队

int main(){
	int n,m;
	cin>>n>>m;
	queue<int> q;
	int tmp=0,min=0,sum=0;
	for(int i=1;i<=n;i++){
		cin>>tmp;
		if(i<=m){  //长度小于m不用滑动窗口，算第一个sum
			q.push(tmp);
			sum += tmp;
			min = sum;
		}
		else{  //滑动窗口
			sum -= q.front();
			sum += tmp;
			q.pop();
			q.push(tmp);
			if(sum<min) min=sum;
		}
	}
	cout<<min;
	return 0;
}

