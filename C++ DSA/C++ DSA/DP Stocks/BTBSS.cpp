#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(void) {
    vector<int> prices {7,1,5,3,6,4};
    int n = prices.size();
    int profit = 0, curMin = prices[0];
    for (int i=1; i<n; i++) {
        profit = max(profit, prices[i]-curMin);
        curMin = min(curMin, prices[i]);
    }
    cout << profit;
}