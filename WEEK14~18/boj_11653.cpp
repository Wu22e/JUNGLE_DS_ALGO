#include <iostream>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int num;
    int div = 2;
    cin >> num;
    while(num != 1) {
        if(num % div == 0) {
            num /= div; 
            cout << div <<'\n';
            div = 2;
        } else {
            div++;
        }
    }

    return 0;
}