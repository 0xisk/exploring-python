import tkinter as Tk
from mail_checker import *
from tkinter import messagebox
# ntlk.download('punkt')

class App(object):
    t = Tk.Text

    def __init__(self, parent):
        self.root = parent
        self.root.title("Email SPAM or HAM detector")
        self.frame = Tk.Frame(parent)
        self.frame.pack()
        btn = Tk.Button(self.frame, text="About Team", command=self.open_About_Team_Frame, bg='black', font=("", 20),
                        fg='green', width=20)
        btn.pack()
        btn = Tk.Button(self.frame, text="Start", command=self.open_Program_Frame, bg='black', font=("", 20), fg='red',
                        width=20,)
        btn.pack()
    def hide(self):
        self.root.withdraw()

    def open_About_Team_Frame(self):
        self.hide()
        about_team_Frame = Tk.Toplevel()
        about_team_Frame.geometry("600x250")
        about_team_Frame.title("otherFrame")
        andrew = Tk.Label(about_team_Frame, text="Andrew Amir   20150153", bg='black', fg="blue",
                          font=("Helvetica", 20))
        andrew.pack()
        yassen = Tk.Label(about_team_Frame, text="Yassen Hatem  20150633", fg="blue", font=("Helvetica", 20))
        yassen.pack()
        marc = Tk.Label(about_team_Frame, text="Marc Essam   20150398", fg="blue", font=("Helvetica", 20))
        marc.pack()
        eyad = Tk.Label(about_team_Frame, text="Eyad Mohamed   20150156", fg="blue", font=("Helvetica", 20))
        eyad.pack()
        mina = Tk.Label(about_team_Frame, text="Mina Mofreh   20150667", fg="blue", font=("Helvetica", 20))
        mina.pack()
        handler = lambda: self.onCloseOtherFrame(about_team_Frame)
        btn = Tk.Button(about_team_Frame, text="Back", command=handler)
        btn.pack()

    def onCloseOtherFrame(self, otherFrame):
        otherFrame.destroy()
        self.show()

    def show(self):
        self.root.update()
        self.root.deiconify()

    def format_text(self):
        text = self.t.get("1.0", 'end-1c')
        email_text = ''
        for i in text:
            if i != '\n':
                email_text += i
            else:
                email_text += ' '
        self.fina_result(email_text)

    def fina_result(self, text):
        result = ''
        text_color = ''
        if len(text) == 0:
            result = "it seems that you entered nothing!"
            text_color = "blue"
        else:
            if self.check_mail(text):
                result = "        SPAM EMAIL       "
            else:
                result = "        HAM EMAIL         "

        messagebox.showinfo("Information", result)

    #################################################
    def check_mail(self, str):
        pr_message = process_message(str)
        if sc_tf_idf.classify(pr_message):
            return True
        else:
            return False
    #################################################

    def open_Program_Frame(self):
        self.hide()
        otherFrame = Tk.Toplevel()
        otherFrame.geometry("500x400")
        otherFrame.title("Email SPAM or HAM detector")
        L1 = Tk.Label(otherFrame, text="Enter Email Text")
        L1.pack()
        self.t = Tk.Text(otherFrame, height=20, width=40, bd=5)
        self.t.pack()
        handler = lambda: self.onCloseOtherFrame(otherFrame)
        btn = Tk.Button(otherFrame, text="Back", width=15, command=handler)
        btn.pack()
        btn = Tk.Button(otherFrame, text="Check", fg='green', width=15, command=self.format_text)
        btn.pack()
