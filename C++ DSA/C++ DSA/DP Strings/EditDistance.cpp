#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int f(int i, int j, string s, string t, vector<vector<int>> &dp) {
    if (j < 0) return i+1;
    if (i < 0) return j+1;
    if (dp[i][j] != -1) return dp[i][j];
    if (s[i] == t[j]) return dp[i][j] = f(i-1, j-1, s, t, dp);
    return dp[i][j] = 1 + min(f(i, j-1, s, t, dp), min(f(i-1, j-1, s, t, dp), f(i-1, j, s, t, dp)));
}

int spaceOpt(int n, int m, string s, string t) {
    vector<int> prev(m+1, 0), cur(m+1, 0);
    for (int j=0; j<=m; j++) prev[j] = j;
    prev[0] = 0;
    for (int i=1; i<=n; i++) {
        cur[0] = i;
        for (int j=1; j<=m; j++) {
            if (s[i-1] == t[j-1]) cur[j] = prev[j-1];
            else cur[j] = 1 + min(cur[j-1], min(prev[j-1], prev[j]));
        }
        prev = cur;
    }
    return prev[m];
}

int main(void) {
    string s = "intention", t = "execution";
    int n = s.size(), m = t.size();
    cout << spaceOpt(n, m, s, t);
    // vector<vector<int>> dp(n, vector<int>(m, -1));
    // cout << f(n-1, m-1, s, t, dp);
}