#include <bits/stdc++.h> 
using namespace std;

//input a integer n,
//print out (how many)/all prime not larger than n

//暴力
int isPrime0(const& n){
	int cnt;
	for(int i=2;i<n;i++){
		bool isp=true;
		for(int j=2;j<i;j++){
			if(i%j==0){
				isp=false;
				break;
			}
		}
		if(isp) {
			cnt++;
			//printf("%d ",i);
		}
	}
	return cnt;
}

//暴力的优化,内循环只跑到i开方就停
int isPrime1(const& n){
	int cnt;
	for(int i=2;i<n;i++){
		bool isp=true;
		int bound = (int)(sqrt(i))+1;
		for(int j=2;j<bound;j++){
			if(i%j==0){
				isp=false;
				break;
			}
		}
		if(isp) {
			cnt++;
			//printf("%d ",i);
		}
	}
	return cnt;
}

// Eratosthenes sieve
// 埃氏筛
// O(nloglogn)
int isPrime3(const& n){
	bool isnotp[n+1]={0};
	int cnt=0;
	//int bound = (int)sqrt(n) + 1;
	for(int i=2;i<=n;i++){
		if(isnotp[i]==true) continue;
		cnt+=1;
		for(int j=2*i;j<=n;j+=i){
			isnotp[j]=true;
		}
	}
	return cnt;
}

// 欧拉筛,线性筛
// O(n)
int isPrime4(const& n){
	bool isnotp[n+1];
	int *primes;
	primes= new int[n+1];
	memset(isnotp,false,sizeof(isnotp));
	memset(primes,0,sizeof(primes));
	int cnt=0;
	
	for(int i=2;i<=n;i++){
		if(!isnotp[i]) primes[cnt++]=i; //没被筛过则肯定是素数,记录
		
		for(int j=0;j<cnt;j++){  //只用已记录的素数一起做筛(隐藏一个逻辑就是之和小于i的素数筛)
			if(primes[j]*i>n) break;  //大于n的就不算了
			isnotp[primes[j]*i] = true;  //筛去合数
			if(i%primes[j]==0) break;  //大于最小因子就停止
		}
	}
	return cnt;
}  

int main(){
	int n;
	cin>>n;	
	clock_t start,end;
	
	start=clock();
	cout<<isPrime0(n)<<endl;
	end=clock();
	printf("Algorithm 0 cost: %d ms\n",end-start);

	start=clock();
	cout<<isPrime1(n)<<endl;
	end=clock();
	printf("Algorithm 1 cost: %d ms\n",end-start);
	
	start=clock();
	cout<<isPrime3(n)<<endl;
	end=clock();
	printf("Algorithm 3 cost: %d ms\n",end-start);

	start=clock();
	cout<<isPrime4(n)<<endl;
	end=clock();
	printf("Algorithm 4 cost: %d ms\n",end-start);
	
	return 0;
}
