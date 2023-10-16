#include <iostream>
#include <bits/stdc++.h>

using namespace std;

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
    vector<int> arr {12,13,2,9};
    int size = arr.size();
    int target = 0;
    for (auto n : arr)
        target += n;
    vector<vector<bool>> dp(size, vector<bool>(target+1, 0));
    tab(target, size, arr, dp);
    for (int i=target/2; i>=0; i--)
        if (dp[size-1][i]) return target-2*i;
}