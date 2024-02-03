from object_Board import Board

class Player:

    def __init__(color, symbol, color):
        self.symbol = symbol
        self.color = color
        self.num = 2
        self.change_flag = False


    
    def _input(self):
        
        row = input("-----------------\n縦を指定する数字を入力して下さい：")
        column = input("横を指定する数字を入力して下さい：")
        # row = random.randrange(1,9)
        # column = random.randrange(1,9)
        try:              #intに変換できない文字入力の場合エラーを返す
            row = int(row)
            column = int(column)
        except ValueError:
            print("1～8の数字を入力して下さい")
        
        if not(1<=row<=8 and 1<=column<=8):         #1~8以外の数字の場合、_turn()でもう一度入力させる
            print("-----------------\n正しい値を入力して下さい")
            return False
        else:
            return (row, column)


    def is_valid(self, row, column, player1: Player, player2: Player, board: Board):
        
        #すでにコマが置いてある場合
        if board[row-1][column-1] != 0:  
            print("\n-----------------\nここにはすでにコマが置かれています")
            return False

        
        #実際にコマを置いてひっくり返せるかどうかの判定
        direction = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)] #置くと決めたマスからどの方向に確認するのか

        for dr,dc in direction: #directionの座標要素を順番に取り出す
            temp_white = player1.num  #一時的に白のコマの数を変化させる                               ###リストや配列は「.copy()」を書かないと参照になって、それ自体が変わってしまう。intやstrにそれはない
            temp_black = player2.num  #黒
            temp_change = 0
            temp_board = board.board.copy()  #一時的にコマをひっくり返した状態の盤面を作るためのもの
            temp_board[row-1][column-1] = self.symbol  #一時的にコマを置く
            r = (row-1) + dr  #縦方向にずらす　（－1は実際の配列とユーザーとのギャップの調整）
            c = (column-1) + dc  #横方向
            if (0 <=r<= 7 and 0 <=c<= 7 and board.board[r][c] == -self.symbol):  #相手のコマがその方向に続いてて、最後に自分のコマがある場合Trueを返す
                while(0 <=r<= 7 and 0 <=c<= 7 and board.board[r][c] == -self.symbol):
                    temp_board[r][c] = self.symbol #一時的にひっくり返す
                    temp_change += 1  #一時的にひっくり返した後の個数調整
                    r += dr 
                    c += dc
                    if (0 <=r<= 7 and 0 <=c<= 7 and board.board[r][c] == self.player):
                        print(row,column)
                        board.board = temp_board   #ひっくり返した状態の盤面に更新
                        self.num += temp_chang  #コマ数を更新.  +1は新たに置いたコマ 
                        self.change_flag = True  #複数方向にひっくり返せることが出来るように導入した
        
        #ひっくり返せるコマがある場合の処理          
        if self.change_flag:
            board.blank -= 1
            self.num += 1
            return temp_change
       
        #ひっくり返せるコマがない場合の処理    
        print("-----------------\nここにはコマが置けません")
        return False

