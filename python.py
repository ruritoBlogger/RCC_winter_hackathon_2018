import time
from tkinter import *
from tkinter import ttk

def get_time():
    while True:
        n = input("設定したい時間を入力してください:")
        if n.isdigit():
            break
        else:
            print("数字を入力してください\n")
    return n

def set_gui():
    root = Tk()
    root.title("キッチンタイマー")
    flame = ttk.Frame(
            root,
            height = 480,
            width = 640,
            relief = 'ridge',
            borderwidth = 10
            )
    flame.grid()

    # ウインドウに表示するものの設定
    label1 = ttk.Label(
            flame,
            text="Hello",
            background="#ffffff",
            width=48,
            padding=(120,50)
            )
    label1.grid()

    return root

def main():
    # GUIの表示
    root = set_gui()
    print("タイマーを起動しました")

    # 計測時間の受け取り
    target_time = get_time()
    #計測開始時間の取得
    start_time = time.time()

    while True:
        if time.time() - start_time > int(target_time):
            print("設定した時間が経過しました")
            break

if __name__ == '__main__':
    main()
