#include<iostream>
#include<vector>
#include<string>
#include<set>
using namespace std;
int n, k;
int cnt = 0;
vector<string> word;	//단어들 집합
set<string> result;
void search(int r, int cur, vector<int> visited, string str)
{
	
	visited[cur] = 1;
	str += word[cur];
	/*cout << r << "번째로 " << cur << "을 방문함"<<endl;
	cout << "현재 상황 : ";
	for (int a = 0; a < n; a++)
	{
		cout << visited[a] << " ";
	}
	cout << endl;*/
	
	if (r == k-1)
	{
		result.insert(str);
		return;

	}
	for (int i = 0; i < n; i++)
	{
		if (visited[i] == 1)
			continue;
		search(r + 1, i, visited, str);
	}
}
int main()
{
	
	vector<int> visited;	//단어 방문 여부, 선택된 단어인가
	
	cin >> n;
	cin >> k;
	for (int i = 0; i < n; i++)
	{
		string input;
		cin >> input;
		word.push_back(input);	//단어 입력
		visited.push_back(0);	//아직 아무것도 선택하지 않았기 때문에 0으로 초기화
	}
	
	for (int i = 0; i < n; i++)
	{
		search(0, i, visited, "");
	}
	/*set<string>::iterator it;
	for (it = result.begin(); it != result.end(); it++)
	{
		cout << *it << endl;
	}*/
	cout << result.size();
	return 0;
}