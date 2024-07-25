class Solution {
private:
    unordered_set<char> vol{
        'a','e','i','o','u'
    };
public:
    int atMostK(string& word,int k){
        unordered_map<char,int> m;
        int l = 0, r = 0;
        int res = 0;
        for(;r < word.size(); r++){
            if(vol.find(word[r]) == vol.end()){
                l = r + 1;
                m.clear();
                continue;
            }
            ++m[word[r]];
            while(l <= r && m.size() > k){
                if(--m[word[l]] == 0){
                    m.erase(word[l]);
                }
                l++;
            }
            res += r - l + 1;
        }
        return res;
    }
    int countVowelSubstrings(string word) {
        return atMostK(word,5) - atMostK(word,4);
    }
};