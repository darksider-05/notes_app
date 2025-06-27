import tkinter
import tkinter.messagebox
import pickle
import datetime

god_dict = {}
god_list = []
god_check = {}
god_dati = {}
users_list= []
users_dict= {}
a= ""
front_color = "#000000"
back_color = "#f1f1f1"


class Firstpage:
    def __init__(self):
        self.main_win()

    def main_win(self):
        self.mainwin = tkinter.Tk()
        self.mainwin.configure(bg=back_color)
        self.mainwin.geometry('500x400')
        self.mainwin.resizable(False, False)
        m_lbl1 = tkinter.Label(self.mainwin, text="welcome", font=("arial", 20), bg=back_color, fg=front_color)
        m_lbl2 = tkinter.Label(self.mainwin, text="this is the main window", font=("arial", 15), bg=back_color,
                               fg=front_color)
        m_btn1 = tkinter.Button(self.mainwin, text="show list", font=("arial", 15), command=self.to_show, width=10,
                                height=1, bg=back_color, fg=front_color)
        m_btn2 = tkinter.Button(self.mainwin, text="sort list", font=("arial", 15), command=self.to_sort, width=10,
                                height=1, bg=back_color, fg=front_color)
        m_btn4 = tkinter.Button(self.mainwin, text="save/import", font=("arial", 15), command=self.to_save, width=10,
                                height=1, bg=back_color, fg=front_color)
        m_btn5 = tkinter.Button(self.mainwin, text="settings", font=("arial", 10), command=self.to_set, width=10,
                                height=1, bg=back_color, fg=front_color)
        m_btn6 = tkinter.Button(self.mainwin, text="exit", font=("arial", 10), command=self.mainwin.destroy, width=10,
                                height=1, bg="darkred", fg="white")

        m_lbl1.pack()
        m_lbl2.pack()
        m_btn1.place(x=190, y=150)
        m_btn2.place(x=190, y=200)
        m_btn4.place(x=190, y=250)
        m_btn5.place(x=0, y=20)
        m_btn6.place(x=400, y=350)
        self.mainwin.mainloop()

    def to_save(self):
        self.mainwin.destroy()
        Storagewin()

    def to_set(self):
        self.mainwin.destroy()
        Settingpage()

    def to_show(self):
        self.mainwin.destroy()
        Showpage()

    def to_sort(self):
        self.mainwin.destroy()
        Sortpage()


