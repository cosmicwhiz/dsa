#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int f(int i, int buy, int n, vector<int> &prices, vector<vector<int>> &dp) {
    if (i >= n) return 0;
    if (dp[i][buy] != -1) return -1;
    if (buy) return dp[i][buy] = max(-prices[i]+f(i+1, 0, n, prices, dp), f(i+1, 1, n, prices, dp));
    return dp[i][buy] = max(prices[i]+f(i+2, 1, n, prices, dp), f(i+1, 0, n, prices, dp));
}

int main(void) {
    vector<int> prices {7,1,5,4,3};
    int n = prices.size();
    vector<vector<int>> dp(n, vector<int>(2, -1));
    cout << f(0, 1, n, prices, dp);
}