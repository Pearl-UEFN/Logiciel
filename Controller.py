import tkinter as tk
from tkinter import *
import csv
from tkinter.filedialog import askopenfilename
import models.Video as _Video_



class Image:
     
    def Test(canvas):
        print("Image")
        print("yes")
        filename = askopenfilename()
        print(filename)
        img = PhotoImage(file= filename)
        img.show()
        canvas.create_image(20,20, anchor=NW, image=img)
        print("all code done")


class Controller():

    def __init__(self,parent, video, view):
        
        self.video = video
        self.view = view
        self.tk = parent
        #-----------------#
        frame = self.view.GetFrame
        self.canvas = Canvas(self.tk, width=300, height=300)
        self.canvas.pack
        print(type(self.canvas))

        self.tk.bind("<Button-1>", Controller.leftclick)

        ####=====BUTTONS=====####
        B = Button(self.tk, text ="Hello", command = Image.Test(self.canvas))
        B.place(x=50,y=50)

    def VideoClass(self):
        return self.video
    
    def GetCanvas(self):
        return self.canvas

    def leftclick(event):
    
        print("left")
        MousePosition = (event.x,event.y)
        Points.AddMousePos(MousePosition)

    def GetTK (self):
        return self.tk

    top = GetTK
    
        


class Points:       

    def AddMousePos(Pos : tuple):
        PosX = Pos[0]
        PosY = Pos[1]
        Lst : list = []
        Chara = ""
        Chara = str(PosX) + ";" + str(PosY)
        Lst.append(Chara)
        print(Lst)
        ToWrite = "X:" + str(PosX) + "-" +"Y:"+ str(PosY) + "|"
        with open('ListePoints.csv', 'a') as csvfile:   
            print("Csv opened")
            writer = csv.writer(csvfile, delimiter= ' ')
            writer.writerows([ToWrite])




    
            



            

        

        