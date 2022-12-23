from tkinter import messagebox
import tkinter.messagebox
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Tic Tac Toe")
root.geometry("700x350")
root.configure(bg='turquoise')

Top = Frame(root,
            bg='aquamarine1',
            pady=1,
            width=750,
            height=575,
            relief=RIDGE)
Top.grid(row=0, column=0)

img = ImageTk.PhotoImage(Image.open("tictactoe (4).jpg"))
label = Label(Top, image = img)
label.place(x=50,y=10)

MainFrame = Frame(root,
                  bg='darkgoldenrod',
                  bd=5,
                  width=675,
                  height=300,
                  relief=RIDGE)
#MainFrame.grid(row=1, column=0)
MainFrame.place(x=125, y=125)
#add anything in main frame
BoardFrame = Frame(
  MainFrame,
  bg='MistyRose',
  bd=5,
  width=375,
  height=250,
  padx=1,
  pady=1,
)
BoardFrame.pack()

PlayerX = IntVar()
PlayerO = IntVar()
#set score
PlayerX.set(0)
PlayerO.set(0)

buttons = StringVar()
click = True
count=0

def checker(buttons):
  global click,count
  if buttons["text"] == " " and click == True:
    buttons["text"] = "X"
    l2=Label(Top,font=('arial', 10, 'bold'),
                bg='LavenderBlush',
                fg='dark blue',
                text="PLAYER X",
                bd=5)
    l2.place(x=140,y=210)
    click = False
    count=count+1
    scoreCard()

  elif buttons["text"] == " " and click == False:
    buttons["text"] = "O"
    l1=Label(Top,font=('arial', 10, 'bold'),
                bg='LavenderBlush',
                fg='dark blue',
                text="PLAYER O",
                bd=5)
    l1.place(x=140,y=210)
    click = True
    count=count+1
    scoreCard()

    
