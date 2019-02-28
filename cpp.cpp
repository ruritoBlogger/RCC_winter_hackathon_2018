#include<iostream>
#include<string>
using namespace std;

bool get_mode()
{
    while(1)
    {
        string ans;
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

int main()
{
    cout << "タイマーを起動しました" << endl;
    bool mode = get_mode();
    cout << mode << endl;







    return 1;
}
