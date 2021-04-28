#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    string s;
    cin >> s;

    long int sum = 0;
    int cnt = 0;
    for(int i = n-1; i >= 0; i--) {
        if(s[i] - '0' >= 0 && s[i] - '0' <= 9) {
            sum += (s[i] - '0') * pow(10, cnt);
            cnt++;
        } else {
            cnt = 0;
            continue;
        }

    }
    cout << sum << '\n';
    return 0;
}