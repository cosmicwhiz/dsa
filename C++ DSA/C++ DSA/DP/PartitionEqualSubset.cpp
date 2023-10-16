#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int f(int i, int target, vector<int> &nums, vector<vector<int>> &dp) {
    if (target == 0) return true;
    if (i == 0) return target == nums[0];
    if (dp[i][target] != -1) return dp[i][target];
    bool notPick = f(i-1, target, nums, dp);
    bool pick = false;
    if (nums[i] <= target) pick = f(i-1, target-nums[i], nums, dp);
    return dp[i][target] = pick | notPick;
}

bool tab(int target, int n, vector<int> &nums, vector<vector<bool>> &dp) {
    dp[0][nums[0]] = true;
    for (int i=0; i<n; i++) dp[i][0] = true;
    for (int i=1; i<n; i++) {
        for (int t=1; t<target; t++) {
            bool notPick = dp[i-1][t];
            bool pick = false;
            if (nums[i] <= t) pick = dp[i-1][t-nums[i]];
            dp[i][t] = pick | notPick;
        }
    }
}

int main(void) {
    vector<int> nums {1, 5, 11, 5};
    int total = 0, n = nums.size();
    for (auto n : nums)
        total += n;
    if (total % 2 != 0)
        cout << false;
    else {
        int target = total/2;
        vector<vector<int>> dp(n, vector<int> (target+1, -1));
        cout << f(n-1, target, nums, dp);
    }
}