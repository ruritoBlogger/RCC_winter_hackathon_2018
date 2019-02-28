#include<iostream>
#include<string>
#include<time.h>
using namespace std;

bool get_mode()
{
    string ans;
    while(1)
    {
        cout << "一分以上の時間を計測しますか?(y or n)";
        cin >> ans;
        if(ans == "y")
        {
            return true;
        }
        else if(ans == "n")
        {
            return false;
        }
    }
}

int get_time(bool mode)
{
    string tmp;
    int n;
    while(1)
    {
        if(mode)
        {
            cout << "設定したい時間を入力してください(分):";
            cin >> tmp;
        }
        else
        {
            cout << "設定したい時間を入力してください(秒):";
            cin >> tmp;
        }
        try
        {
            n = std::stoi(tmp);
            return n;
        }
        catch(...)
        {
        }
    }
}

int main()
{
    cout << "タイマーを起動しました" << endl;
    bool mode = get_mode();
    int target_time = get_time(mode);
    double start_time = clock();



    return 1;
}
