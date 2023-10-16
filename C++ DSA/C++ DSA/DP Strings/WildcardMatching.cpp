#include <iostream>
#include <bits/stdc++.h>

using namespace std;

bool f(int i, int j, string s, string p, vector<vector<int>> &dp) {
    if (i < 0 && j < 0) return true;
    if (i >= 0 && j < 0) return false;
    if (i < 0 && j >= 0) {
        for (int k=0; k<=j; k++) if (p[k] != '*') return false;
        return true;
    }
    if (dp[i][j] != -1) return dp[i][j];
    if (s[i] == p[j] || p[j] == '?') return dp[i][j] = f(i-1, j-1, s, p, dp);
    if (p[j] == '*') return dp[i][j] = f(i-1, j, s, p, dp) or f(i, j-1, s, p, dp);
    return dp[i][j] = false;
}

int spaceOpt(int n, int m, string s, string p) {
    vector<int> prev(m+1, 0), cur(m+1, 0);
    prev[0] = 1;
    int j = 0;
    while (p[j] == '*') {
        prev[j+1] = 1;
        j++;
    }
    for (int i=1; i<=n; i++) {
        for (int j=1; j<=m; j++) {
            if (s[i-1] == p[j-1] || p[j-1] == '?') cur[j] = prev[j-1];
            else if (p[j-1] == '*') cur[j] = prev[j] or cur[j-1];
            else cur[j] = 0;
        }
        prev = cur;
    }
    return prev[m];
}

int main(void) {
    string s = "aa", p = "a";
    int n = s.size(), m = p.size();
    vector<vector<int>> dp(n, vector<int>(m, -1));
    cout << f(n-1, m-1, s, p, dp);
}