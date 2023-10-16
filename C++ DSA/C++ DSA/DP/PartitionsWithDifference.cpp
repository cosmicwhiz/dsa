#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int f(int i, int target, vector<int> &arr, vector<vector<int>> &dp) {
    if (i == 0) {
        if (target == 0 && arr[i] == 0) return 2;
        if (target == 0 || target == arr[i]) return 1;
        return 0;
    }
    if (dp[i][target] != -1) return dp[i][target];
    int notPick = f(i-1, target, arr, dp);
    int pick = 0;
    if (arr[i] <= target) pick = f(i-1, target-arr[i], arr, dp);
    return dp[i][target] = pick + notPick;
}

int main(void) {
    vector<int> arr {3,1,1,2,1};
    int n = arr.size(), d = 0;
    int total = 0;
    for (auto n : arr) total += n;
    if (total - d < 0 || (total-d)%2 != 0) cout << 0;
    else {
        int target = (total-d)/2;
        vector<vector<int>> dp(n, vector<int>(target+1, -1));
        cout << f(n-1, target, arr, dp);
    }
}