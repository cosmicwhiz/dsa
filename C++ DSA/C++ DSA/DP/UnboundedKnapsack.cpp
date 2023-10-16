#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int f(int i, int w, vector<int> &weight, vector<int> &profit, vector<vector<int>> &dp) {
    if (i == 0) {
        if (weight[i] <= w) return profit[0]*(w/weight[0]);
        return 0;
    }
    if (dp[i][w] != -1) return dp[i][w];
    int notPick = f(i-1, w, weight, profit, dp);
    int pick = 0;
    if (weight[i] <= w) pick = profit[i] + f(i, w-weight[i], weight, profit, dp);
    return dp[i][w] = max(pick, notPick);
}

int spaceOpt(int n, int w, vector<int> &weight, vector<int> &profit) {
    vector<int> prev(w+1, 0);
    for (int j=weight[0]; j<=w; j++) prev[j] = profit[0]*(j/weight[0]);
    for (int i=1; i<n; i++) {
        vector<int> cur(w+1, 0);
        for (int j=0; j<=w; j++) {
            int notPick = prev[j];
            int pick = 0;
            if (weight[i] <= j) pick = profit[i] + cur[j-weight[i]];
            cur[j] = max(pick, notPick);
        }
        prev = cur;
    }
    return prev[w];
}

int main(void) {
    vector<int> profit {6,12};
    vector<int> weight {4,17};
    int n = profit.size();
    int maxWeight = 3;
    vector<vector<int>> dp(n, vector<int>(maxWeight+1, -1));
    // cout << f(n-1, maxWeight, weight, profit, dp);
    cout << spaceOpt(n, maxWeight, weight, profit);
}