class Showpage:
    def __init__(self):
        self.show_win()

    def show_win(self):

        self.showwin = tkinter.Tk()
        self.showwin.configure(bg=back_color)
        self.showwin.geometry('500x400')
        self.showwin.resizable(False, False)

        self.listbo = tkinter.Listbox(self.showwin, bg=back_color, fg=front_color)
        self.scrollbar = tkinter.Scrollbar(self.showwin, orient=tkinter.VERTICAL, command=self.listbo.yview)
        self.listbo.configure(yscrollcommand=self.scrollbar.set)
        self.listbo.pack()

        btn_bac = tkinter.Button(self.showwin, text="back to main page", command=self.back_from_show, bg=back_color,
                                 fg=front_color)
        btn_bac.pack()

        for i in god_list:
            if god_check[i] == "checked":
                self.listbo.insert(tkinter.END, i + "  *")
            else:
                self.listbo.insert(tkinter.END, i)

        btn_add = tkinter.Button(self.showwin, command=self.aded,
                                 text="add note, \nif topic exists, \nedits the content", font=("arial", 10),
                                 bg=back_color, fg=front_color)
        btn_add.place(x=365, y=150)

        srch_lbl = tkinter.Label(self.showwin, text="search exact topic:", font=("arial", 9), bg=back_color,
                                 fg=front_color)
        srch_lbl.place(x=40, y=30)
        self.srch_ent = tkinter.Entry(self.showwin, bg=back_color, fg=front_color)
        self.srch_ent.place(x=40, y=50)
        srch_btn = tkinter.Button(self.showwin, command=self.srched, text="search", font=("arial", 10), bg=back_color,
                                  fg=front_color)
        srch_btn.place(x=40, y=75)

        self.del_ent = tkinter.Entry(self.showwin, width=15, bg=back_color, fg=front_color)
        self.del_ent.place(x=365, y=90)
        del_btn = tkinter.Button(self.showwin, command=self.dele, text="delete note", font=("arial", 10), bg=back_color,
                                 fg=front_color)
        del_btn.place(x=365, y=110)

        updeit_btn = tkinter.Button(self.showwin, command=self.updeit, text="update list", font=("arial", 10),
                                    bg=back_color, fg=front_color)
        updeit_btn.place(x=365, y=40)

        self.show_ent = tkinter.Entry(self.showwin, width=23, bg=back_color, fg=front_color)
        self.show_ent.pack(pady=10)
        self.show_txt = tkinter.Text(self.showwin, width=50, height=7, bg=back_color, fg=front_color)
        self.show_txt.pack()
        self.show_stat = tkinter.Label(self.showwin, text="unchecked", font=("arial", 12), bg=back_color,
                                       fg=front_color)
        self.show_stat.place(x=80, y=150)
        self.stat_changer = tkinter.Button(self.showwin, text="check/uncheck", command=self.change_stat, bg=back_color,
                                           fg=front_color)
        self.stat_changer.place(x=65, y=175)

        self.da_me = tkinter.Label(self.showwin,font=("arial", 10), bg=back_color, fg=front_color)
        self.da_me.place(x=60, y=125)

        self.clerr = tkinter.Button(self.showwin, command=self.clerre, text="clear fields", font=("arial",10) ,
                                    bg=back_color, fg=front_color)
        self.clerr.place(x=230, y=360)

        self.listbo.bind('<<ListboxSelect>>', self.selected_of_the_list)
        self.showwin.mainloop()
    
    def clerre(self):
        try:
            self.show_ent.delete(0, tkinter.END)
        except:
            pass
        try:
            self.show_txt.delete(1.0, tkinter.END)
        except:
                pass
        try:
            self.da_me.config(text="")
        except:
            pass
        try:
            self.show_stat.config(text="unchecked")
        except:
            pass
        self.da_me.config(text="")

    def selected_of_the_list(self, event):
        if self.showwin.focus_get() != self.listbo:
            return

        try:
            self.show_ent.delete(0, tkinter.END)
            self.show_txt.delete(1.0, tkinter.END)
        except:
            pass
        a = self.listbo.curselection()  # here, "a" gets returned as a tuple
        if len(a) != 0:
            index = a[-1]  # "index" is the index of topic in god_list
            b = god_list[index]  # "b" is the text
            c = god_dict[b]
            d = god_check[b]
            e= god_dati[b]
            self.show_ent.insert(tkinter.END, b)
            self.show_txt.insert(tkinter.END, str(c))
            self.show_stat.config(text=d)
            self.da_me.config(text=e)
            a = 0
        else:
            tkinter.messagebox.showerror("Error",
                                         "nothing selected, please update \nand select an existing option \nor make a new one")

    def back_from_show(self):
        self.showwin.destroy()
        Firstpage()

    def srched(self):
        try:
            self.show_ent.delete(0, tkinter.END)
            self.show_txt.delete(1.0, tkinter.END)
        except:
            pass
        a = self.srch_ent.get()
        if a in god_list:
            self.show_ent.insert(tkinter.END, a)
            self.show_txt.insert(tkinter.END, god_dict[a])
            self.show_stat.config(text=god_check[a])
            self.da_me.config(text=god_dati[a])
            tkinter.messagebox.showinfo(title="done", message="the note has been found")
        else:
            tkinter.messagebox.showwarning(title="Warning", message="the note was not found")

    def aded(self):
        a = self.show_ent.get()
        b = self.show_txt.get(1.0, tkinter.END)
        now = datetime.datetime.now()
        c = now.strftime("%Y-%m-%d %H:%M:%S")

        if a in god_list:
            god_dict[a] = b
            god_dati[a] = c
            tkinter.messagebox.showinfo(title="done", message="the note has been overwritten")
        else:
            if a != "" and a != " " and a != "  " and a != "   " and a != "    " and a != "     ":
                god_list.append(a)
                god_dict[a] = b
                god_check[a] = "unchecked"
                god_dati[a] = c
                self.updeit()
                self.show_stat.config(text="unchecked")
                
                tkinter.messagebox.showinfo(title="done", message="the note has been added")
            else:
                tkinter.messagebox.showwarning(title="Warning", message="the note needs a title")

    def change_stat(self):
        a = self.show_ent.get()
        if a != "" and a != " " and a != "  " and a != "   " and a != "    " and a != "     ":
            b = god_check[a]
            if b == "unchecked":
                god_check[a] = "checked"
            elif b == "checked":
                god_check[a] = "unchecked"
            self.show_stat.config(text=god_check[a])
            self.updeit()
        else:
            tkinter.messagebox.showwarning(title="Warning", message="please select an existing note, first")

    def updeit(self):
        self.listbo.delete(0, tkinter.END)
        for i in god_list:
            if god_check[i] == "checked":
                self.listbo.insert(tkinter.END, i + "  *")
            else:
                self.listbo.insert(tkinter.END, i)

    def dele(self):
        a = self.del_ent.get()
        if a in god_list:
            god_list.remove(a)
            god_dict.pop(a, None)
            god_check.pop(a, None)
            god_dati.pop(a, None)
            self.updeit()
            tkinter.messagebox.showinfo(title="done", message="the note has been deleted")
        else:
            tkinter.messagebox.showwarning(title="warning", message="the note was not found")


