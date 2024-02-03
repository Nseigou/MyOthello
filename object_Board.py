from numpy import zeros, where, float32, array2string
import random
class Board:

    def __init__(self, player1: Player,player2: Player):
        self.edge = 8     # 1辺の個数
        self.player1 = player1
        self.player2 = player2
        self.white = player1.symbol
        self.black = player2.symbol
        self.empty = 0  #置かれていないマス
        self.board = zeros((self.edge,self.edge), dtype=float32) #8×8の要素が全て0の行列
        self.board[3,3] = self.board[4,4] = 1  #白を配置
        self.board[3,4] = self.board[4,3] = -1  #黒を配置
        self.player = player1.symbol
        self.blank = 60  #空いているマスの個数




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

    
    