#include <iostream>
#include <bits/stdc++.h>

using namespace std;

// Time Complexity: O(N*4)*3
// Space Complexity: O(N) + O(4*N)
int f(int day, int i, vector<vector<int>> &points, vector<vector<int>> &dp) {
    if (day < 0) return 0;
    if (dp[day][i] != -1) return dp[day][i];

    int maxMerit = 0;
    for (int j=0; j<3; j++) {
        if (j != i) {
            int merit = points[day][j] + f(day-1, j, points, dp);
            maxMerit = max(maxMerit, merit);
        }
    }
    return dp[day][i] = maxMerit;
}

// tabulation approach reduces call stack space 
int merit(int n, vector<vector<int>> &points) {
    vector<vector<int>> dp(n, vector<int> (3, -1));
    dp[0][0] = max(points[0][1], points[0][2]);
    dp[0][1] = max(points[0][0], points[0][2]);
    dp[0][2] = max(points[0][0], points[0][1]);

    for (int i=1; i<n-1; i++) {
        dp[i][0] = max(points[i][1]+dp[i-1][1], points[i][2]+dp[i-1][2]);
        dp[i][1] = max(points[i][0]+dp[i-1][0], points[i][2]+dp[i-1][2]);
        dp[i][2] = max(points[i][0]+dp[i-1][0], points[i][1]+dp[i-1][1]);
    }
    int firstCheck = max(points[n-1][0]+dp[n-2][0], points[n-1][1]+dp[n-2][1]);
    return max(firstCheck, points[n-1][2]+dp[n-2][2]);
}

// Space Complexity: O(4) Highly Optimized
int meritIIApproach(int n, vector<vector<int>> &points) {
    vector<int> dp(4, 0);
    dp[0] = max(points[0][1], points[0][2]);
    dp[1] = max(points[0][0], points[0][2]);
    dp[2] = max(points[0][0], points[0][1]);
    dp[3] = max(points[0][0], max(points[0][1], points[0][2]));

    for (int day=1; day<n; day++) {
        vector<int> temp(4, 0);
        for (int last=0; last<4; last++) {
            temp[last] = 0;
            for (int task=0; task<3; task++) {
                if (task != last)
                    temp[last] = max(temp[last], points[day][task]+dp[task]);
            }
        }
        dp = temp;
    }
    return dp[3];
}

int main(void) {
    vector<vector<int>> points = {{10, 40, 70}, {20, 50, 80}, {30, 60, 90}};
    int size = points.size();
    vector<vector<int>> dp(size, vector<int> (4, -1));
    cout << meritIIApproach(size, points) << endl;
    return 0;
}