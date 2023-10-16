#include <iostream>
#include <bits/stdc++.h>

using namespace std;

string spaceOpt(int n, int m, string text1, string text2) {
    vector<string> prev(m+1, "");
    for (int i=1; i<=n; i++) {
        vector<string> cur(m+1, "");
        for (int j=1; j<=m; j++) {
            if (text1[i-1] == text2[j-1]) cur[j] = prev[j-1] + text1[i-1];
            else {
                if (prev[j].length() < cur[j-1].length()) cur[j] = cur[j-1];
                else cur[j] = prev[j];
            }
        }
        prev = cur;
    }
    return prev[m];
}

int main(void) {
    string text1 = "abcde", text2 = "ace";
    int n = text1.length(), m = text2.length();
    cout << spaceOpt(n, m, text1, text2);
}