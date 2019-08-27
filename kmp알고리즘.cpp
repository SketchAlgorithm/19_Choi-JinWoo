#include<iostream>
#include<vector>
#define  _CRT_SECURE_NO_WARNINGS

using namespace std;

vector<int> makeTable(string pattern)
{
	int patternSize = pattern.size();
	vector<int> table(patternSize, 0);
	int j = 0;
	for (int i = 1; i < patternSize; i++)
	{
		while (j > 0 && pattern[i] != pattern[j])
		{
			j = table[j - 1];
		}
		if (pattern[i] == pattern[j])
		{
			table[i] = ++j;
		}
	}
	return table;
}
int main(void)
{
	string father, mother;
	cin >> father >> mother;
	string pattern = father + mother;
	//string pattern = "ababcababababcabab";
	vector<int> table = makeTable(pattern);
	
	//for (int i = 0; i < table.size(); i++)
	//{
	//	printf("%d ", table[i]);
	//}
	vector<int> answer;
	int k = table.size();
	answer.push_back(k);
	
	while (true)
	{
		k = table[k - 1];
		if (k == 0)
		{
			break;
		}
		answer.push_back(k);
	}

	for (int i = answer.size()-1; i >=0; i--)
	{
		printf("%d ", answer[i]);
	}
	
	
	return 0;
}