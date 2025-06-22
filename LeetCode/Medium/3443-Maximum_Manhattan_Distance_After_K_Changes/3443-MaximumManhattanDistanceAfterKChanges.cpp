class Solution {
public:
    int maxDistance(string s, int k) {
        int ans = 0;
        int north = 0, south = 0, east = 0, west = 0;

        for (int i = 0; i < s.size(); i++) {
            switch (s[i]) {
                case 'N':
                    north++;
                    break;
                case 'S':
                    south++;
                    break;
                case 'E':
                    east++;
                    break;
                case 'W':
                    west++;
                    break;
            }

            int conflicts = min(north, south) + min(east, west);

            int max_distance = i + 1;

            if (k < conflicts) max_distance = max_distance - (conflicts * 2) + (k * 2);

            ans = max(ans, max_distance);
        }

        return ans;
    }
};