class Settingpage:
    def __init__(self):
        self.set_page()

    def set_page(self):
        self.setwin = tkinter.Tk()
        self.setwin.config(bg=back_color)
        self.setwin.geometry('500x400')
        self.setwin.resizable(False, False)

        bac_btn = tkinter.Button(self.setwin, text="back to main page", command=self.back_from_settings, bg=back_color,
                                 fg=front_color)
        bac_btn.place(x=200, y=300)

        setlbl1 = tkinter.Label(self.setwin, text="theme settings", bg=back_color, fg=front_color, font=("arial", 12))
        setlbl1.place(x=190, y=50)

        python_btn = tkinter.Button(self.setwin, text="python theme", command=self.color_set_python, bg="darkblue",
                                    fg="yellow")
        python_btn.place(x=200, y=75)
        invert_python_btn = tkinter.Button(self.setwin, text="inverted python theme",
                                           command=self.color_set_inverted_python, bg="#ffe933", fg="#202aca")
        invert_python_btn.place(x=175, y=110)
        green_btn = tkinter.Button(self.setwin, text="nature theme", command=self.color_set_nature, bg="#03bc49",
                                   fg="yellow")
        green_btn.place(x=200, y=145)
        white_btn = tkinter.Button(self.setwin, text="white theme", command=self.color_set_white, bg="#f1f1f1",
                                   fg="#000000")
        white_btn.place(x=200, y=180)
        night_btn = tkinter.Button(self.setwin, text="night theme", command=self.color_set_night, bg="#000000",
                                   fg="#ffffff")
        night_btn.place(x=200, y=215)

        self.setwin.mainloop()

    def back_from_settings(self):
        self.setwin.destroy()
        Firstpage()

    def color_set_python(self):
        global back_color
        global front_color
        back_color = "darkblue"
        front_color = "yellow"

    def color_set_inverted_python(self):
        global back_color
        global front_color
        back_color = "#ffe933"
        front_color = "#202aca"

    def color_set_nature(self):
        global back_color
        global front_color
        back_color = "#03bc49"
        front_color = "yellow"

    def color_set_white(self):
        global back_color
        global front_color
        back_color = "#f9f9f9"
        front_color = "#000000"

    def color_set_night(self):
        global back_color
        global front_color
        back_color = "#000000"
        front_color = "#ffffff"