#set score card :
def scoreCard():

  if (button1["text"] == button2["text"] == button3["text"] == "X"):
    button1.configure(bg='ivory')
    button2.configure(bg='ivory')
    button3.configure(bg='ivory')
    n = int(PlayerX.get())
    score = (n + 1)
    PlayerX.set(score)
    lbl = Label(Top,
                font=('arial', 12, 'bold'),
                bg='LavenderBlush',
                fg='dark blue',
                text="PLAYER X",
                bd=5)
    lbl.place(x=502, y=225)  #1005-400
    tkinter.messagebox.showinfo("WINNER IS X!!",
                                "YOU HAVE JUST WON THE GAME.....")
 
   
  if (button4["text"] == button5["text"] == button6["text"] == "X"):
    button4.configure(bg='ivory')
    button5.configure(bg='ivory')
    button6.configure(bg='ivory')
    n = int(PlayerX.get())
    score = (n + 1)
    PlayerX.set(score)
    lbl = Label(Top,
                font=('arial', 12, 'bold'),
                bg='LavenderBlush',
                fg='dark blue',
                text="PLAYER X",
                bd=5)
    lbl.place(x=502, y=225)
    tkinter.messagebox.showinfo("WINNER IS X!!",
                                "YOU HAVE JUST WON THE GAME.....")
  
   
  if (button7["text"] == button8["text"] == button9["text"] == "X"):
    button7.configure(bg='ivory')
    button8.configure(bg='ivory')
    button9.configure(bg='ivory')
    n = int(PlayerX.get())
    score = (n + 1)
    PlayerX.set(score)
    lbl = Label(Top,
                font=('arial', 12, 'bold'),
                bg='LavenderBlush',
                fg='dark blue',
                text="PLAYER X",
                bd=5)
    lbl.place(x=502, y=225)
    tkinter.messagebox.showinfo("WINNER IS X!!",
                                "YOU HAVE JUST WON THE GAME.....")
  
   
  if (button1["text"] == button4["text"] == button7["text"] == "X"):
    button1.configure(bg='yellow')
    button4.configure(bg='yellow')
    button7.configure(bg='yellow')
    n = int(PlayerX.get())
    score = (n + 1)
    PlayerX.set(score)
    lbl = Label(Top,
                font=('arial', 12, 'bold'),
                bg='LavenderBlush',
                fg='dark blue',
                text="PLAYER X",
                bd=5)
    lbl.place(x=502, y=225)
    tkinter.messagebox.showinfo("WINNER IS X!!",
                                "YOU HAVE JUST WON THE GAME.....")
 
  if (button2["text"] == button5["text"] == button8["text"] == "X"):
    button2.configure(bg='yellow')
    button5.configure(bg='yellow')
    button8.configure(bg='yellow')
    n = int(PlayerX.get())
    score = (n + 1)
    PlayerX.set(score)
    lbl = Label(Top,
                font=('arial', 12, 'bold'),
                bg='LavenderBlush',
                fg='dark blue',
                text="PLAYER X",
                bd=5)
    lbl.place(x=502, y=225)
    tkinter.messagebox.showinfo("WINNER IS X!!",
                                "YOU HAVE JUST WON THE GAME.....")
   
  if (button3["text"] == button6["text"] == button9["text"] == "X"):
    button3.configure(bg='yellow')
    button6.configure(bg='yellow')
    button9.configure(bg='yellow')
    n = int(PlayerX.get())
    score = (n + 1)
    PlayerX.set(score)
    lbl = Label(Top,
                font=('arial', 12, 'bold'),
                bg='LavenderBlush',
                fg='dark blue',
                text="PLAYER X",
                bd=5)
    lbl.place(x=502, y=225)
    tkinter.messagebox.showinfo("WINNER IS X!!",
                                "YOU HAVE JUST WON THE GAME.....")
  
  if (button1["text"] == button5["text"] == button9["text"] == "X"):
    button1.configure(bg='Red')
    button5.configure(bg='Red')
    button9.configure(bg='Red')
    n = int(PlayerX.get())
    score = (n + 1)
    PlayerX.set(score)
    lbl = Label(Top,
                font=('arial', 12, 'bold'),
                bg='LavenderBlush',
                fg='dark blue',
                text="PLAYER X",
                bd=5)
    lbl.place(x=502, y=225)
    tkinter.messagebox.showinfo("WINNER IS X!!",
                                "YOU HAVE JUST WON THE GAME.....")
   
  if (button3["text"] == button5["text"] == button7["text"] == "X"):
    button3.configure(bg='Red')
    button5.configure(bg='Red')
    button7.configure(bg='Red')
    n = int(PlayerX.get())
    score = (n + 1)
    PlayerX.set(score)
    lbl = Label(Top,
                font=('arial', 12, 'bold'),
                bg='LavenderBlush',
                fg='dark blue',
                text="PLAYER X",
                bd=5)
    lbl.place(x=502, y=225)
    tkinter.messagebox.showinfo("WINNER IS X!!",
                                "YOU HAVE JUST WON THE GAME.....")
  
    # score card for player O :
  if (button1["text"] == button2["text"] == button3["text"] == "O"):
    button1.configure(bg='light green')
    button2.configure(bg='light green')
    button3.configure(bg='light green')
    n = int(PlayerO.get())
    score = (n + 1)
    PlayerO.set(score)
    lbl = Label(Top,
                font=('arial', 12, 'bold'),
                bg='LavenderBlush',
                fg='dark blue',
                text="PLAYER O",
                bd=5)
    lbl.place(x=502, y=225)
    tkinter.messagebox.showinfo("WINNER IS O!!",
                                "YOU HAVE JUST WON THE GAME.....")
   
  if (button4["text"] == button5["text"] == button6["text"] == "O"):
    button4.configure(bg='light green')
    button5.configure(bg='light green')
    button6.configure(bg='light green')
    n = int(PlayerO.get())
    score = (n + 1)
    PlayerO.set(score)
    lbl = Label(Top,
                font=('arial', 12, 'bold'),
                bg='LavenderBlush',
                fg='dark blue',
                text="PLAYER O",
                bd=5)
    lbl.place(x=502, y=225)
    tkinter.messagebox.showinfo("WINNER IS O!!",
                                "YOU HAVE JUST WON THE GAME.....")
    
  if (button7["text"] == button8["text"] == button9["text"] == "O"):
    button7.configure(bg='light green')
    button8.configure(bg='light green')
    button9.configure(bg='light green')
    n = int(PlayerO.get())
    score = (n + 1)
    PlayerO.set(score)
    lbl = Label(Top,
                font=('arial', 12, 'bold'),
                bg='LavenderBlush',
                fg='dark blue',
                text="PLAYER O",
                bd=5)
    lbl.place(x=502, y=225)
    tkinter.messagebox.showinfo("WINNER IS O!!",
                                "YOU HAVE JUST WON THE GAME.....")
    
  if (button1["text"] == button4["text"] == button7["text"] == "O"):
    button1.configure(bg='sky blue')
    button4.configure(bg='sky blue')
    button7.configure(bg='sky blue')
    n = int(PlayerO.get())
    score = (n + 1)
    PlayerO.set(score)
    lbl = Label(Top,
                font=('arial', 12, 'bold'),
                bg='LavenderBlush',
                fg='dark blue',
                text="PLAYER O",
                bd=5)
    lbl.place(x=502, y=225)
    tkinter.messagebox.showinfo("WINNER IS O!!",
                                "YOU HAVE JUST WON THE GAME.....")
   
  if (button2["text"] == button5["text"] == button8["text"] == "O"):
    button2.configure(bg='sky blue')
    button5.configure(bg='sky blue')
    button8.configure(bg='sky blue')
    n = int(PlayerO.get())
    score = (n + 1)
    PlayerO.set(score)
    lbl = Label(Top,
                font=('arial', 12, 'bold'),
                bg='LavenderBlush',
                fg='dark blue',
                text="PLAYER O",
                bd=5)
    lbl.place(x=502, y=225)
    tkinter.messagebox.showinfo("WINNER IS O!!",
                                "YOU HAVE JUST WON THE GAME.....")
    
  if (button3["text"] == button6["text"] == button9["text"] == "O"):
    button3.configure(bg='sky blue')
    button6.configure(bg='sky blue')
    button9.configure(bg='sky blue')
    n = int(PlayerO.get())
    score = (n + 1)
    PlayerO.set(score)
    lbl = Label(Top,
                font=('arial', 12, 'bold'),
                bg='LavenderBlush',
                fg='dark blue',
                text="PLAYER O",
                bd=5)
    lbl.place(x=502, y=225)
    tkinter.messagebox.showinfo("WINNER IS O!!",
                                "YOU HAVE JUST WON THE GAME.....")
   
  if (button1["text"] == button5["text"] == button9["text"] == "O"):
    button1.configure(bg='Red')
    button5.configure(bg='Red')
    button9.configure(bg='Red')
    n = int(PlayerO.get())
    score = (n + 1)
    PlayerO.set(score)
    lbl = Label(Top,
                font=('arial', 12, 'bold'),
                bg='LavenderBlush',
                fg='dark blue',
                text="PLAYER O",
                bd=5)
    lbl.place(x=502, y=225)
    tkinter.messagebox.showinfo("WINNER IS O!!",
                                "YOU HAVE JUST WON THE GAME.....")
    
  if (button3["text"] == button5["text"] == button7["text"] == "O"):
    button3.configure(bg='Red')
    button5.configure(bg='Red')
    button7.configure(bg='Red')
    n = int(PlayerO.get())
    score = (n + 1)
    PlayerO.set(score)
    lbl = Label(Top,
                font=('arial', 12, 'bold'),
                bg='LavenderBlush',
                fg='dark blue',
                text="PLAYER O",
                bd=5)
    lbl.place(x=502, y=225)
    tkinter.messagebox.showinfo("WINNER IS O!!",
                                "YOU HAVE JUST WON THE GAME.....")
    
  if(count==9):
    if (not(button1["text"] == button2["text"] == button3["text"] == "X"or button4["text"] == button5["text"] == button6["text"] == "X"or
    button7["text"] == button8["text"] == button9["text"] == "X"or button1["text"] == button4["text"] == button7["text"]or button2["text"] == button5["text"] == button8["text"]
    or button3["text"] == button6["text"] == button9["text"]or button1["text"] == button5["text"] == button9["text"]
    or button3["text"] == button5["text"] == button7["text"])):
      tkinter.messagebox.showinfo("TIE","THERE IS TIE.....")
      
