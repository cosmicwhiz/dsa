#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int f(int i, int wt, vector<int> &weight, vector<int> &value, vector<vector<int>> &dp) {
    if (i == 0) {
        if (weight[i] <= wt) return value[i];
        return 0;
    }
    if (dp[i][wt] != -1) return dp[i][wt];
    int notPick = f(i-1, wt, weight, value, dp);
    int pick = 0;
    if (weight[i] <= wt)
        pick = value[i] + f(i-1, wt-weight[i], weight, value, dp);
    
    return dp[i][wt] = max(pick, notPick);
}

int tab(int n, int maxWeight, vector<int> &weight, vector<int> &value) {
    vector<int> prev(maxWeight+1, 0);
    for (int j=0; j<=maxWeight; j++) {
        if (j < weight[0]) prev[j] = 0;
        else prev[j] = value[0];
    }
    for (int i=1; i<n; i++) {
        vector<int> cur(maxWeight+1, 0);
        for (int wt=0; wt<=maxWeight; wt++) {
            int notPick = prev[wt];
            int pick = 0;
            if (weight[i] <= wt)
                pick = value[i] + prev[wt-weight[i]];
            
            cur[wt] = max(pick, notPick);
        }
        prev = cur;
    }
    return prev[maxWeight];
}

int main(void) {
    vector<int> weight {1,2,4,5};
    vector<int> value {5,4,8,6};
    int maxWeight = 5;
    int n = weight.size();
    vector<vector<int>> dp(n, vector<int>(maxWeight+1, 0));
    // cout << f(n-1, maxWeight, weight, value, dp);
    cout << tab(n, maxWeight, weight, value);
}