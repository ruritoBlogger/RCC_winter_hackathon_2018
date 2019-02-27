import time

def getTime():
    while True:
        n = input("設定したい時間を入力してください:")
        if n.isdigit():
            break
        else:
            print("数字を入力してください\n")
    return n

def main():
    start_time = time.time()
    print("タイマーを起動しました")
    target_time = getTime()
    while True:
        if time.time() - start_time > int(target_time):
            print("設定した時間が経過しました")
            break

if __name__ == '__main__':
    main()
