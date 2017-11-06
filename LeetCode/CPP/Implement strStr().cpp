//
//Created on March 23, 2014
//
//@author: Xufan Du
//
class Solution {
public:
    //brute force O(m*n)
    char *strStr(char *haystack, char *needle) {
        if(!(*needle)) return haystack;
        char *p1;
        char *p2=needle;
        //p1_end use to check if p1 reaches end while matching p2 
        char *p1_end=haystack;
        for(p2=needle+1;*p2;p2++){
            p1_end++;
        }
        //strat point of each matching
        char *start=haystack;
        for(;*p1_end;p1_end++){
            p2=needle;
            p1=start;
            while(*p1&&*p2&&*p1==*p2){
                p1++;
                p2++;
            }
            //if p2 run out, means find a match
            if(!*p2) return start;
            //else, start at next char
            start++;
            
        }
        return NULL;
    }
};
