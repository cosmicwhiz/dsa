#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int f(int len, vector<int> &costs, vector<int> &dp) {
    if (len <= 0) return 0; 
    if (dp[len] != -1) return dp[len];
    int sales = 0;
    for (int l=1; l<=len; l++) sales = max(sales, costs[l-1] + f(len-l, costs, dp));
    return dp[len] = sales;
}

int main(void) {
    int length = 6;
    vector<int> costs {3,5,6,7,10,12};
    vector<int> dp(length+1, -1);
    cout << f(length, costs, dp);
}