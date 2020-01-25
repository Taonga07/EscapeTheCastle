import tkinter
onclick = 0
window = None

class Game_Object():
    def __init__(self, piece, icon, colour, column, row):
        self.icon = icon
        self.colour = colour
        self.piece = piece
        self.row = row
        self.column = column

    def moveto(pos):
        pass
        

class Pawn(Game_Object):
    def __init__(self, icon):
        super().__int__(icon, colour)
        self.piece = 'Pawn'
                 

def on_click(event):
    global window
    global onclick
    global piecetomove
    onclick = onclick+1
    square = event.widget
    bttnclr="white"
    rowNumber = int(square.grid_info()["row"])
    columnNumber  = int(square.grid_info()["column"])
    currentText = square.cget("text")
    try:
        if onclick == 1:
            print('Where would you like to move your', board[rowNumber][columnNumber].piece, 'to?')
            piecetomove = board[rowNumber][columnNumber]
        else:
            newsquare = board[rowNumber][columnNumber]
            print(newsquare)
            move_piece()
            #newsquare = tkinter.Label(window, bg = "grey" if(rowNumber + columnNumber) % 2 else "white", image = tkinter.PhotoImage(file = board[piecetomove.row][piecetomove.column].icon))
            oldsquare = square.config(window, bg = "grey" if(rowNumber + columnNumber) % 2 else "white")
            ##rowlist.append(Game_Object('Pawn', path+'Black_Pawn.gif', 'black', column, row))
            ##newsquare.image = tkinter.PhotoImage(board[piecetomove.row][piecetomove.column].icon)
            moveingpiece.image = board[piecetomove.row][piecetomove.column].icon
            moveingpiece.grid(newsquare)
            onclick = 0
            # class for bourd
    except:
        if onclick == 1:
            print('No piece there, try again')
        else:
            print('an error has ocurred')
        onclick = 0
        raise
#make new event
#called/trigured from main meathod
#trigures itself
#u[date screen
#a list
#put all objects in list
#put everthing in list on screen
#when thing taken minus thing from
def move_piece():
    pass
    #check_Rules()
    #if rules == True:
        #delete space in bourd list
        #add peice to move to bourd list
        #write bourd list to .txt file
        #pass move to next player
    #else:
        #alert that move is not allowed
def check_Rules():
    pass
    #check peice to move
    #check PEICE TO MOVE class
    #if returned true return true else return false
    
def layout_window(window):
    bttnclr="white"
    for rowNumber, rowlist in enumerate(board):
        for columnNumber, columnEntry in enumerate(rowlist):
            try:
                img = tkinter.PhotoImage(file = board[rowNumber][columnNumber].icon)
                square = tkinter.Label(window, bg = bttnclr, image = img)
                square.image = img
            except:
                square = tkinter.Label(window, text = "                 \n\n\n", bg = bttnclr)

            if bttnclr == "white":
                bttnclr = "grey"
            else:
                bttnclr = "white"
            square.grid(row = rowNumber, column = columnNumber)
            square.bind("<Button-1>", on_click)
        if bttnclr == "white":
            bttnclr = "grey"
        else:
            bttnclr = "white"

def create_board(board):
    global squaresToClear
    for row in range(0,8):
        rowlist = []
        for column in range(0,8):
            if row == 0:
                rowlist.append(Game_Object(black_pieces[column], path+icons[column+8], 'black', column, row))
            elif row == 7:
                rowlist.append(Game_Object(white_pieces[column], path+icons[column], 'white', column, row))
            elif row == 6:
                rowlist.append(Game_Object('Pawn', path+'White_Pawn.gif', 'white', column, row))
            elif row == 1:
                rowlist.append(Game_Object('Pawn', path+'Black_Pawn.gif', 'black', column, row))
            else:
                rowlist.append(0)
        board.append(rowlist)

def play_Chess():
    create_board(board)
    window = tkinter.Tk()
    window.title('chess')
    layout_window(window)
    window.tk.call('wm', 'iconphoto', window._w, tkinter.PhotoImage(file= path +'Black_King.gif'))
    window.mainloop()
    return window


def updateFile():
    Game = 0
    try:
        file = open(path + Game +'.txt','r')
        board_state = json.load(file)
        file.close()
    except:
        board_state = []
    if board_state == ' ':
        file = json.load(board)
    else:
        file = json.load(board)
    file.close()
    return board_state
    
    
    
  

path = '/media/barton_hill/THOMAS/Digi@Local/MyCode/Python/4 - Green/Code/Chess_Resources/'
icons = ['White_Rook.gif', 'White_Bishop.gif', 'White_Knight.gif', 'White_Queen.gif', 'White_King.gif', 'White_Knight.gif', 'White_Bishop.gif', 'White_Rook.gif', 'Black_Rook.gif', 'Black_Bishop.gif', 'Black_Knight.gif', 'Black_King.gif', 'Black_Queen.gif', 'Black_Knight.gif', 'Black_Bishop.gif', 'Black_Rook.gif']
gameOver = False
score = 0 
white_pieces = ['Rook', 'Bishop', 'Knight', 'Queen',  'King', 'Knight', 'Bishop', 'Rook'] 
black_pieces = ['Rook', 'Bishop', 'Knight', 'King',  'Queen', 'Knight', 'Bishop', 'Rook']
board = []
piecetomove = 0
targetpiece = 0
piecemove = 0
piece_capture = 0

if __name__ =="__main__":
    window = play_Chess()

                
