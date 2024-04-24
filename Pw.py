import tkinter.messagebox
import turtle as l
import datetime, tkinter

def draw():
    l.setup(width=1280, height=720)
    l.hideturtle()
    l.color('#c2c902', '#560090')
    l.pensize(2)
    l.title('Polygon drawer')
    varlibol = int(l.numinput('Polygon drawer', 'Polygon sides:', default=3, minval=3, maxval=360))
    moves = 0
    if varlibol >= 270:
     moves = 5
    elif varlibol >= 200:
     moves = 6
    elif varlibol >= 120:
     moves = 9
    elif varlibol >= 60:
     moves = 15
    elif varlibol >= 20:
     moves = 30
    elif varlibol <= 19:
     moves = 62
    l.penup()
    l.goto(0, -250)
    l.pendown()
    l.begin_fill()
    time = 0
    for mama in range(varlibol):
      l.forward(moves)
      l.left(360 / varlibol)
      time += 1
      day = datetime.datetime.now().strftime("%X.%f")
      print(f'Side {time} drawing done at {day}.')
    l.end_fill()
    print('Done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print(f'{varlibol} sides polygon.')
    again = l.textinput('Polygon drawer', 'Do you want to draw another one? Yes pls type [y],No just click [Cancel].')
    if again == 'y':
      l.reset()
      draw()
    else:
      l.bye()
      
    l.mainloop()

draw()