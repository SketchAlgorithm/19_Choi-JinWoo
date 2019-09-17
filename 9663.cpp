#include<iostream>
#include<vector>
using namespace std;
int chess[15];
int N;
int answer = 0;
bool isPossible(int row)
{
	bool con = true;
	for (int i = 0; i < row; i++)
	{
		if (chess[i] == chess[row] || abs(chess[i] - chess[row]) == abs(i - row))
		{
			con = false;
		}
	}
	return con;
}
void dfs(int row)
{
	if (row == N)
	{
		answer += 1;

	}
	
	else
	{
		for (int col = 0; col < N; col++)
		{
			chess[row] = col;
			if(isPossible(row))
				dfs(row+1);
		}
	}
	
}
int main()
{
	

	cin >> N;
	dfs(0);
	cout << answer;


}