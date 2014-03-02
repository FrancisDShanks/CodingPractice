//
//Created on March 02, 2014
//
//@author: Xufan Du
//
class Solution {
public:
    int sqrt(int x) {
        if(x<=1) return x;
        long long left = 1;
        long long right = x/2;
        long long mid;
        long long square,nextsquare;
        while(left<=right){
            mid = (left+right)/2;
            square=mid*mid;
            nextsquare=(mid+1)*(mid+1);
            if( square<=x && x<nextsquare) return mid;
            else if(square>x) right=mid-1;
            else left=mid+1;
        }
        return left;
    }
};
