import os
import PIL
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import *
folder="compress"

def addText(text):
    display_text.set(display_text.get()+"\n"+text)
def createFoldear(route):
    try:
        addText("Created folder")
        os.mkdir(route+folder)
    except:
        addText("Unable to create folder or exists")
def getElements(route):
    print(route)
    elements = []
    for e in os.listdir(route):
        elements.append(e)
    return elements
def getRoutes():
    return os.path.dirname(__file__)+"\\"
def saveCompressFile(elemen,route):
    print(elemen)
    for e in elemen:
        try:
            Image=PIL.Image.open(route+e)
            height, width = Image.size
            Image = Image.convert('RGB')
            Img = Image.resize((height,width), PIL.Image.ANTIALIAS)
            Img.save(route+folder+"\\"+e.split(".")[0]+".webp", 'webp' , quality=65, optimize=True) 
        except:
            print("Unable to save "+e)
def execute():
    button_1["state"] = "disabled"
    route= filedialog.askdirectory()+"/"
    print(route)
    createFoldear(route)
    elementos = getElements(route)
    addText("Compress files in :"+route)
    saveCompressFile(elementos,route)
    
    

app=tk.Tk()
app.geometry("600x300")

app.configure(background="gray")

tk.Wm.wm_title(app,"Compress Image")

display_text = tk.StringVar()

tk.Label(app, 
    textvariable=display_text,
    height= 10,
    width=100,
    anchor='n').pack(pady=20)
button_1 = tk.Button(app,
    text="Compress",
    font=("Coutrier",14),
    bg="#00CBD2",
    fg="white",
    command=execute,
    height= 2,
    width=10,)
button_1.pack(pady=10)


app.mainloop()