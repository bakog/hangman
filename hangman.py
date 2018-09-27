# coding=utf-8
import tkinter as tk
from tkinter import ttk, Menu, Toplevel
import sys
import random


words = ['hardver', 'alaplap', 'monitor', 'lapolvasó']

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__( self, *args, **kwargs)

        mainframe = ttk.Frame()
        mainframe.pack(fill="both", expand=True)

        menubar = Menu(self)
        self.config(menu=menubar)
        self.config(padx=3, pady=3)

        self.user_chars = list()
        self.tippszam = 0
        self.user_char = ''
        self.user_word= ''
        self.error = 0

        def setting(self):
            pass

        def exit():
            sys.exit()

        def new_game():
            self.tippszam=0
            self.word = random.choice(words).upper()
            self.user_chars = [ "_" for i in self.word ]
            print(self.word)
            gombok = list()

            def test_char():
                self.user_char= user_char.get().upper()
                print(self.user_char)
                self.tippszam+=1
                if self.user_char in self.word:
                    print("benne van")
                    for i in range(len(self.word)):
                        if self.user_char== self.word[i]:
                            gombok[i].config(text=self.user_char)
                            self.user_chars[i] = self.user_char
                            self.user_word = "".join(self.user_chars)
                    user_char_value.set('')
                    if self.user_word == self.word:
                        print("kitaláltad")
                    if self.error >=5:
                        print("nincs több lehetőséged")

                else:
                    self.error += 1
                    print(self.error, str(self.error) + ".png")
                    user_char_value.set('')
                    photo = tk.PhotoImage(file=str(self.error) + ".png")
                    photo_label.configure(image = photo)
                    photo_label.image = photo

                    #photo_label.grid(row=2, column=0, columnspan=2)
                    #photo_label.update()
                    print("nincs benne")




            user_char_label = ttk.Label(mainframe, text="Melyik betűre tippelsz?")
            user_char_label.grid(row=0, column=0)
            user_char_value = tk.StringVar()
            user_char_value.set('')
            user_char = ttk.Entry(mainframe, textvariable=user_char_value)
            user_char.grid(row=0, column=1)
            user_char.bind('<Return>', lambda w: test_char())

            word_frame = ttk.Frame(mainframe)
            word_frame.grid(row=1, column=0, columnspan=2)

            for i in range(len(self.word)):
                btn= ttk.Button(word_frame,text="_", width=2)
                btn.grid(row=1, column=i)
                gombok.append(btn)

            #vaszon = tk.Canvas(mainframe, width=160, height=160, bg='white')
            photo = tk.PhotoImage(file=str(self.error)+".png")
            photo_label = tk.Label(mainframe, image=photo)
            photo_label.grid(row=2, column=0, columnspan=2)
            photo_label.image = photo
            #photo_label.image.config(height=100)
            #photo_label.image.config(width=100)



        def about():
            about_win = tk.Toplevel()
            about_win.title("Hangman - Akasztófa játék")
            about_win.wm_minsize(300, 200)
            about_win.resizable(False, False)
            mainframe = ttk.Frame(about_win)
            mainframe.pack(fill="both", expand=True)

            def exit():
                about_win.destroy()

            mainframe.bind("<Button-1>", lambda w: exit())

            label_keszito = ttk.Label(mainframe, text="Bakó Gábor")
            label_keszito.pack()




        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade( label="File", menu=filemenu)
        filemenu.add_command(label="New game", command=new_game)
        filemenu.add_command(label="Settings", command=setting)
        filemenu.add_command(label="About", command=about)

        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=exit)







hangman = App()
hangman.title ("Hangman - Akasztófa játék")
hangman.wm_minsize(300, 200)
#hangman.resizable(False, False)
hangman.mainloop()