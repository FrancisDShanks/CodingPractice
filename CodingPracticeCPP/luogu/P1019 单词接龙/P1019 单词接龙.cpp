// Author: FrancisDShanks
// Email: tctcdtc@gmail.com
//题目几个点，（1）重叠取最短的重叠，也就是贪心最大长度。（2）不能包含
#include <bits/stdc++.h>

using namespace std;


int n,f,i,j,length=0;
string word[21];
int used[21]={0};

 //返回a在前b在后接龙重叠的长度
string intersection(string a, string b){
	//i start from 1, because contain is not allowed
	for(i=1;i<min(a.length(),b.length());i++){
		int flag = 1;
		for(j=0;j<i;j++){
			//这里是得到的最短重叠就返回
			if(a[a.length()-i+j]!=b[j]) flag=0;
		}
		if(flag) return i;
	}
	return 0;
}

void dfs(string a, int lengthnow){
	length = max(lengthnow,length);
	for(i=0;i<n;i++){
		if(used[i] >= 2) continue;
		int c = intersection(a, word[i]);
		if(c>0){
			used[i]++;
			dfs(word[i],lengthnow+word[i].length()-c);
			used[i]--;
		}
	}
}

int main(){
	cin>>n;
	
	for(i=0;i<n;i++){
		cin>>word[i];
	}	
	cin>>f;
	
	//run dfs
	dfs(' '+f,1);//给首字符加个‘ ’组成一个初始串，长度为1，拿进去跑dfs
	cout<<length<<endl;

	return 0;
}


