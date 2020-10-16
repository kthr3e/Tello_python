import tello    # tello.pyをインポート
from tello_control_ui import TelloUI    # tello_control_ui.pyをインポート

# メイン関数本体
def main():

    # Telloクラスを使って，droneというインスタンス(実体)を作る
    drone = tello.Tello('', 8889) 

    # TelloUIクラスを使って，vplayerというインスタンスを作る
    # 　上記のdroneと，スナップショット保存先フォルダを引数で渡す.
    # 　なので，droneに対する操作はvplayer(TelloUIクラス)の中で行っている
    vplayer = TelloUI(drone,"./img/")    

    # vplayerはTkinterを使ったGUIウィンドウプログラムなので，メインループを回す必要がある
    vplayer.root.mainloop() 

# "python main.py"として実行された時だけ動く様にするおまじない処理
if __name__ == "__main__":
    main()    # メイン関数を実行

