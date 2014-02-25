#include<stack>
class Solution {
public:
    bool isValid(string s) {
        stack<char> shown;
        int size=s.size();
        if(size==0) return true;
        if(s[0]==')' || s[0]=='}' || s[0]==']') return false;
        shown.push(s[0]);
        
        for(int i=1;i<size;i++){
            if(s[i]==')' || s[i]=='}' || s[i]==']'){
                //need to consider when the stack is empty
                if(shown.empty()) return false;
				if((s[i]==')'&&shown.top()=='(')||(s[i]=='}'&&shown.top()=='{')||(s[i]==']'&&shown.top()=='[')) shown.pop();
                else return false;
            }
            else{
                shown.push(s[i]);
            }
        }
        
        if(shown.empty()) return true;
        else return false;
    }
};
