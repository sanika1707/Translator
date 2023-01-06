import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from googletrans import LANGUAGES
from translate import Translator

root = tk.Tk()

src_text = Text(root, font="arial 10", height=11, wrap=WORD, padx=5, pady=5, width=60)
src_text.place(x=50, y=120)

des_text = Text(root, font="arial 10", height=11, wrap=WORD, padx=5, pady=5, width=60)
des_text.place(x=600, y=120)

class Lang_Translator(Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.label()

	src_text = Text(root)
	des_text = Text(root)
	
	def label(self):
		Label(root,text="Language Translator", font="italic 20").pack(side="top")
		Label(root,text="Select Language", font="arial 15").place(x=30, y=60)
		Label(root,text="Select Language", font="arial 15").place(x=600, y=60)

lang = list(LANGUAGES.values())
src_lang = ttk.Combobox(root, values=lang, width=30)
src_lang.place(x=200, y=63)
src_lang.set("english")

des_lang = ttk.Combobox(root, values=lang, width=30)
des_lang.place(x=770, y=63)
des_lang.set("marathi")

def trans():
	translator2 = Translator(to_lang = des_lang.get())
	translated = translator2.translate(src_text.get(0.0, END))
	des_text.insert(0.0, translated)

def clear_all() : 
    des_text.delete(0.0, END)  
    src_text.delete(0.0, END)
	
button_1 = Button(root, text="Translate" , command=trans).place(x=510, y=160)
button_2 = Button(root, text="Clear", command=clear_all).place(x=510, y=220)

app = Lang_Translator(master=root)
app.master.title('Translator')
app.master.geometry('1080x350')
app.mainloop()									
