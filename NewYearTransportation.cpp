#include <iostream>
using namespace std;

int main()
{
	int n, t;
	cin >> n >> t;
	int* a = new int[n-1];
	int start = 0;
	for (int i = 0; i < n-1; i++) cin >> a[i];
	while (start < t - 1) start += a[start];
	cout << ((start == t - 1) ? "YES" : "NO")<< endl;
}