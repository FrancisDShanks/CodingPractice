// Author: FrancisDShanks
// Email: tctcdtc@gmail.com

#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    if(n==0) cout<<"0.00"<<endl;
    else if(n==1) cout<<"1.00"<<endl;
	else if(n==2) cout<<"1.00"<<endl;
	else{
		long long a=1,b=1,c=0;
	    for(int i=3;i<=n;i++){
	        c=a+b;
	        a=b;
	        b=c;
	    }
	    cout<<c<<".00"<<endl;
    }
	return 0;
}
