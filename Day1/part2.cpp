#include <bits/stdc++.h>
using namespace std;

int main()
{
    ifstream file("input.txt");
    string line;
    unordered_map<string, int> mp;
    mp = {{"one", 1}, {"two", 2}, {"three", 3}, {"four", 4}, {"five", 5}, {"six", 6}, {"seven", 7}, {"eight", 8}, {"nine", 9}, {"zero", 0}};
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
            else
            {
                string nxtThree, nxtFour, nxtFive;
                if (i + 2 < line.size())
                    nxtThree = line.substr(i, 3);
                if (i + 3 < line.size())
                    nxtFour = line.substr(i, 4);
                if (i + 4 < line.size())
                    nxtFive = line.substr(i, 5);
                if (mp.find(nxtFive) != mp.end())
                {
                    start_dig = mp[nxtFive];
                    break;
                }
                else if (mp.find(nxtFour) != mp.end())
                {
                    start_dig = mp[nxtFour];
                    break;
                }
                else if (mp.find(nxtThree) != mp.end())
                {
                    start_dig = mp[nxtThree];
                    break;
                }
            }
        }
        for (int i = line.size() - 1; i >= 0; i--)
        {
            if (line[i] >= '0' && line[i] <= '9')
            {
                end_dig = line[i] - '0';
                break;
            }
            else
            {
                string beforeThree, beforeFour, beforeFive;
                if (i - 2 >= 0)
                    beforeThree = line.substr(i - 2, 3);
                if (i - 3 >= 0)
                    beforeFour = line.substr(i - 3, 4);
                if (i - 4 >= 0)
                    beforeFive = line.substr(i - 4, 5);
                if (mp.find(beforeFive) != mp.end())
                {
                    end_dig = mp[beforeFive];
                    break;
                }
                else if (mp.find(beforeFour) != mp.end())
                {
                    end_dig = mp[beforeFour];
                    break;
                }
                else if (mp.find(beforeThree) != mp.end())
                {
                    end_dig = mp[beforeThree];
                    break;
                }
            }
        }
        sum += start_dig * 10 + end_dig;
    }
    cout << sum << endl;
}