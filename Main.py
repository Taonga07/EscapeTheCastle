import Escape_The_Castle
import tkinter as tk

    
screen = tk.Tk()
screen.title("Welcome")

def begin():
    screen.destroy()
    Escape_The_Castle.run_main_game()
    
instructions = tk.Label(screen, text = '''Helo and Welcome, to the game of escape.
You have been traped in the dungeons of Castle Camlest.
You have escaped. You have no weapons so will have to collect 
them along the way but beware of cheacky ghosts, feice knights
and closing portcullis. 
Press space or the up arrow to jump and collect the swords. 
Press down arrow to slide under an obstacle
other than that good luck
and hope you escape''',font = ('Helvetica', 12))
instructions.pack()

b1 = tk.Button(screen,text="Play_Game",command=begin)
b1.pack()

screen.mainloop()
