#include<iostream>

using namespace std;
void move(int n, int from, int to)
{
	cout << n << "을 " << from << "에서 " << to << "로 이동" << endl;
}

void hanoi(int n, int from, int temp, int to)
{
	if (n == 1)
	{
		move(n, from, to);
		return;
	}
	hanoi(n - 1, from, to, temp);
	move(n, from, to);
	hanoi(n - 1, temp, from, to);
}
int main()
{
	hanoi(3, 1, 2, 3);
}