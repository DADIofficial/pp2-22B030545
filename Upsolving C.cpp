#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;
int main(){
int a, l, k = 1, max = 0;
cin >> a;
int b[a];
for(int i = 0; i < a; i++){
	cin >> b[i];
}
for(int i = 0; i < a; i++){
	for(int j = i + 1; j < a; j++){
		l = min(b[i], b[j]);
		for(int m = l; m >= 2; m--){
			if((b[i]/m)*m == b[i] && (b[j]/m)*m == b[j]){
				k = m;
				break;
			}
		}
	if(max < k){
		max = k;
	}
}
}
cout << max;
}
