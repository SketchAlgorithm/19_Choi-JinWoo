#include<iostream>
#include<vector>
#include<string>
using namespace std;
bool answer(string str) {
	vector<char> stack;
	for (int i = 0; i < str.size(); i++) {
		if (str.at(i) == '[' || str.at(i) == '(') {
			stack.push_back(str.at(i));
		}
		else if (str.at(i) == ')') {
			if (stack.empty() || stack.back() != '(')
				return false;
			else 
				stack.pop_back();
		}
		else if (str.at(i) == ']') {
			if (stack.empty() || stack.back() != '[')
				return false;
			else
				stack.pop_back();
		}
	}
	if (stack.empty())
		return true;
	else
		return false;
}
int main() {
	vector<string> v;
	while (true) {
		string str;
		getline(cin, str);
		if (str == ".")
			break;
		else v.push_back(str);
	}
	for (int i = 0; i < v.size(); i++)
		cout << (answer(v.at(i)) ? "yes" : "no") << endl;
}