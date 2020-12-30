// Author: FrancisDShanks
// Email: tctcdtc@gmail.com

//一定要注意题目问的是“其中有多少个数，恰好等于集合中另外两个（不同的）数之和？”
//也就是说1+4=5和2+3=5只算一个，不是问多少组合，是问有多少个5这样的数。。。。

//用两个集合一个拿来查找logn,一个拿来去重（只存一次 & 只存在一个同样的）
//时间复杂度是O(n^2 * logn)

#include <iostream>
#include <set>
using namespace std;

int main(){
	int n,i,j,tmp;

	cin>>n;
	int a[n]={};
	set<int> f; //find sum
	set<int> d; //check duplicate
	
	for(i=0;i<n;i++){
		cin>>a[i];
		f.insert(a[i]);
	}
	
	for(i=0;i<n;i++){
		for(j=i+1;j<n;j++){
			tmp = a[i]+a[j];
			//if(f.find(tmp)!=f.end() && d.find(tmp)==d.end()){ 利用set性质这里可以不判断tmp是否在d里面
			if(f.find(tmp)!=f.end()){
				d.insert(tmp);
			}
			
		}
	}
	cout<<d.size();
	return 0;
}

