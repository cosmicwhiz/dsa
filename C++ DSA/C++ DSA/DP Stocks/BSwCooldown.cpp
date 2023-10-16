#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int spaceOpt(vector<int> &prices) {
    int n = prices.size();
    vector<int> last(2, 0), slast(2, 0), cur(2, 0);
    for (int i=n-1; i>=0; i--) {
        for (int buy=1; buy>=0; buy--) {
            if (buy) cur[buy] = max(-prices[i]+last[0], last[buy]);
            else cur[buy] = max(prices[i]+slast[1], last[buy]);
        }
        slast = last;
        last = cur;
    }
    return last[1];
}

int maxProfit(vector<int>& prices) {
    int n = prices.size();
    return spaceOpt(prices);
}

int main(void) {
    vector<int> prices {1,2,3,0,2};
    maxProfit(prices);
}