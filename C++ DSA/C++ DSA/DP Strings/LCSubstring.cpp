#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int spaceOpt(int n, int m, string haystack, string needle) {
    vector<int> last(m+1, 0);
    int ind = -1;
    for (int i=n-1; i>=0; i--) {
        vector<int> cur(m+1, 0);
        for (int j=m-1; j>=0; j--) {
            if (haystack[i] == needle[j]) cur[j] = 1 + last[j+1];
            else cur[j] = 0;
            if (cur[j] == m) ind = i;
        }
        last = cur;
    }
    return ind;
}

int main(void) {
    string haystack = "mississipi", needle = "issip";
    int n = haystack.size(), m = needle.size();
    cout << spaceOpt(n, m, haystack, needle);
}