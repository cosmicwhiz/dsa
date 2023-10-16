#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int f(int l, int r, string s, vector<vector<int>> &dp) {
    if (l >= r) return 0;
    if (dp[l][r] != -1) return dp[l][r];
    if (s[l] != s[r]) return 1 + min(f(l+1, r, s, dp), f(l, r-1, s, dp));
    return dp[l][r] = f(l+1, r-1, s, dp);
}

int main(void) {
    string s = "helper";
    int len = s.length();
    vector<vector<int>> dp(len, vector<int>(len, -1));
    cout << f(0, len-1, s, dp);
}