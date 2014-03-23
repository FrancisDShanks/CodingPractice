//
//Created on March 23, 2014
//
//@author: Xufan Du
//

class Solution {
public:
    int atoi(const char *str) {
        int num=0;
        int sign=1;
        int i=0;
        int n=strlen(str);
        
        while(str[i]==' '&&i<n) i++;
        
        if(str[i]=='+') i++;
        if(str[i]=='-') {i++;sign=-1;}
        
        while(i<n){
            if(str[i]<'0' || str[i]>'9') break;
            
            if(num>INT_MAX/10 || (num==INT_MAX/10&&(str[i]-'0')>INT_MAX%10)) return sign==-1?INT_MIN:INT_MAX;
            
            num=num*10+str[i]-'0';
            
            i++;
        }
        return num*sign;
    }
};
