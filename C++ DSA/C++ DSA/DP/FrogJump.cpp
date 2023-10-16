#include <iostream>
#include <bits/stdc++.h>

using namespace std;

// f(x) = min energy required to reach from index 0 to index x
int f(int i, vector<int> &heights, vector<int> &dp, int k) {
    if (i == 0) return 0;
    if (dp[i] != -1) return dp[i];

    int minEnergy = INT_MAX;
    for (int j=1; j<=k; j++) {
        if (i-j >= 0) {
            int jump = f(i-j, heights, dp, k) + abs(heights[i]-heights[i-j]);
            minEnergy = min(minEnergy, jump);
        }
    }
    return dp[i] = minEnergy;
}

int kFrogJumps(int k, int n, vector<int> &heights) {
    vector<int> dp(n, -1);
    dp[0] = 0;

    for (int i=1; i<n; i++) {
        set<int> jumps = {};
        for (int j=1; j<=k; j++) {
            if (i-j >= 0)
                jumps.insert(dp[i-j]+abs(heights[i-j]-heights[i]));
        }
        dp[i] = *jumps.begin();
    }
    return dp[n-1];
}

int main(void) {
    vector<int> heights = {10, 20, 30, 10, 20, 40, 10, 20, 50, 20};
    int size = heights.size();
    vector<int> dp(size, -1);
    int k = 4;
    int res = kFrogJumps(k, size, heights); 
    res = f(size-1, heights, dp, k);
    cout << res << endl;

    return 0;
}