def getTime():
    time = input("設定したい時間を入力してください:")
    return time

def main():
    print("タイマーを起動しました")
    time = getTime()
    print("time is %s" % time)




if __name__ == '__main__':
    main()
