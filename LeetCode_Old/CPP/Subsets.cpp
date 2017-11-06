class Solution {
public:
    vector<vector<int> > subsets(vector<int> &S) {
        vector<vector<int>> m;
        vector<int> v;
        sort(S.begin(),S.end());
        int temp;
        int n=pow(2,S.size());
        for(int i=0;i<n;i++){
            temp=i;
            v.clear();
            for(int j=0;j<S.size();j++){
                if(temp%2==1) v.push_back(S[j]);
                temp=temp/2;
            }
            m.push_back(v);
        }
        return m;
    }
};
