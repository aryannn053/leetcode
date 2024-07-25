class Solution {
public:
    bool digitCount(string num) {
        unordered_map<char, int> countMap;

        for (char c : num) {
            countMap[c]++;
        }

        for (int i = 0; i < num.size(); ++i) {
            int x = countMap['0' + i];
            int y = num[i] - '0';

            if (x != y) {
                return false;
            }
        }

        return true;  
    }
};