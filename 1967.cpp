//#include<iostream>
//#include<vector>
//#include<algorithm>
//using namespace std;
//const int MAX = 10001;
//vector<pair<int, int>> graph[MAX];
//int n;
//int max_node=0;
//int diameter = 0;
//void dfs(int v, int cost, bool visited[]) {
//	if (visited[v])
//		return;
//	visited[v] = true;
//	if (diameter < cost) {
//		max_node = v;
//		diameter = cost;
//	}
//	for (int i = 0; i < graph[v].size(); i++)
//		dfs(graph[v][i].first, graph[v][i].second+cost, visited);
//}
//int main() {
//	
//	
//	cin >> n;
//	for (int i = 0; i < n-1; i++) {
//		int x, y, cost;
//		cin >> x >> y >> cost;
//		graph[x-1].push_back(make_pair(y-1, cost));
//		graph[y-1].push_back(make_pair(x-1, cost));
//	}
//
//	bool visited[MAX] = { false, };
//	dfs(0, 0, visited);
//	for (int i = 0; i < n; i++) {
//		visited[i] = false;
//	}
//
//	dfs(max_node, 0, visited);
//	cout<<diameter;
//}