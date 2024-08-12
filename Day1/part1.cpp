#include <bits/stdc++.h>
using namespace std;

int main()
{
    ifstream file("./Day1/input.txt");
    string line;
    int sum = 0;
    while (getline(file, line))
    {
        int start_dig = 0, end_dig = 0;
        for (int i = 0; i < line.size(); i++)
        {
            if (line[i] >= '0' && line[i] <= '9')
            {
                start_dig = line[i] - '0';
                break;
            }
        }
        for (int i = line.size() - 1; i >= 0; i--)
        {
            if (line[i] >= '0' && line[i] <= '9')
            {
                end_dig = line[i] - '0';
                break;
            }
        }
        sum += start_dig * 10 + end_dig;
    }
    cout << sum << endl;
}