#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int f(int i, int j, vector<vector<int>> &obstacleGrid, vector<vector<int>> &dp) {
    if (i < 0 || j < 0 || obstacleGrid[i][j] == 1) return 0;
    if (i == 0 && j == 0) return 1;
    if (dp[i][j] != -1) return dp[i][j];

    int up = f(i-1, j, obstacleGrid, dp);
    int left = f(i, j-1, obstacleGrid, dp);
    return dp[i][j] = up + left;
}

int main(void) {
    vector<vector<int>> obstacleGrid {{0,0,0},{0,1,0},{0,0,0},{1,0,0}};
    int m = obstacleGrid.size(), n = obstacleGrid[0].size();
    vector<vector<int>> dp(m, vector<int> (n, -1));
    
    cout << f(m-1, n-1, obstacleGrid, dp);
}