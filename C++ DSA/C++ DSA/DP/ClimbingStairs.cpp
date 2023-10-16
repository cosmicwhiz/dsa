#include <iostream>
#include <bits/stdc++.h>

using namespace std;

// f(n) -> no. of ways to reach n from 0
// Time Complexity: O(N)
// Space Complexity: O(N) + O(N)

int f(int n, vector<int> &dp) {
    if (n == 0) return 1;
    if (n == 1) return 1;
    if (dp[n] != -1) return dp[n];
    return dp[n] = f(n-1, dp) + f(n-2, dp);
}

// Space Complexity: O(N)
int climb(int n, vector<int> &dp) {
    dp[0] = 1;
    dp[1] = 1;
    for (int i=2; i<n+1; i++)
        dp[i] = dp[i-1] + dp[i-2];
    return dp[n];
}

// Space Complexity: O(1)
int climbOpt(int n) {
    int prev1 = 1;
    int prev2 = 1;
    for (int i=2; i<n+1; i++) {
        int temp = prev1;
        prev1 = prev1 + prev2;
        prev2 = temp;
    }
    return prev1;
}

// minCost(i) -> min cost to reach from 0 to ith index

int minCost(int i, vector<int> &cost, vector<int> &dp) {
    if (i < 0) return 0;
    if (dp[i] != -1) return dp[i];

    int first = cost[i] + minCost(i-1, cost, dp);
    int second = cost[i] + minCost(i-2, cost, dp);

    return dp[i] = min(first, second);
}

int minCostII(vector<int> &cost) {
    int size = cost.size();
    int prev2 = cost[0];
    int prev1 = cost[1];
    for (int i=2; i<size; i++) {
        int temp = prev1;
        prev1 = min(cost[i]+prev1, cost[i]+prev2);
        prev2 = temp;
    }
    return prev1;
}

int main(void) {
    vector<int> cost = {10, 15, 20, 0};
    int size = cost.size();
    vector<int> dp(size, -1);
    cout << minCostII(cost);

    return 0;
}