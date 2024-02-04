from object_Board import Board
from object_Player import Player

class GameMaster:
    def __init__(self):
        self.player1 = Player(1, "白", "○")
        self.player2 = Player(-1, "黒", "●")
        self.board = Board(self.player1, self.player2)
        self.player = self.player1
        self.game_flag = False


    #ひっくり返したことによるコマ数の変化を相手に反映させる
    def ajust(self):
        if self.player == self.player1:
            self.player2.num -= self.player.temp_change
            self.player.temp_change = 0
        else:
            self.player1.num -= self.player.temp_change
            self.player.temp_change = 0

    
    #アップデート関数(主にリセットとターン交代)
    def update(self):
        self.player.change_flag = False    
        if self.player == self.player1:
            self.player = self.player2
        else:
            self.player = self.player1

        print("-----------------")
        self.board.draw()
        print("\n{}のターン{}".format(self.player.color,self.player.mark))


    #勝敗条件
    def isWin(self):
        if self.player1.num == 0 or self.player2.num == 0 or self.board.blank == 0:     #白のコマが0個になったら  
            print("----------------------\n")
            self.board.draw()
            if self.player1.num > self.player2.num:
                print("\n{}の勝ちです".format(self.player1.color))
            elif self.player1.num < self.player2.num:
                print("\n{}の勝ちです".format(self.player2.color))
            else:
                print("\n引き分けです")
            self.game_flag = True
        

            print("白：",self.player1.num)
            print("黒：",self.player2.num)

    


    def gamestart(self):
        
        self.board.draw()
        print("\n白：○　　黒：●")
        print("-----------------\n{}のターン{}".format(self.player.color, self.player.mark))
        while True:
            while True:
                if self.board.check(self.player):  #ひっくり返せるマスが存在している場合
                    while True:
                        if self.player.is_valid(self.board):  
                            self.ajust()
                            break
                        else:
                            continue
                    break
                else:
                    print("コマを置けるマスがありません。あなたの番はパスされます。")
                    self.update()  #相手の番にする
            self.isWin()
            if self.game_flag:   #勝敗が付いたら
                break
            self.update()

        
