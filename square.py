class Square():

    def __init__(self,x1,y1,x2,y2,canvas,outer,var,coef):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.outer = outer
        self.var = var
        self.coef = coef
        self.xin = None
        self.xout = None
        self.pin = None
        self.pout = None
        self.canvas = canvas

        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill="white", outline = 'black')
        #topleft
        canvas.create_line(x1-70,y1+25,x1,y1+25)

        #topright
        canvas.create_line(x1+80,y1+25,x1+150,y1+25)


        #bottomleft
        canvas.create_line(x1-70,y2-25,x1,y2-25)


        #bottomright
        canvas.create_line(x1+80,y2-25,x1+150,y2-25)


        if outer == False:
            canvas.create_rectangle(x1-70,y1+10,x1-50,y1+40, fill="black", outline = 'black')
            canvas.create_rectangle(x1-70,y2-10,x1-50,y2-40, fill="black", outline = 'black')

        canvas.create_text((x1+40,y1+30), text="P"+str(var))
        canvas.create_text((x1+40,y1+90), text=str(coef))
        self.draw_tags()
       


    def draw_tags(self):
        #topleft
        if(self.pin != None):
            self.canvas.create_text((self.x1-15,self.y1+15), tag="tag", text= str(self.pin))
        else:
            self.canvas.create_text((self.x1-15,self.y1+15), tag="tag", text="")

        #topright
        if(self.pout != None):
            self.canvas.create_text((self.x1+95,self.y1+15), tag="tag", text=str(self.pout))
        else:
            self.canvas.create_text((self.x1+95,self.y1+15), tag="tag", text="")

        #bottomleft
        if(self.xin != None):
            self.canvas.create_text((self.x1-15,self.y2-35), tag="tag", text=str(self.xin))
        else:
            self.canvas.create_text((self.x1-15,self.y2-35), tag="tag", text="")

        #bottomright
        if(self.xout != None):
            self.canvas.create_text((self.x1+95,self.y2-35), tag="tag", text=str(self.xout))
        else:
            self.canvas.create_text((self.x1+95,self.y2-35), tag="tag", text="")




    def __str__(self):
        return str(self.x1) + " " + str(self.y1) + " " + str(self.x2) + " " + str(self.y2)