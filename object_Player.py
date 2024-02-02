from object_Board import Board

class Player:

    def __init__(color, symbol, color):
        self.symbol = symbol
        self.color = color
        self.num = 2
    
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


