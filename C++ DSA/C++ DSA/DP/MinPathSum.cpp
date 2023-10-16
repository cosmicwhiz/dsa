#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int f(int i, int j, vector<vector<int>> &grid, vector<vector<int>> &dp) {
    if (i == 0 && j == 0) return grid[0][0];
    if (dp[i][j] != -1) return dp[i][j];
    int up = INT_MAX, left = INT_MAX;
    if (i > 0) up = f(i-1, j, grid, dp);
    if (j > 0) left = f(i, j-1, grid, dp);
    return dp[i][j] = grid[i][j] + min(up, left);
}

int main(void) {
    vector<vector<int>> grid {{1,3,1},{1,5,1},{4,2,1}};
    int m = grid.size(), n = grid[0].size();
    vector<vector<int>> dp(m, vector<int> (n, -1));
    cout << f(m-1, n-1, grid, dp);
}