//B.Taxi
//time limit per test3 seconds
//memory limit per test256 megabytes
//inputstandard input
//outputstandard output
//After the lessons n groups of schoolchildren went outsideand decided to visit Polycarpus to celebrate his birthday.We know that the i - th group consists of si friends(1 ≤ si ≤ 4), and they want to go to Polycarpus together.They decided to get there by taxi.Each car can carry at most four passengers.What minimum number of cars will the children need if all members of each group should ride in the same taxi(but one taxi can take more than one group) ?
//
//Input
//The first line contains integer n(1 ≤ n ≤ 105) — the number of groups of schoolchildren.The second line contains a sequence of integers s1, s2, ..., sn(1 ≤ si ≤ 4).The integers are separated by a space, si is the number of children in the i - th group.
//
//Output
//Print the single number — the minimum number of taxis necessary to drive all children to Polycarpus.

#include<iostream>

using namespace std;
int main()
{
	int N, result = 0, cnt[5] = { 0 };

	cin >> N;
	
	for (int i = 0; i < N; i++)
	{
		int tmp;
		cin >> tmp;
		cnt[tmp]++;
		
	}
	result += cnt[4];

	result += cnt[2] / 2;
	
	result += cnt[3];
	cnt[1] -= cnt[3];

	//if (cnt[3] <= cnt[1])
	//{
	//	result += cnt[3];
	//	cnt[1] -= cnt[3];
	//	cnt[3] = 0;
	//	
	//}
	//else //(cnt[3] > cnt[1])
	//{
	//	//result += cnt[3];

	//	result += cnt[1];
	//	cnt[3] -= cnt[1];
	//	cnt[1] = 0;
	//	result += cnt[3];
	//}
	if (cnt[2] % 2 == 1)
	{
		result += 1;
		/*if(cnt[1]>2)*/
		cnt[1] -= 2;
	}
	if (cnt[1] > 0)
	{
		result += (cnt[1] + 3) / 4;
	}
	

	cout << result;



}