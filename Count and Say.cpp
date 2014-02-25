class Solution {
public:
    string countAndSay(int n) {
        string s;
		if(n<=0) return s;
		s="1";

		int count;
		string temp;
		for(int i=2;i<=n;i++){
			temp="";
			count=1;
			for(int j=1;j<s.size();j++){
				if(s[j]==s[j-1]){
					count++;
				}
				else{
					temp+=char(count+48);
					temp+=s[j-1];
					count=1;
				}
			}
			temp+=char(count+48);
			temp+=s[s.size()-1];
			s=temp;
		}
		return s;
    }
};
