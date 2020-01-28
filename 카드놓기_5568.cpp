#include<iostream>
#include<vector>
#include<string>
#include<set>
using namespace std;
int n, k;
int cnt = 0;
vector<string> word;	//�ܾ�� ����
set<string> result;
void search(int r, int cur, vector<int> visited, string str)
{
	
	visited[cur] = 1;
	str += word[cur];
	/*cout << r << "��°�� " << cur << "�� �湮��"<<endl;
	cout << "���� ��Ȳ : ";
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
	
	vector<int> visited;	//�ܾ� �湮 ����, ���õ� �ܾ��ΰ�
	
	cin >> n;
	cin >> k;
	for (int i = 0; i < n; i++)
	{
		string input;
		cin >> input;
		word.push_back(input);	//�ܾ� �Է�
		visited.push_back(0);	//���� �ƹ��͵� �������� �ʾұ� ������ 0���� �ʱ�ȭ
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