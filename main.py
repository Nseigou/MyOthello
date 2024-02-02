from numpy import zeros, where, float32, array2string
import random

class Othello:
    #定数 (-1をかけることで黒から白、白から黒へのひっくり返しを表現できる)
    white = 1   
    black = -1
    empty = 0  #置かれていないマス
    edge = 8     # 1辺の個数 
    player = 1  #どっちのターンかを表す　　１が白、-１が黒
    n_white = 2  #白いコマの個数
    n_black = -2  #黒のコマの個数      playerに合わせるためマイナスにする
    n_blank = 60  #空いているマスの個数
    game_flag = False  #ゲームが続くかどうか
    change_flag = False  #一方向以上にひっくり返せる位置に置いているかどうか
    

    #初期化
    def __init__(self):
        self.board = zeros((self.edge,self.edge), dtype=float32) #8×8の要素が全て0の行列
        self.board[3,3] = self.board[4,4] = self.white  #白を配置
        self.board[3,4] = self.board[4,3] = self.black  #黒を配置
        
    
    #盤面の描写
    def draw(self):
        print("\n  1 2 3 4 5 6 7 8")    #盤面生成
        
        for i in range(self.edge):
            temp = []                      #出力を工夫するため1行ずつ取り出すための配列
            temp.append(str(i+1))
            for j in range(self.edge):
                if self.board[i,j] == self.white:  #配列の要素が1なら白丸を描写
                    temp.append("○")
                elif self.board[i,j] == self.black:  #配列の要素が-1なら黒丸を描写
                    temp.append("●")
                else:                                #0なら＋を描写
                    temp .append("+")
            print(" ".join(temp))                   #配列のコンマと[]を消す作業
        print("  1 2 3 4 5 6 7 8")

    #コマがおけるかどうかと置けたらひっくり返す
    def is_valid(self, row, column):

        if self.board[row-1][column-1] != 0:  #すでにコマが置いてある場合
            print("\n-----------------\nここにはすでにコマが置かれています")
            return False

        direction = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)] #置くと決めたマスからどの方向に確認するのか
        

        for dr,dc in direction: #directionの座標要素を順番に取り出す
            temp_white = self.n_white  #一時的に白のコマの数を変化させる                               ###リストや配列は「.copy()」を書かないと参照になって、それ自体が変わってしまう。intやstrにそれはない
            temp_black = self.n_black  #黒
            temp_blank = self.n_blank  #空いているところ
            temp_board = self.board.copy()  #一時的にコマをひっくり返した状態の盤面を作るためのもの
            temp_board[row-1][column-1] = self.player  #一時的にコマを置く
            r = (row-1) + dr  #縦方向にずらす　（－1は実際の配列とユーザーとのギャップの調整）
            c = (column-1) + dc  #横方向
            if (0 <=r<= 7 and 0 <=c<= 7 and self.board[r][c] == -self.player):  #相手のコマがその方向に続いてて、最後に自分のコマがある場合Trueを返す
                while(0 <=r<= 7 and 0 <=c<= 7 and self.board[r][c] == -self.player):
                    temp_board[r][c] = self.player #一時的にひっくり返す
                    temp_white += self.player  #一時的にひっくり返した後の個数調整
                    temp_black += self.player 
                    r += dr 
                    c += dc
                    if (0 <=r<= 7 and 0 <=c<= 7 and self.board[r][c] == self.player):
                        print(row,column)
                        self.board = temp_board   #ひっくり返した状態の盤面に更新
                        self.n_white = temp_white  #コマ数を更新
                        self.n_black = temp_black 
                        self.n_blank = temp_blank
                        self.change_flag = True  #複数方向にひっくり返せることが出来るように導入した
                    
        if self.change_flag:
            if self.player == self.white:  #白の番だったら一時的に白のコマ数を+1、空いているマスを-1
                self.n_blank -= 1
                self.n_white += 1
            else:                          #黒
                self.n_blank -= 1
                self.n_black -= 1   #1方向以上にひっくり返せる場合
            return True
        print("-----------------\nここにはコマが置けません")
        return False

  


    #ひっくり返せるマスがあるかどうかのチェック
    def check(self):
        for row in range(self.edge):     #全てのマスを「コマが置いてない」状態かをチェック
            for column in range(self.edge):
                if self.board[row][column] == 0:    #もしコマが置いてないなら,シュミレーションをしてひっくり返せるマスなのかを判定
                    direction = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)] #置くと決めたマスからどの方向に確認するのか
                    for dr,dc in direction: #directionの座標要素を順番に取り出す
                        r = row + dr  #縦方向にずらす　（－1は実際の配列とユーザーとのギャップの調整）
                        c = column + dc  #横方向
                        if (0 <=r<= 7 and 0 <=c<= 7 and self.board[r][c] == -self.player):  #相手のコマがその方向に続いてて、最後に自分のコマがある場合Trueを返す
                            while(0 <=r<= 7 and 0 <=c<= 7 and self.board[r][c] == -self.player):
                                r += dr 
                                c += dc
                                if (0 <=r<= 7 and 0 <=c<= 7 and self.board[r][c] == self.player):
                                    #print("置ける！")
                                    return True
        #print("置けない")
        return False 




    #入力
    def _input(self):
        while True:
            row = input("-----------------\n縦を指定する数字を入力して下さい：")
            column = input("横を指定する数字を入力して下さい：")
            # row = random.randrange(1,9)
            # column = random.randrange(1,9)
            try:              #intに変換できない文字入力の場合エラーを返す
                row = int(row)
                column = int(column)
                break
            except ValueError:
                print("1～8の数字を入力して下さい")
        
        if not(1<=row<=8 and 1<=column<=8):         #1~8以外の数字の場合、_turn()でもう一度入力させる
            print("-----------------\n正しい値を入力して下さい")
            return False
        else:
            return self.is_valid(row, column)
            


    #ターンの動き全体
    def _turn(self):
        while True:
            if self._input():  #正しくターンが終わったらupdate()へ
                break
            else:
                continue       #正しい入力がされなかったらもう一度入力
        


    

    #勝敗条件
    def win(self):
        if self.n_white == 0:     #白のコマが0個になったら  
            print("----------------------\n")
            self.draw()
            print("\n黒の勝ちです")
            self.game_flag = True
        elif self.n_black == 0:    #黒のコマが0個になったら
            print("----------------------\n")
            self.draw()
            print("\n白の勝ちです")
            self.game_flag = True
        elif self.n_blank == 0:   #全てのマスにコマが置かれたら
            if self.n_white > -(self.n_black):    #白>黒
                print("----------------------\n")
                self.draw()
                print("\n白の勝ちです")
                self.game_flag = True
            elif self.n_white < -(self.n_black):     #白<黒
                print("----------------------\n")
                self.draw()
                print("\n黒の勝ちです")
                self.game_flag = True
            elif self.n_white == -(self.n_black):                             #白=黒
                print("----------------------\n")
                self.draw()
                print("\n引き分けです")
                self.game_flag = True

            print("白：",self.n_white)
            print("黒：",-self.n_black)
            

    #アップデート関数(主にリセットとターン交代)
    def update(self):
        self.player *= -1 #ターン交代
        self.change_flag = False
        print("-----------------")
        self.draw()
        if self.player == self.white:
            print("\n白のターン○")
        else:
            print("\n黒のターン●")


#メイン関数
def main():
    s = Othello()
    s.draw()
    print("\n白：○　　黒：●")
    print("-----------------\n白のターン○")
    while True:
        while True:
            if s.check():  #ひっくり返せるマスが存在している場合
                s._turn()  #プレイヤーがでどこに置くか決める
                break
            else:
                print("コマを置けるマスがありません。あなたの番はパスされます。")
                s.update()  #相手の番にする
        s.win()
        if s.game_flag:   #勝敗が付いたら
            break
        s.update()
    return 0



if __name__ == "__main__":
    main()





#参考
# #チャットgpt
#https://qiita.com/KProgramed/items/b6592b15348adce2a9ea

#制作時間：8時間

#工夫したところ
#コマの数の管理をし、勝敗決定時を判断する際に全探索を避けた
#入力のエラーを導入
#現在の番でコマをひっくり返せるマスがあるかどうかを判定し、ある場合とない場合の処理を書いた。
#現状の盤面やコマの数をコピーすることで、ダミーのもので盤面変化を実験的に実証し、不具合がないことが確認できたらその変化させたダミーを本物に置き換えるという操作を実装。

#やりたいこと
#他のオセロのプログラムから最適化できるところを見つめ直したい