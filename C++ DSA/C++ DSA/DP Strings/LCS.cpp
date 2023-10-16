#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int f(int i1, int i2, string text1, string text2, vector<vector<int>> &dp) {
    if (i1 < 0 || i2 < 0) return 0;
    if (dp[i1][i2] != -1) return dp[i1][i2];
    if (text1[i1] == text2[i2]) return dp[i1][i2] = 1 + f(i1-1, i2-1, text1, text2, dp);
    return dp[i1][i2] = max(f(i1-1, i2, text1, text2, dp), f(i1, i2-1, text1, text2, dp));
}

int spaceOpt(int n, int m, string text1, string text2) {
    vector<int> prev(m+1, 0);
    for (int i=1; i<=n; i++) {
        vector<int> cur(m+1, 0);
        for (int j=1; j<=m; j++) {
            if (text1[i-1] == text2[j-1]) cur[j] = 1 + prev[j-1];
            else cur[j] = max(prev[j], cur[j-1]);
        }
        prev = cur;
    }
    return prev[m];
}

int main(void) {
    string text1 = "abc", text2 = "def";
    int n = text1.length(), m = text2.length();
    vector<vector<int>> dp(n+1, vector<int>(m+1, 0));
    // cout << f(n-1, m-1, text1, text2, dp);
    cout << spaceOpt(n, m, text1, text2);
}