#include <bits/stdc++.h>

using namespace std;

int f(int i, int amount, vector<int> &coins, vector<vector<int>> &dp) {
    if (i == 0) {
        if (amount % coins[i]) return 0;
        return 1;
    }
    if (dp[i][amount] != -1) return dp[i][amount];
    int notPick = f(i-1, amount, coins, dp);
    int pick = 0;
    if (coins[i] <= amount) pick = f(i, amount-coins[i], coins, dp);
    return dp[i][amount] = pick + notPick;
}

int tab(int n, int amount, vector<int> &coins) {
    vector<int> prev(amount+1, 0);
    for (int j=0; j<=amount; j++) {
        if (j % coins[0] == 0) prev[j] = j/coins[0];
        else prev[j] = 1e9; 
    }
    for (int i=1; i<n; i++) {
        vector<int> cur(amount+1, 0);
        for (int j=0; j<=amount; j++) {
            int notPick = prev[j];
            int pick = 1e9;
            if (coins[i] <= j) pick = 1 + cur[j-coins[i]];
            cur[j] = min(pick, notPick);
        }
        prev = cur;
    }
    return prev[amount];
}

int main(void) {
    vector<int> coins = {1,6,3,2,8,10};
    int n = coins.size();
    int amount = 50;
    vector<vector<int>> dp(n, vector<int>(amount+1, -1));
    cout << f(n-1, amount, coins, dp);
    // cout << tab(n, amount, coins);
}