#include <iostream>
#include<cstdio>
#include<cstring>
void solve() {
	string S, T;
	cin >> S >> T;
	int q = 0;
	for (char ch : S) {
		while (q < T.length() && T[q] != ch) {
			++q;
		}
		if (q == T.length()) {
			printf("IMPOSSIBLE");
			return;
		}
		++q;
	}	
	printf("%d", (int)(T.length() - S.length()));

}

int main() {
	int T;
	cin >> T;
	for (int Case = 1; Case <= T; ++Case) {
		printf("Case #%d: ", Case);
		solve();
		putchar('\n');
	}
}
