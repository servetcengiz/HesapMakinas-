import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("hesap Makinası - servet")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_810=tk.Button(root)
        GButton_810["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_810["font"] = ft
        GButton_810["fg"] = "#000000"
        GButton_810["justify"] = "center"
        GButton_810["text"] = "+"
        GButton_810.place(x=110,y=350,width=70,height=25)
        GButton_810["command"] = self.GButton_810_command

        GButton_128=tk.Button(root)
        GButton_128["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_128["font"] = ft
        GButton_128["fg"] = "#000000"
        GButton_128["justify"] = "center"
        GButton_128["text"] = "-"
        GButton_128.place(x=190,y=350,width=70,height=25)
        GButton_128["command"] = self.GButton_128_command

        GButton_356=tk.Button(root)
        GButton_356["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_356["font"] = ft
        GButton_356["fg"] = "#000000"
        GButton_356["justify"] = "x"
        GButton_356["text"] = "Button"
        GButton_356.place(x=270,y=350,width=70,height=25)
        GButton_356["command"] = self.GButton_356_command

        GButton_251=tk.Button(root)
        GButton_251["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_251["font"] = ft
        GButton_251["fg"] = "#000000"
        GButton_251["justify"] = "center"
        GButton_251["text"] = "/"
        GButton_251.place(x=350,y=350,width=70,height=25)
        GButton_251["command"] = self.GButton_251_command

        GLineEdit_387=tk.Entry(root)
        GLineEdit_387["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_387["font"] = ft
        GLineEdit_387["fg"] = "#333333"
        GLineEdit_387["justify"] = "center"
        GLineEdit_387["text"] = "Entry"
        GLineEdit_387.place(x=140,y=210,width=70,height=25)

        GLineEdit_232=tk.Entry(root)
        GLineEdit_232["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_232["font"] = ft
        GLineEdit_232["fg"] = "#333333"
        GLineEdit_232["justify"] = "center"
        GLineEdit_232["text"] = "Entry"
        GLineEdit_232.place(x=230,y=210,width=70,height=25)

        GLineEdit_643=tk.Entry(root)
        GLineEdit_643["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_643["font"] = ft
        GLineEdit_643["fg"] = "#333333"
        GLineEdit_643["justify"] = "center"
        GLineEdit_643["text"] = "Entry"
        GLineEdit_643.place(x=340,y=210,width=70,height=25)

        GLabel_498=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_498["font"] = ft
        GLabel_498["fg"] = "#333333"
        GLabel_498["justify"] = "center"
        GLabel_498["text"] = "sayı 1"
        GLabel_498.place(x=130,y=170,width=70,height=25)

        GLabel_483=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_483["font"] = ft
        GLabel_483["fg"] = "#333333"
        GLabel_483["justify"] = "center"
        GLabel_483["text"] = "sayı 2"
        GLabel_483.place(x=220,y=170,width=70,height=25)

        GLabel_394=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_394["font"] = ft
        GLabel_394["fg"] = "#333333"
        GLabel_394["justify"] = "center"
        GLabel_394["text"] = "sonuc"
        GLabel_394.place(x=330,y=170,width=70,height=25)

    def GButton_810_command(self):
        print("Buton 1'e basıldı")


    def GButton_128_command(self):
        print("Buton 2'ye basıldı")


    def GButton_356_command(self):
        print("command")


    def GButton_251_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)

    textBoxYazilanlar1 = tk.StringVar()
    textBoxYazilanlar2 = tk.StringVar()
    textBoxYazilanlar3 = tk.StringVar()
    root.mainloop()
