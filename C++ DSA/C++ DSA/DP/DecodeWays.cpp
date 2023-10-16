#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int f(int i, int length, string s, vector<int> &dp) {
    if (i >= length-1) return 1;
    if (s[i] == '0') return 0;

    if (dp[i] != -1) return dp[i];

    int first = 0, second = 0;
    if (stoi(s.substr(i, 1)) > 0)
        first = f(i+1, length, s, dp);
    if (stoi(s.substr(i, 2)) <= 26)
        second = f(i+2, length, s, dp);
    return dp[i] = first + second;
}

int main(void) {
    string s = "128346123874";
    int length = s.length();
    vector<int> dp(length, -1);
    cout << f(0, length, s, dp);
    return 0;
}