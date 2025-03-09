class Solution {
public:
    int numberOfAlternatingGroups(vector<int>& colors, int k) {
        colors.insert(colors.end(), colors.begin(), colors.begin()+(k-1));

        int cnt = 0;
        int left = 0;

        for (int right = 1; right < colors.size(); right++) {
            if (colors[right] == colors[right-1]) {
                left = right;
            }

            if (right-left+1 >= k) {
                cnt ++;
            }
        }
        return cnt;
    }
};