def reset():
  button1["text"] = " "
  button2["text"] = " "
  button3["text"] = " "
  button4["text"] = " "
  button5["text"] = " "
  button6["text"] = " "
  button7["text"] = " "
  button8["text"] = " "
  button9["text"] = " "

  button1.configure(bg="orange")
  button2.configure(bg="orange")
  button3.configure(bg="orange")
  button4.configure(bg="orange")
  button5.configure(bg="orange")
  button6.configure(bg="orange")
  button7.configure(bg="orange")
  button8.configure(bg="orange")
  button9.configure(bg="orange")


def new():
  button1["text"] = " "
  button2["text"] = " "
  button3["text"] = " "
  button4["text"] = " "
  button5["text"] = " "
  button6["text"] = " "
  button7["text"] = " "
  button8["text"] = " "
  button9["text"] = " "

  button1.configure(bg="orange")
  button2.configure(bg="orange")
  button3.configure(bg="orange")
  button4.configure(bg="orange")
  button5.configure(bg="orange")
  button6.configure(bg="orange")
  button7.configure(bg="orange")
  button8.configure(bg="orange")
  button9.configure(bg="orange")
  PlayerX.set(0)
  PlayerO.set(0)


#add labels to the players
#player 1 label :
lbl = Label(
  Top,
  font=('arial', 10, 'bold'),
  text="PLAYER X",
  bd=5,
  bg='NavajoWhite',
  fg='DeepPink',
)
lbl.place(x=375, y=125)  #350-250
txt = Entry(Top, font=('arial', 12, 'bold'), textvariable=PlayerX, width=7)
txt.place(x=500, y=125)  #350-250

