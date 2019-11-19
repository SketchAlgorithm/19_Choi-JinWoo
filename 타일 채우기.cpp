#include <stdio.h>
#include<iostream>
using namespace std;
int main(void) {

	int Dp[31] = {};
	int result[31] = {};
	int K;
	result[0] = 1;
	Dp[2] = 3;
	for (int i = 4; i <= 30; i += 2)
		Dp[i] = 2;

	cin >> K;

	for (int i = 2; i <= K; i += 2) {
		for (int j = 2; j <= i; j += 2) {
			result[i] += Dp[j] * result[i - j];

		}
	}

	printf("%d\n", result[K]);

	return 0;
}
