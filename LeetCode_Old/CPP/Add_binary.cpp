class Solution {
public:
    string addBinary(string a, string b) {
        if(a=="" || b=="") return a+b;
        int sizea=a.size();
        int sizeb=b.size();
        string c="";
        int carry=0;
        while(sizea>0 && sizeb>0){
            if(a[sizea-1]=='1' && b[sizeb-1]=='1'){
                if (carry==0) c+='0';
                else c+='1';
                carry=1;
            }
            else if(a[sizea-1]=='0' && b[sizeb-1]=='0'){
                if (carry==0) c+='0';
                else c+='1';
                carry=0;
            }
            else{
                if(carry==0){
                    c+='1';
                    carry=0;
                }
                else{
                    c+='0';
                    carry=1;                
                }
            }
            sizea--;
            sizeb--;
        }
        
        if(sizea==0 && sizeb==0){
            if(carry==1) {c+='1';carry=0;}
        }
        else if(sizeb==0){
            while(sizea>0){
                if(carry==0) c+=a[sizea-1];
                else{
                    if(a[sizea-1]=='1'){
                        carry=1;
                        c+='0';
                    }
                    else{
                        c+='1';
                        carry=0;
                    }
                }
                sizea--;
            }
        }
        else{
            while(sizeb>0){
                if(carry==0) c+=b[sizeb-1];
                else{
                    if(b[sizeb-1]=='1'){
                        carry=1;
                        c+='0';
                    }
                    else{
                        c+='1';
                        carry=0;
                    }
                }
                sizeb--;
            }
        }
        if(carry==1) c+='1';
        reverse(c.begin(),c.end());
        return c;
        
    }
};
