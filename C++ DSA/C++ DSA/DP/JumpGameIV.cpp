#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int f(int i, int prev, int n, vector<int> &arr, vector<vector<int>> &dp) {
    if (i >= n-1) return 0;
    if (i < 0) return 1e9;
}

int test(vector<int> &path) {
    cout << path[0];
}

int main(void) {
    vector<int> arr {7,6,9,6,9,6,9,7};
    // int n = arr.size();
    // vector<vector<int>> dp(n, vector<int>(n, -1));
    // cout << f(0, 0, n, arr, dp);
    vector<int> path;
    path.push_back(4);
    test(path);
}