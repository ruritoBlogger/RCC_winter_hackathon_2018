import time
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

def get_mode():
    ans = input("分単位もしくは秒単位どちらで計測しますか?(y or n)")
    if ans == "y":
        return True
    elif ans == "n":
        return False

def get_time(mode):
    while True:
        if mode:
            n = input("設定したい時間を入力してください(分):")
        else:
            n = input("設定したい時間を入力してください(秒):")
        if n.isdigit():
            break
        else:
            print("時間を入力してください\n")
    return n

def set_gui():
    root = Tk()
    root.title("キッチンタイマー")
    flame = ttk.Frame(
            root,
            relief = 'ridge',
            borderwidth = 10
            )
    flame.grid()
    # ウインドウに表示するものの設定
    img = Image.open(open('../yukarin.jpg', 'rb'))
    img = ImageTk.PhotoImage(img)

    canvas = Canvas(
        root,  # 親要素をメインウィンドウに設定
        width=500,  # 幅を設定
        height=500  # 高さを設定
        # relief=tk.RIDGE  # 枠線を表示
        # 枠線の幅を設定
    )

    canvas.place(x=0, y=0)  # メインウィンドウ上に配置

    canvas.create_image(  # キャンバス上にイメージを配置
        0,  # x座標
        0,  # y座標
        image=img,  # 配置するイメージオブジェクトを指定
        tag="illust",  # タグで引数を追加する。
        anchor=NW  # 配置の起点となる位置を左上隅に指定
    )

    label1 = ttk.Label(
            flame,
            text="キッチンタイマー",
            background="#ffffff",
            padding=(120,50)
            )
    label1.grid(row=1,column=1)

    label2 = ttk.Label(
            flame,
            text="料理のお供",
            background="#ffffff",
            padding=(120,50)
    )
    label2.grid(row=2,column=1)

    return root

def main():
    # gui起動
    root = set_gui()
    print("タイマーを起動しました")
    # 1分以上かどうか
    mode = get_mode()
    # 計測時間の受け取り
    target_time = float(get_time(mode))
    #計測開始時間の取得
    start_time = time.time()

    if mode:
        target_time *= 60
    tmp = int(float(target_time) - time.time() + start_time)
    tmp2 = tmp + 1
    while True:
        if time.time() - start_time > int(target_time):
            print("設定した時間が経過しました")
            break
        elif tmp != int(float(target_time) - time.time() + start_time) - 0.2 or tmp != int(float(target_time) - time.time() + start_time) + 0.2:
            if tmp != tmp2:
                tmp2 = tmp
                if mode:
                    #if (tmp + 1) / 60 != 0:
                    if (tmp + 1) % 60 > 9:
                        print(str(int((tmp + 1) / 60)) + "分" + str((tmp + 1) % 60) + "秒")
                    else:
                        print(str(int((tmp + 1) / 60)) + "分0" + str((tmp + 1) % 60) + "秒")
                else:
                    if tmp + 1 > 9:
                        print(tmp + 1)
                    else:
                        print("0" + str(tmp + 1))
        tmp = int(float(target_time) - time.time() + start_time)

if __name__ == '__main__':
    main()