class Sortpage:
    def __init__(self):
        self.container1 = ""
        self.container2 = ""
        self.container3 = ""
        self.sor_win()

    def sor_win(self):
        self.sorwin = tkinter.Tk()
        self.sorwin.config(bg=back_color)
        self.sorwin.geometry('500x400')
        self.sorwin.resizable(False, False)

        self.sor_listbo = tkinter.Listbox(self.sorwin, bg=back_color, fg=front_color)
        self.sor_scrollbar = tkinter.Scrollbar(self.sorwin, orient=tkinter.VERTICAL, command=self.sor_listbo.yview)
        self.sor_listbo.configure(yscrollcommand=self.sor_scrollbar.set)
        self.sor_listbo.pack()

        self.sor_listbo.bind('<<ListboxSelect>>', self.set_to_sort)

        for i in god_list:
            if god_check[i] == "checked":
                self.sor_listbo.insert(tkinter.END, i + "  *")
            else:
                self.sor_listbo.insert(tkinter.END, i)

        self.sor_lbl1 = tkinter.Label(self.sorwin, text=f"you chose: ", bg=back_color, fg=front_color)
        self.sor_lbl1.place(x=350, y=150)

        sor_btn1 = tkinter.Button(self.sorwin, command=self.back_from_sort, text="back to main window",
                                  background=back_color, foreground=front_color)
        sor_btn2 = tkinter.Button(self.sorwin, command=self.move_up, text="move up", background=back_color,
                                  foreground=front_color)
        sor_btn3 = tkinter.Button(self.sorwin, command=self.move_down, text="move down", background=back_color,
                                  foreground=front_color)

        sor_btn1.pack(pady=10)
        sor_btn2.place(x=350, y=115)
        sor_btn3.place(x=350, y=185)

        self.sorwin.mainloop()

    def back_from_sort(self):
        self.sorwin.destroy()
        Firstpage()

    def move_up(self):
        self.container2 = god_list[self.container1]
        self.container3 = self.container1 - 1
        if self.container3 < 0:
            self.container3 = 0
            tkinter.messagebox.showwarning(title="error", message="this is the beginning of the list")
        god_list.remove(self.container2)
        god_list.insert(self.container3, self.container2)
        self.container1 = self.container3
        self.sor_listbo.delete(0, tkinter.END)
        for i in god_list:
            if god_check[i] == "checked":
                self.sor_listbo.insert(tkinter.END, i + "  *")
            else:
                self.sor_listbo.insert(tkinter.END, i)

    def move_down(self):
        self.container2 = god_list[self.container1]

        self.container3 = self.container1 + 1
        god_list.remove(self.container2)
        god_list.insert(self.container3, self.container2)
        self.container1 = self.container3
        if self.container1 > len(god_list) - 1:
            self.container1 -= 1
            tkinter.messagebox.showwarning(title="error", message="this is the end of the list")
        self.sor_listbo.delete(0, tkinter.END)
        for i in god_list:
            if god_check[i] == "checked":
                self.sor_listbo.insert(tkinter.END, i + "  *")
            else:
                self.sor_listbo.insert(tkinter.END, i)

    def set_to_sort(self, event):
        global god_sort
        a = self.sor_listbo.curselection()  # here, "a" gets returned as a tuple
        if len(a) != 0:
            self.container1 = a[-1]  # "index" is the index of topic in god_list
            z = god_list[a[-1]]
            self.sor_lbl1.configure(text=f"you chose: {z}")
            tkinter.messagebox.showinfo(title="done", message="the note has been selected")
        else:
            tkinter.messagebox.showwarning(title="error", message="nothing selected")


class Storagewin:
    def __init__(self):
        self.savloa()

    def savloa(self):
        self.filepage = tkinter.Tk()
        self.filepage.config(bg=back_color)
        self.filepage.geometry('500x400')
        self.filepage.resizable(False, False)

        file_btn1 = tkinter.Button(self.filepage, command=self.back_from_file, text="back to main window",
                                   bg=back_color, fg=front_color)
        file_btn1.place(x=190, y=300)

        file_lbl1 = tkinter.Label(self.filepage,text="here, you can save/load data data",
                                  font=("arial", 12,), bg=back_color, fg=front_color)
        file_lbl1.pack()
        file_btn3 = tkinter.Button(self.filepage, command=self.seiv, text="save to file", bg=back_color, fg=front_color)
        file_btn4 = tkinter.Button(self.filepage, command=self.lode, text="load from file", bg=back_color,fg=front_color)
        file_btn5 = tkinter.Button(self.filepage, command=self.cler, text="clear file", bg=back_color, fg=front_color)

        file_btn5.place(x=330, y=180)
        file_btn3.place(x=110, y=120)
        file_btn4.place(x=110, y=180)

        self.filepage.mainloop()

    def back_from_file(self):
        self.filepage.destroy()
        Firstpage()

    def seiv(self):
        global god_list
        global god_dict
        global god_check
        global god_dati
        global a
        z = open(f"{a}.bkz", "wb")
        pickle.dump(god_list, z)
        pickle.dump(god_dict, z)
        pickle.dump(god_check, z)
        pickle.dump(god_dati, z)
        z.close()



    def lode(self):
        global god_list
        global god_dict
        global god_check
        global god_dati
        global a

        z = open(f"{a}.bkz", "rb")
        try:
            god_list = pickle.load(z)
        except:
            god_list = []
        try:
            god_dict = pickle.load(z)
        except:
            god_dict = {}
        try:
            god_check = pickle.load(z)
        except:
            god_check = {}
        try:
            god_dati = pickle.load(z)
        except:
            god_dati = {}
        
        z.close()

    def cler(self):
        global god_list
        global god_dict
        global god_check
        global god_dati
        global a
        
        z = open(a, "wb")
        pickle.dump({}, z)
        pickle.dump({}, z)
        pickle.dump({}, z)
        pickle.dump({}, z)
        z.close()

