import tkinter
from square import Square

height=500
width=1600
initial_height_x = 200
whitespace_width_x = 80
initial_height_y  = 190
whitespace_width_y = 120

inp = [10,9,8,7,6,5,4,3,2,1]
polynom = [1,2,1]
list_squares = []
output = []
top = tkinter.Tk()
canvas = tkinter.Canvas(top, bg="white", height=500, width=1600)



def draw_input(top):       
    global I
    I = tkinter.Label(top, height = 1, width = 50, font=("Purisa", 16), text="Input:" + string_builder(inp))
    I.pack()


def draw_output(top):       
    global O
    O = tkinter.Label(top, height = 1, width = 50, font=("Purisa", 16), text="Output:" + string_builder(output) )
    O.pack()


def draw():

    for i in range(len(polynom)):
        outer = False
        helper = i+1
        x1 = helper*initial_height_x
        x2 = helper*initial_height_x + whitespace_width_x
        y1 = initial_height_y
        y2 = initial_height_y + whitespace_width_y
        if i==0:
            outer = True
        item = Square(x1,y1,x2,y2,canvas,outer,i,polynom[i])
        list_squares.append(item)


    draw_input(top)
    draw_output(top)
    button = tkinter.Button(top, text = "Advance", command= step)
    button.pack()
    canvas.pack()

def string_builder(array):
    string = ""
    for i in range(len(array)):
        if(i != len(array)-1):
            string = string+str(array[i])+","
        else:
            string = string+str(array[i])

    return string    

def step():

    if (list_squares[len(list_squares)-1].pout != None):
        output.append(list_squares[len(list_squares)-1].pout)    
    
    i = len(list_squares)-1
    while(i > 0):
        list_squares[i].xin = list_squares[i-1].xout
        list_squares[i].xout = list_squares[i].xin
        list_squares[i].pin = list_squares[i-1].pout
        
        if(list_squares[i].pin != None and list_squares[i].xin != None):
            list_squares[i].pout = list_squares[i].pin*list_squares[i].xin+list_squares[i].coef 
        else:
            list_squares[i].pout = None 

        i = i-1
    
    if inp:
        aux = inp.pop()
        list_squares[0].xin = aux
        list_squares[0].xout = aux
        list_squares[0].pin = 0
        list_squares[0].pout = list_squares[0].pin*list_squares[0].xin+list_squares[0].coef  

    else:
        list_squares[0].xin = None
        list_squares[0].xout = None
        list_squares[0].pin = None
        list_squares[0].pout = None

    I.configure(text = "Input: " + string_builder(inp))
    O.configure(text = "Output: "+ string_builder(output))
    canvas.delete("tag")

    for k in list_squares:
         k.draw_tags()  

def main():
    draw() 
    top.mainloop()

main()
