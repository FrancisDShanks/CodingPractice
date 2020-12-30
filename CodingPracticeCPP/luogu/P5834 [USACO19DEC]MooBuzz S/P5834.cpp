// Author: FrancisDShanks
// Email: tctcdtc@gmail.com

/*
  1  2  m  4  m  m  7  8  m  m  11  m 13 14 m 
# 16 17  m 19 m  m 22 23  m  m  26  m 28 29 m
# count 8 numbers for every 15 numbers
# count nth number is m
# if m is multiply of 15:
# m / 15 * 8 = n
# m = n / 8 * 15
# if m is not multiply of 15:
# only need to count n % 8 more number is ok
# 90 -> 150
# 95 -> 150, count 5 more, 95%15=5
*/

/*
规律是每15个数中有8个数会数到，7个数会跳过，之所以是15的原因是15是3和5的最小公倍数
每15个数就轮回一次
反过来看就是每数8个数，实际数字的增长是15
所以数n个数时，分两种情况
	1. n是8的倍数，则实际数字 m=n/8*15
	   注意这种情况有个bug，最后结果m应该是m=n/8*15-1
	   很明显当n=8，n/8*15=15，此时第8个数还没有数到15，应该是m=0再数8个数，而不是m=15在数8个数
	   
	2. n不是8的倍数，先找到（0，n）区间最大的8的倍数n’
	   对应的m’=n'/8*15,
	   然后在数剩下的n-n'个数，也就是n%8个数，数的时候遵循规则跳过3，5倍数
*/
#include <iostream>
using namespace std;

int main(){
	int n;
	cin>>n;
	
	int m = n / 8 * 15;
	int r = n % 8;
	
	for(;r>0;r--){
		m++;
		while(m%3==0 | m%5==0) m++;
	}
	
	if (n%8==0) m-=1;
	cout<<m;
	
	return 0;
}



