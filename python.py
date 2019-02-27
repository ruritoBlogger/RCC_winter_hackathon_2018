import time

def get_time():
    while True:
        n = input("設定したい時間を入力してください:")
        if n.isdigit():
            break
        else:
            print("時間を入力してください(秒)\n")
    return n

def main():
    print("タイマーを起動しました")

    # 計測時間の受け取り
    target_time = get_time()
    #計測開始時間の取得
    start_time = time.time()
    tmp = int(float(target_time) - time.time() + start_time)
    tmp2 = tmp + 1
    while True:
        if time.time() - start_time > int(target_time):
            print("設定した時間が経過しました")
            break
        elif tmp != int(float(target_time) - time.time() + start_time) - 0.2 or tmp != int(float(target_time) - time.time() + start_time) + 0.2:
            if tmp != tmp2:
                tmp2 = tmp
                if(tmp + 1 > 9 ):
                    print(tmp + 1)
                else:
                    print("0" + str(tmp + 1))
        tmp = int(float(target_time) - time.time() + start_time)

if __name__ == '__main__':
    main()
