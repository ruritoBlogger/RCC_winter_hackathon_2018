#include<iostream>
#include<string>
#include<time.h>
using namespace std;

bool get_mode()
{
    string ans;
    while(1)
    {
        cout << "分単位もしくは秒単位どちらで計測しますか(y or n)";
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

double get_time(bool mode)
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
            n = std::stod(tmp);
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
    bool isMiniteMode = get_mode();
    double target_time = get_time(isMiniteMode);
    double start_time = clock();
    if(isMiniteMode)
    {
        target_time *= 60;
    }
    int tmp = (clock() - start_time)/CLOCKS_PER_SEC;
    while(1)
    {
        
        if(tmp != int( (clock() - start_time)/CLOCKS_PER_SEC ))
        {
            cout << target_time - tmp - 1 << endl;
            tmp = int( (clock() - start_time)/CLOCKS_PER_SEC );
            
            if((clock() - start_time)/CLOCKS_PER_SEC > target_time)
            {
                break;
            }
        }
    }
    return 1;
}
