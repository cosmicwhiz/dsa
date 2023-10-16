#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int spaceOpt(vector<int> &prices) {
    int n = prices.size();
    vector<vector<int>> last(2, vector<int>(3, 0)), cur(2, vector<int>(3, 0));
    for (int i=n-1; i>=0; i--) {
        for (int buy=0; buy<=1; buy++) {
            for (int cap=1; cap<=2; cap++) {
                if (buy) cur[buy][cap] = max(-prices[i]+last[0][cap], last[buy][cap]);
                else cur[buy][cap] = max(prices[i]+last[1][cap-1], last[buy][cap]);
            }
        }
        last = cur;
    }
    return last[1][2];
}

int main(void) {
    vector<int> prices {3,3,5,0,0,3,1,4};
    cout << spaceOpt(prices);
}