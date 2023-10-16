#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int f(int i, int j, int m, int n, vector<vector<int>> &grid, vector<vector<int>> &moveCost, vector<vector<int>> &dp) {
    if (i == m-1) return grid[i][j];
    if (dp[i][j] != -1) return dp[i][j];

    int num = grid[i][j];
    int minCost = INT_MAX;
    for (int k=0; k<n; k++) {
        int cost = moveCost[num][k] + f(i+1, k, m, n, grid, moveCost, dp);
        minCost = min(cost, minCost);
    }
    return dp[i][j] = num + minCost;
}

int main(void) {
    vector<vector<int>> grid {{5,1,2},{4,0,3}};
    vector<vector<int>> moveCost {{12,10,15},{20,23,8},{21,7,1},{8,1,13},{9,10,25},{5,3,2}};
    int m = grid.size(), n = grid[0].size();
    vector<vector<int>> dp(m, vector<int> (n, -1));
    int minCost = INT_MAX;
    for (int i=0; i<n; i++)
        minCost = min(minCost, f(0, i, m, n, grid, moveCost, dp));
    cout << minCost;
}