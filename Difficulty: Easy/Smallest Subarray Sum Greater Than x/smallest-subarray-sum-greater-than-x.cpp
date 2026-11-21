class Solution {
  public:
    int smallestSubWithSum(vector<int>& arr, int x) {
        int n = arr.size();
        int left = 0;
        int currsum = 0;
        int ans = INT_MAX;

        for (int right = 0; right < n; right++) {
            currsum += arr[right];

            while (currsum > x) {
                ans = min(ans, right - left + 1);
                currsum -= arr[left];
                left++;
            }
        }

        return (ans == INT_MAX) ? 0 : ans;
    }
};
