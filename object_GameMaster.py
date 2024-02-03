from object_Board import Board
from object_Player import Player

class GameMaster:
    def __init__(self,symbol,color):
        player1 = Player(1, "白")
        player2 = Player(-1, "黒")
        board = Board()
    
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

    

    def gamestart():
        



