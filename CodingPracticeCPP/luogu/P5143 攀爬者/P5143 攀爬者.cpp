// Author: FrancisDShanks
// Email: tctcdtc@gmail.com

#include<bits/stdc++.h>
using namespace std;

//data struct used to store point 
struct point{
	int x;
	int y;
	int z;
	bool operator < (const point& p) const{
		//sorting depends on z value 
		return this->z < p.z;
	}
};

//calculate two point's Euclidean distance
double point_distance(const point& a, const point& b){
	double tmp = 0;
	tmp += pow(a.x - b.x, 2);	
	tmp += pow(a.y - b.y, 2);
	tmp += pow(a.z - b.z, 2);
	tmp = sqrt(tmp);
	return tmp;
}

int main(){
	int n;
	double s=0;
	cin>>n;
	point p[n];
	for(int i=0;i<n;i++){
		cin>>p[i].x>>p[i].y>>p[i].z;
	}
	sort(p,p+n);
	for(int i=0;i<n-1;++i){
		s += point_distance(p[i],p[i+1]);
	}
	printf("%.3f\n",s);
	return 0;
	}

