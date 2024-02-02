from numpy import zeros, where, float32, array2string
import random
from 

class Board:

    def __init__(self):
        self.board = zeros((self.edge,self.edge), dtype=float32) #8×8の要素が全て0の行列
        self.board[3,3] = self.board[4,4] = 1  #白を配置
        self.board[3,4] = self.board[4,3] = -1  #黒を配置



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