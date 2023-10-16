#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int f(int i, int j, string s, string t, vector<vector<int>> &dp) {
    if (j < 0) return 1;
    if (i < 0) return 0;
    if (dp[i][j] != -1) return dp[i][j];
    if (s[i] == t[j]) return dp[i][j] = f(i-1, j-1, s, t, dp) + f(i-1, j, s, t, dp);
    return dp[i][j] = f(i-1, j, s, t, dp);
}

int tab(int n, int m, string s, string t) {
    vector<vector<int>> dp(n+1, vector<int>(m+1, 0));
    for (int i=0; i<=n; i++) dp[i][0] = 1;
    for (int i=1; i<=n; i++) {
        for (int j=1; j<=m; j++) {
            if (s[i-1] == t[j-1]) dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
            else dp[i][j] = dp[i-1][j];
        }
    }
    return dp[n][m];
}

int spaceOpt(int n, int m, string s, string t) {
    vector<int> prev(m+1, 0);
    prev[0] = 1;
    for (int i=1; i<=n; i++) {
        vector<int> cur(m+1, 0);
        cur[0] = 1;
        for (int j=1; j<=m; j++) {
            if (s[i-1] == t[j-1]) cur[j] = prev[j-1] + prev[j];
            else cur[j] = prev[j];
        }
        prev = cur;
    }
    return prev[m];
}

int main(void) {
    string s = "babgbag", t = "bag";
    int n = s.size(), m = t.size();
    cout << spaceOpt(n, m, s, t);
    // vector<vector<int>> dp(n, vector<int>(m, -1));
    // cout << f(n-1, m-1, s, t, dp);
}