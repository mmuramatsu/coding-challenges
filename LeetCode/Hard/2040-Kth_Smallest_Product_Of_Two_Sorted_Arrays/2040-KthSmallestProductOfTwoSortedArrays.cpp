class Solution {
public:
    std::pair<std::vector<int>, std::vector<int>> split(std::vector<int>& num) {
        std::vector<int> pos;
        std::vector<int> neg;

        for (int i = 0; i < num.size(); i++) {
            if (num[i] < 0) {
                neg.push_back(-num[i]);
            } else {
                pos.push_back(num[i]);
            }
        }

        std::reverse(neg.begin(), neg.end());

        return std::make_pair(pos, neg);
    }

    long long count_products(std::vector<int>& A, std::vector<int>& B, long long m) {
        long long count = 0;
        long long j = B.size() -1;

        for (int num :  A) {
            while (j >= 0 && (long long) num * B[j] > m) {
                j--;
            }

            count += j + 1;
        }

        return count;
    }

    long long kthSmallestProduct(vector<int>& nums1, vector<int>& nums2, long long k) {
        std::vector<int> A1, A2, B1, B2;

        std::pair< std::vector<int>,  std::vector<int>> result = split(nums1);
        A1 = result.first;
        A2 = result.second;

        result = split(nums2);
        B1 = result.first;
        B2 = result.second;

        int negative_count = A1.size() * B2.size() + A2.size() * B1.size();
        int  sign = 1;

        if (k > negative_count) {
            k -= negative_count;
        }
        else {
            k = negative_count - k + 1;
            sign = -1;
            std::swap(B1, B2);
        }

        long long left = 0;
        long long right = static_cast<long long>(pow(10, 10));

        while (left < right) {
            long long mid = (left + right) / 2;

            if (count_products(A1, B1, mid) + count_products(A2, B2, mid) >= k) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return sign * left;
    }
};