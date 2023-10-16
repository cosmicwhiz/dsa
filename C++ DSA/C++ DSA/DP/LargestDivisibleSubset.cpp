#include <iostream>
#include <bits/stdc++.h>

using namespace std;

vector<int> tabulation(vector<int> &nums) {
    int n = nums.size();
    vector<int> dp(n, 1), hash(n);
    hash[0] = 0;
    int res = 1, resInd = 0;
    for (int i=1; i<n; i++) {
        hash[i] = i;
        for (int j=0; j<i; j++) {
            if (nums[i] % nums[j] == 0 || nums[j] % nums[i] == 0) {
                if (dp[j]+1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                    hash[i] = j;
                }
            }
        }
        if (dp[i] > res) {
            res = dp[i];
            resInd = i;
        }
    }
    vector<int> ans;
    while (hash[resInd] != resInd) {
        ans.push_back(nums[resInd]);
        resInd = hash[resInd];
    }
    ans.push_back(nums[resInd]);
    return ans;
}

int main(void) {
    vector<int> nums {5,9,18,54,108,540,90,180,360,720};
    sort(nums.begin(), nums.end());
    for (auto n : tabulation(nums)) cout << n << " ";
}