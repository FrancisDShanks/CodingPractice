class Solution {
public:
    bool isPalindrome(string s) {
        if(s.empty() || s.size()==1) return true;
		// set two cursors, start from head and rear
        int rear=0;
        int front = s.size()-1;
        
        while(rear<front){
			//if not alpahnumeric, ignore
            if(!isAlphanum(s[rear])){
                rear++;
                continue;
            }
            if(!isAlphanum(s[front])){
                front--;
                continue;
            }
			//compare to cursor
			//if they are different, return false
            if(isSameChar(s[rear],s[front])){
                rear++;
                front--;
            }
            else return false;
        }
		//when two cursors meet, return true
        return true;
    }
    
    bool isAlphanum(char a){
        if( (a>='0'&&a<='9') || (a>='a'&&a<='z') || (a>='A'&&a<='Z')) return true;
        else return false;
    }
    
    bool isSameChar(char a,char b){
        if(a==b) return true;
        if((a>='a'&&a<='z') && (b>='A'&&b<='Z') && (b-a) == ('A'-'a')) return true;
        if((b>='a'&&b<='z') && (a>='A'&&a<='Z') && (a-b) == ('A'-'a')) return true;
        return false;
    }
};
