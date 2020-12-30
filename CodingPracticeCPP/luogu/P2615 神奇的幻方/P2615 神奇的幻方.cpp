// Author: FrancisDShanks
// Email: tctcdtc@gmail.com

#include <iostream>
using namespace std;

int main(){
	int n;
	cin>>n;
	if(n%2==0) return 0;
	
	int a[n+1][n+1]={0};
	a[1][(n+1)/2] = 1;
	
	int x=1,y=(n+1)/2;
	for(int i=2;i<=n*n;i++){
		if(x==1 && y!=n){
			x = n;
			y = y + 1;
			a[x][y] = i;
		}
		else if(x!=1 && y==n){
			x = x-1;
			y = 1;
			a[x][y] = i;
		}
		else if(x==1 && y==n){
			x = x + 1;
			a[x][y] = i;
		}
		else{
			if((y+1)<=n && (x-1)>0 && a[x-1][y+1]==0){
				x = x - 1;
				y = y + 1;
				a[x][y] = i;
			}
			else{
				x = x + 1;
				a[x][y] = i;
			}
		} 
		
	}
	
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			cout<<a[i][j]<<" ";
		}
		cout<<endl;
	}

	return 0;
}

