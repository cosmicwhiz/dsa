#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int f(int i, int prev, vector<int> &nums, int length, vector<vector<int>> &dp) {
    if (i == length-1) {
        if (prev == -1 || nums[i] > nums[prev]) return 1;
        return 0;
    }
    if (dp[i][prev+1] != -1) return dp[i][prev+1];
    int len = f(i+1, prev, nums, length, dp);
    if (prev == -1 || nums[i] > nums[prev]) {
        len = max(len, 1 + f(i+1, i, nums, length, dp));
    }
    return dp[i][prev+1] = len;
}

int tabulation(vector<int> &nums) {
    int length = nums.size();
    vector<vector<int>> dp(length+1, vector<int>(length+1, 0));
    for (int i=length-1; i>=0; i--) {
        for (int prev=i-1; prev>=-1; prev--) {
            int len = dp[i+1][prev+1];
            if (prev == -1 || nums[i] > nums[prev]) {
                len = max(len, 1 + dp[i+1][i+1]);
            }
            dp[i][prev+1] = len;
        }
    }
    return dp[0][0];
}

int main() {
    vector<int> nums {10,9,2,5,3,7,101,18};
    int length = nums.size();
    int startIndex = 0, prevIndex = -1;
    vector<vector<int>> dp(length, vector<int> (length+1, -1));

    // int ans = f(startIndex, prevIndex, nums, length, dp);
    int ans = tabulation(nums);
    cout << ans;
}