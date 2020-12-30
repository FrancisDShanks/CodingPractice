// Author: FrancisDShanks
// Email: tctcdtc@gmail.com

#include<bits/stdc++.h>
using namespace std;

int main(){
	int n;
	cin>>n;
	string in[n];
	
	for(int i=0;i<n;++i){
		cin>>in[i];
	}
	
	vector<char> res;  //result
	vector<char> st;  //stack
	
	if(in[0][2]!='*') st.push_back(in[0][2]);
	if(in[0][1]!='*') st.push_back(in[0][1]);
	res.push_back(in[0][0]);
	
	while(!st.empty()){
		int pos = 0;
		// fetch the top of the stack
		char tmp = st.back();
		st.pop_back();
		// loop to find tmp in array in
		for(int i=1;i<n;i++){
			if(in[i][0] != tmp) continue;
			// found tmp, record the position
			pos = i;
			// put a note here to present this element is 'deleted'
			// don't do "delete element from array" here, it will cost more time
			in[i][0] = '*';
			break;
		}
		//deal with tmp node
		if(in[pos][2]!='*') st.push_back(in[pos][2]);
		if(in[pos][1]!='*') st.push_back(in[pos][1]);
		res.push_back(tmp);		
	}
	
	for(vector<char>::iterator it=res.begin();it!=res.end();++it) printf("%c",*it);
	return 0;
	}

