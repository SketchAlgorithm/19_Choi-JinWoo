#include<iostream>
using namespace std;
unsigned long long int koong(int n)
{
	unsigned long long int* arr = new unsigned long long int[68];
	arr[0] = 1;
	arr[1] = 1;
	arr[2] = 2;
	arr[3] = 4;
	if (n <= 3)
	{
		return arr[n];
	}
	for (int j = 4; j <=n;j++)
	{
		arr[j] = arr[j - 1] + arr[j - 2] + arr[j - 3] + arr[j - 4];
	}
	return arr[n];
}
int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int n;
		cin >> n;
		cout << koong(n)<<endl;
		
	}
	
}