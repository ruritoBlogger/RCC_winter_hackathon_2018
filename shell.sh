#!/bin/sh

echo "タイマーを起動しました"
echo -n "一分以上の時間を計測しますか?(y or n):"
read ans
if [ "$ans" = y ]
then 
    echo "1分以上"
elif [ "$ans" = n ]
then
    echo "1分以下"

fi

SECONDS=0

### 時間測定したい処理
sleep 3

time=$SECONDS

echo $time
