#!/bin/sh

InputTime() {
    if [ "$1" = y ]
    then 
        #1分以上
        echo -n "設定したい時間を入力してください(分):"
    elif [ "$1" = n ]
    then
        #1分以下
        echo -n "設定したい時間を入力してください(秒):"
    fi
}

echo "タイマーを起動しました"

# 1分間以上計測するか
while [ 1 ]
do
    echo -n "一分以上の時間を計測しますか?(y or n):"
    read ans

    if test "$ans" = y -o "$ans" = n
    then 
        InputTime $ans 
        break
    else
        echo "yもしくはnを入力してください"
    fi

    # ans初期化
    ans="" 
done

# どれだけの時間計測するか
while [ 1 ]
do
    read target_time

    # 入力された値が数字かどうか判定する
    expr "$target_time" + 1 >/dev/null 2>&1
    if [ $? -lt 2 ]
    then
        echo "great"
        break
    else
        echo "数字を入力してください"
        InputTime $ans
        # target_time初期化
        target_time=""
    fi
done

SECONDS=0

### 時間測定したい処理
sleep 3

time=$SECONDS

echo $time