# player 2 label :
lbl1 = Label(
  Top,
  font=('arial', 10, 'bold'),
  text="PLAYER O",
  bd=5,
  bg='NavajoWhite',
  fg='DeepPink',
)
lbl1.place(x=375, y=175)  #450-350
txt = Entry(Top, font=('arial', 12, 'bold'), textvariable=PlayerO, width=7)
txt.place(x=500, y=175)  #450-350

#score label:
lbl4 = Label(
  Top,
  font=('arial', 10, 'bold'),
  text="SCORE : ",
  bd=3,
  bg='azure',
  fg='DeepPink',
)
lbl4.place(x=502, y=90)  #250-150

#winner label :
labl2 = Label(Top,
              font=('Helvetica', 12, 'bold'),
              text="WINNER",
              bd=5,
              bg='OrangeRed',
              fg='BlanchedAlmond')
labl2.place(x=375, y=225)  #550-450

button1 = Button(BoardFrame,
                 text=" ",
                 font=('arial', 5, 'bold'),
                 height=2,
                 width=5,
                 bg='Plum',
                 command=lambda: checker(button1))
button1.grid(row=1, column=0, sticky=N + E + W + S)
button2 = Button(BoardFrame,
                 text=" ",
                 font=('arial', 5, 'bold'),
                 height=2,
                 width=5,
                 bg='Plum',
                 command=lambda: checker(button2))
button2.grid(row=1, column=1, sticky=N + E + W + S)
button3 = Button(BoardFrame,
                 text=" ",
                 font=('arial', 5, 'bold'),
                 height=2,
                 width=5,
                 bg='Plum',
                 command=lambda: checker(button3))
button3.grid(row=1, column=2, sticky=N + E + W + S)
button4 = Button(BoardFrame,
                 text=" ",
                 font=('arial', 5, 'bold'),
                 height=2,
                 width=5,
                 bg='Plum',
                 command=lambda: checker(button4))
button4.grid(row=2, column=0, sticky=N + E + W + S)
button5 = Button(BoardFrame,
                 text=" ",
                 font=('arial', 5, 'bold'),
                 height=2,
                 width=5,
                 bg='Plum',
                 command=lambda: checker(button5))
button5.grid(row=2, column=1, sticky=N + E + W + S)
button6 = Button(BoardFrame,
                 text=" ",
                 font=('arial', 5, 'bold'),
                 height=2,
                 width=5,
                 bg='Plum',
                 command=lambda: checker(button6))
button6.grid(row=2, column=2, sticky=N + E + W + S)
button7 = Button(BoardFrame,
                 text=" ",
                 font=('arial', 5, 'bold'),
                 height=2,
                 width=5,
                 bg='Plum',
                 command=lambda: checker(button7))
button7.grid(row=3, column=0, sticky=N + E + W + S)
button8 = Button(BoardFrame,
                 text=" ",
                 font=('arial', 5, 'bold'),
                 height=2,
                 width=5,
                 bg='Plum',
                 command=lambda: checker(button8))
button8.grid(row=3, column=1, sticky=N + E + W + S)
button9 = Button(BoardFrame,
                 text=" ",
                 font=('arial', 5, 'bold'),
                 height=2,
                 width=5,
                 bg='Plum',
                 command=lambda: checker(button9))
button9.grid(row=3, column=2, sticky=N + E + W + S)


def help():
  tkinter.messagebox.showinfo(
    'HELP',
    'HOW TO PLAY:\n1.Press a square to place your mark\n2.Make three in a row horizontally, vertically, or diagonally to win\n3.Watch your opponent and block them if they get 2 in a row\n4.Use the bottom right buttons to reset and new game'
  )

#help button
Help = Button(Top,
              text="HELP",
              height=1,
              width=4,
              bg='powder blue',
              command=help)
Help.place(x=600, y=280)
root.bind('<Button-1>', help)

#reset button
reset = Button(Top,
               text="RESET",
               height=1,
               width=5,
               bg='powder blue',
               command=reset)
reset.place(x=500, y=280)

#new button
new = Button(Top, text="NEW", height=1, width=4, bg='powder blue', command=new)
new.place(x=550, y=280)

#quit button
def quit():
  msg=messagebox.askquestion("Do you really want to Quit? You still have chances left!")
  if msg=='yes':
    root.destroy()
Quit=Button(Top,text="QUIT",height=1,width=4,bg='powder blue',command=quit)
Quit.place(x=600,y=50)

root.mainloop()