class Logpage:
    def __init__(self):
        self.first_file()
        self.log_win()

    def log_win(self):
        self.logwin= tkinter.Tk()
        self.logwin.config(bg=back_color)
        self.logwin.geometry("500x400")
        self.logwin.resizable( False, False)

        log_lbl1= tkinter.Label(self.logwin, text="welcome, please sign up or log in,\nplease note that your password can not be changed",
                                font=("arial", 12), bg= back_color, fg=front_color )
        log_lbl2= tkinter.Label(self.logwin, text="user name",bg= back_color, fg=front_color )
        log_lbl3= tkinter.Label(self.logwin, text="password", bg= back_color, fg=front_color )
        self.log_ent1= tkinter.Entry(self.logwin, width=15, bg= back_color, fg= front_color)
        self.log_ent2= tkinter.Entry(self.logwin, width=15, bg= back_color, fg= front_color)
        log_btn1= tkinter.Button(self.logwin, command=self.sign_up, text="sign up", bg= back_color, fg= front_color)
        log_btn2= tkinter.Button(self.logwin, command=self.log_in, text="log in", bg= back_color, fg= front_color)


        log_lbl1.pack()
        log_lbl2.place(x=150, y=100)
        log_lbl3.place(x=150, y=125)
        self.log_ent1.place(x=210, y=100)
        self.log_ent2.place(x=210, y=125)
        log_btn1.place(x=120, y=180)
        log_btn2.place(x=340, y=180)
        self.logwin.mainloop()

    def first_file(self):
        global users_list
        global users_dict
        try:
            z=open("users.uzr", "rb")
        except:
            z=open("users.uzr", "w")
            z.close()
            z=open("users.uzr", "rb")
        try:
            users_list= pickle.load(z)
        except:
            users_list= []
        try:
            users_dict= pickle.load(z)
        except:
            users_dict= {}
        z.close()

    def sign_up(self):
        global users_list
        global users_dict

        i= self.log_ent1.get()
        j= self.log_ent2.get()

        if not i in users_list:
            users_list.append(i)
            users_dict[i]= j
            tkinter.messagebox.showinfo(title="done", message="the user has been made")
        else:
            tkinter.messagebox.showwarning(title="error", message="this username already existed,\nnote that the password was not changed")
    
    def log_in(self):
        global god_list
        global god_dict
        global god_check
        global god_dati
        global users_list
        global users_dict
        global a

        i= self.log_ent1.get()
        j= self.log_ent2.get()

        if i in users_list:
            if j == users_dict[i]:
                a= i
                self.logwin.destroy()
                try:
                    z= open(f"{a}.bkz", "r")
                except:
                    z= open(f"{a}.bkz", "w")
                z.close()



                z = open(f"{a}.bkz", "rb")
                try:
                    god_list = pickle.load(z)
                except:
                    god_list = []
                try:
                    god_dict = pickle.load(z)
                except:
                    god_dict = {}
                try:
                    god_check = pickle.load(z)
                except:
                    god_check = {}
                try:
                    god_dati = pickle.load(z)
                except:
                    god_dati = {}
        
                z.close()


                Firstpage()


                z = open(f"{a}.bkz", "wb")
                pickle.dump(god_list, z)
                pickle.dump(god_dict, z)
                pickle.dump(god_check, z)
                pickle.dump(god_dati, z)
                z.close()
                self.last_file()

            else:
                tkinter.messagebox.showwarning(title="error", message="the password is wrong")
        else:
            tkinter.messagebox.showwarning(title="error", message="no such username found")
    
    def last_file(self):
        global users_list
        global users_dict
        global a

        z= open("users.uzr", "wb")
        pickle.dump(users_list, z)
        pickle.dump(users_dict, z)
        z.close()

a = Logpage()

