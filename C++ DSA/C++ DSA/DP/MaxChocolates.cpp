#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int f(int i, int j1, int j2, int m, int n, vector<vector<int>> &grid, vector<vector<vector<int>>> &dp) {
    if (j1 < 0 || j2 < 0 || j1 >= n || j2 >= n) return -1e8;
    if (i == m-1) {
        if (j1 == j2) return grid[i][j1];
        else return grid[i][j1] + grid[i][j2];
    }
    if (dp[i][j1][j2] != -1) return dp[i][j1][j2];
    
    int value = 0;
    if (j1 == j2) value = grid[i][j1];
    else value = grid[i][j1] + grid[i][j2];
    int maxi = -1e8;
    for (int dj1=-1; dj1<=1; dj1++)
        for (int dj2=-1; dj2<=1; dj2++)
            maxi = max(maxi, f(i+1, j1+dj1, j2+dj2, m, n, grid, dp));
    return dp[i][j1][j2] = value + maxi;
}

int tab(int m, int n, vector<vector<int>> &grid) {
    vector<vector<int>> front(n, vector<int> (n, -1));
    vector<vector<int>> cur(n, vector<int> (n, -1));
    for (int j1=0; j1<n; j1++) {
        for (int j2=0; j2<n; j2++) {
            if (j1 == j2) front[j1][j2] = grid[m-1][j1];
            else front[j1][j2] = grid[m-1][j1] + grid[m-1][j2];
        }
    }
    for (int i=m-2; i>=0; i--) {
        for (int j1=0; j1<n; j1++) {
            for (int j2=0; j2<n; j2++) {
                int value = 0;
                if (j1 == j2) value = grid[i][j1];
                else value = grid[i][j1] + grid[i][j2];
                int maxi = -1e8;
                for (int dj1=-1; dj1<=1; dj1++)
                    for (int dj2=-1; dj2<=1; dj2++)
                        if (j1+dj1 >= 0 && j1+dj1 < n && j2+dj2 >= 0 && j2+dj2 < n)
                            maxi = max(maxi, front[j1+dj1][j2+dj2]);
                cur[j1][j2] = value + maxi;   
            }
        }
        front = cur;
    }
    return front[0][n-1];
}

int main(void) {
    vector<vector<int>> grid {{2,3,1,2},{3,4,2,2},{5,6,3,5}};
    int m = grid.size(), n = grid[0].size();
    vector<vector<vector<int>>> dp(m, vector<vector<int>> (n, vector<int> (n, -1)));
    cout << tab(m, n, grid);
}