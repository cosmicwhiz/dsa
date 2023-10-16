#include <iostream>
#include <bits/stdc++.h>

using namespace std;

// Time Complexity: O(n)
// Space Complexity: O(n) + O(n)
int f(int i, vector<int> &nums, vector<int> &dp) {
    if (i < 0) return 0;
    if (dp[i] != -1) return dp[i];

    int pick = nums[i] + f(i-2, nums, dp);
    int notPick = 0 + f(i-1, nums, dp);

    return dp[i] = max(pick, notPick);
}

// space optimized solution O(1)
int robInCircular(vector<int> &nums) {
    int prev1 = 0, prev2 = 0;
    
    for (int i=0; i<nums.size(); i++) {
        int pick = nums[i] + prev2;
        int notPick = prev1;
        prev2 = prev1;
        prev1 = max(pick, notPick);
    }
    int cash1 = prev2;
    prev1 = 0; 
    prev2 = 0;
    
    for (int i=1; i<nums.size(); i++) {
        int pick = nums[i] + prev2;
        int notPick = prev1;
        prev2 = prev1;
        prev1 = max(pick, notPick);
    }
    return max(cash1, prev1);
}

int main(void) {
    vector<int> nums = {1,2,3,7,4,5};
    int size = nums.size();
    vector<int> dp(size, -1);

    // int res = f(size-1, nums, dp);
    // cout << res << endl;
    cout << robInCircular(nums) << endl;
    return 0;
}