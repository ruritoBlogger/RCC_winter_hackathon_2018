def getTime():
    while True:
        time = input("設定したい時間を入力してください:")
        if time.isdigit():
            break
        else:
            print("数字を入力してください\n")
    return time

def main():
    print("タイマーを起動しました")
    time = getTime()
    print("time is %s" % time)




if __name__ == '__main__':
    main()
