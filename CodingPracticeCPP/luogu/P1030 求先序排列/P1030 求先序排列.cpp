// Author: FrancisDShanks
// Email: tctcdtc@gmail.com
/*
没有选择构建树，直接通过中序和后序推出的前序
用了递归写法
*/

#include<bits/stdc++.h>
using namespace std;
string pre;

void helper(string mid, string post){
	// node with no children is a leaf node
	if(mid.length()==1){
		pre.push_back(mid[0]);
		return;
	}
	
	string mid_first,mid_second;
	string post_first,post_second;
	
	// root node is last char in post order traversal
	char root=post[post.length()-1];
	// find root in mid traversal, divide it from both sides
	size_t pos = mid.find(root);  
	
	if(pos == 0){  // if no left child
		mid_second = mid.substr(1);
		post_second = post.substr(0,post.length()-1);
	}
	else if(pos == mid.length()-1){  // if no right child
		mid_first = mid.substr(0,pos);
		post_first = post.substr(0,post.length()-1);
	}
	else{
		// divide mid traversal based on position of root node
		mid_first = mid.substr(0,pos);
		mid_second = mid.substr(pos+1);
		
		// divide post traversal based on the same size of mid
		post_first = post.substr(0,pos);
		post_second = post.substr(pos,post.length()-pos-1);
	}
	
	pre.push_back(root);  // record root node for previous traversal
	if(!mid_first.empty()) helper(mid_first,post_first);
	if(!mid_second.empty()) helper(mid_second,post_second);
	return;	
}


int main(){
	string mid,post;
	cin>>mid>>post;
	
	helper(mid,post);
	cout<<pre;
	return 0;
	}

