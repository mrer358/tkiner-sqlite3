from Tkinter import *
import sqlite3
import  tkMessageBox
import threading
import time
class Start():
    def __init__(self):
        self.listV = []
        self.root = Tk()
        self.root.geometry("300x200")
        self.root.title("chat")
        self.leb = Label(self.root, text="username:")
        self.leb.place(x=20, y=20)
        self.net = Label(self.root, text="password:")
        self.net.place(x=20, y=40)
        self.ley = Entry(self.root ,bg="black",fg="green")
        self.ley.place(x=80, y=25)
        self.ley2 = Entry(self.root, show="*",bg="black",fg="green")
        self.ley2.place(x=80, y=45)
        self.butt = Button(self.root, text="login",bg="black",fg="green", command=self.checkLogindata)
        self.butt.place(x=165, y=95)
        self.butt2 = Button(self.root, text="registration",bg="black",fg="green", command=self.registration)
        self.butt2.place(x=15, y=95)
        mainloop()

    def registration(self):
        self.root2 = Tk()
        self.root2.geometry("400x200")
        self.eny3 = Label(self.root2, text="first name")
        self.eny3.place(x=20, y=20)
        self.eny3 = Label(self.root2, text="lest name")
        self.eny3.place(x=20, y=40)
        self.eny3 = Label(self.root2, text="email")
        self.eny3.place(x=20, y=60)
        self.eny3 = Label(self.root2, text="password")
        self.eny3.place(x=20, y=80)
        self.eny3 = Label(self.root2, text="second password")
        self.eny3.place(x=20, y=100)
        self.br1 = Entry(self.root2,bg="black",fg="green")
        self.br1.place(x=80, y=20)
        self.br2 = Entry(self.root2,bg="black",fg="green")
        self.br2.place(x=80, y=40)
        self.br3 = Entry(self.root2,bg="black",fg="green")
        self.br3.place(x=80, y=60)
        self.br4 = Entry(self.root2, show="*",bg="black",fg="green")
        self.br4.place(x=80, y=80)
        self.br5 = Entry(self.root2, show="*",bg="black",fg="green")
        self.br5.place(x=120, y=100)
        self.butt3 = Button(self.root2, text="register",bg="black",fg="green", command=self.checkregisterion)
        self.butt3.place(x=195, y=150)

    def checkregisterion(self):
        firstname = self.br1.get()
        lesttname = self.br2.get()
        email = self.br3.get()
        password = self.br4.get()
        password2 = self.br5.get()
        self.conn = sqlite3.connect("myweb.db")
        self.c = self.conn.cursor()
        self.c.execute(
            '''create table if not exists michael5(id integer primary key autoincrement,   firstname varchar(100),lestname varchar(200), email varchar(200), friends  varchar(255),password varchar(200),scuondpasssowrd varchar(200))''')

        self.c.execute("insert into michael5(firstname,lestname,email,password,scuondpasssowrd)  values " + str((firstname, lesttname, email, password, password2)))

        sql = "select * from michael5"
        self.c.execute(sql)
        ssss = self.c.fetchall()
        for u in ssss:
            print u
        self.conn.commit()
        tkMessageBox._show("chat", "thank for registerion")

    def checkLogindata(self):
        self.userlog = self.ley.get()
        passwordlog = self.ley2.get()
        self.conn2 = sqlite3.connect("myweb.db")
        self.cc = self.conn2.cursor()
        fe = "select * from michael5 WHERE firstname = "
        fe2 = "and password="
        #print self.userlog
        gg = self.userlog
        gg2= passwordlog

        da =self.cc.execute(fe + ("'"+gg+"'")+fe2+("'"+ gg2 +"'"))
        da2 = self.cc.fetchone()
        self.google2 = self.userlog + "_table"
        if da2 is None:
            tkMessageBox._show("sorry", "the username or the password are not corrct")
        else:
            tkMessageBox._show("login", "you are login user "+ self.userlog)
            self.chat_root()
        for v in da:
            print v

    def searchdbfriends(self):

        self.searchlist.delete(END, END)
        self.searchdata = self.searchbox.get()
        self.conn3= sqlite3.connect("myweb.db")
        self.ccc = self.conn3.cursor()

        self.searchlist.delete(END, END)
        sql2 = "select firstname,email from  michael5 WHERE firstname = "+ str("'"+self.searchdata+"'")
        sql3  = "select firstname from  michael5 WHERE firstname = "+ str("'"+self.searchdata+"'")
        a2 = self.ccc.execute(sql2)
        google = a2.fetchone()
        if google is None:
            tkMessageBox._show("chat", "the user not Existing")
        af =tkMessageBox.askyesno("add this user",google)
        self.ffff = []
        if af == True:
            self.google2 = self.userlog + "_table"
            print self.google2
            gg=self.ccc.execute("PRAGMA table_info(tbl_name)")
            for ggv in gg:
                print ggv
            a=self.ffff.append(self.google2)
            print a
            self.searchlist.delete(END, END)
            #self.ccc.execute("delete  from "+self.google2)
            #a3 = self.ccc.execute("insert into michael5(email) values(" + str(searchdata) + ")")
            self.ccc.execute("create table if not exists "+self.google2+" (id integer primary key autoincrement,   friends varchar(100),massege varchar(200))")
            self.conn3.commit()
            #self.ccc.execute("insert into "+"google"+"(friends) values (?)" , (self.searchdata, ) )
            self.conn3.commit()
            ad = self.ccc.execute("select friends from "+self.google2)

            #for ff in ad:
               # print ff

            tt = self.cccc.execute("insert into "+self.google2+"(friends)  values(?)", (self.searchdata,))
            self.conn3.commit()
            ds = self.cccc.execute("select friends from " + self.google2)
            #print self.searchdata
            self.dss = ds.fetchall()
            self.conn3.commit()


            self.searchlist.delete(END, END)
            for fg in self.dss:

                print fg
                self.searchlist.delete(END, END)

                self.listV.append(fg)

            for gh,fc in enumerate(self.listV):
                #print gh
                vv = gh,fc
                self.listV = []
                self.searchlist.insert(gh,vv)

        self.listV = []       #gj =self.cccc.execute("select *from " +self.searchdata)
        self.searchlist.delete(END,END)


        if af == False:
            pass
    def friendsdatamassege(self):
        #print self.google2
        self.text.delete(1.0, END)

        self.conn5 = sqlite3.connect("myweb.db")
        self.ccccc = self.conn5.cursor()
        self.facebook = self.elbg.get()
        self.text.delete(END, END)
        self.ccccc.execute("insert into " + self.google2 + "(massege) values(?) ", (self.facebook,))
        self.conn5.commit()
        gb =self.ccccc.execute("select massege from "+self.google2)
        gt = gb.fetchall()

        for jj in gt:
            print jj
            vg = jj,"\n"

            for f, jj in enumerate(jj):
                self.text.insert(END,vg)

    def chat_root(self):
        self.root3 = Tk()
        self.root3.geometry("700x800")
        self.root3.title("chat login "+self.userlog)
        self.searchbox = Entry(self.root3,bg="black",fg="green")
        self.searchbox.place(x=500,y=40)
        self.searchlebat = Label(self.root3, text="search:")
        self.searchlebat.place(x=450,y=40)
        self.searchbouttn = Button(self.root3, text="search",bg="black",fg="green",command=self.searchdbfriends)
        self.searchbouttn.place(x=600,y=69)
        self.searchlist = Listbox(self.root3,font=40,bg="black",fg="green")
        self.searchlist.place(x=460,y=160)
        self.searchlistleb = Label(self.root3, text="friends")
        self.searchlistleb.place(x=460,y=140)
        self.text = Text(self.root3,width=50,bg="black",fg="green")
        self.text.place(x=0,y=0)
        self.elbg = Entry(self.root3, font=20,bg="black",fg="green")
        self.elbg.place(x=50,y=440)
        self.butt4 = Button(self.root3, text="send",bg="black",fg="green",command=self.friendsdatamassege)
        self.butt4.place(x=350,y=440)
        self.searchlist.delete(END, END)
        self.butt5 = Button(self.root3, command=self.bbb,text="reflash")
        self.butt5.place(x=500,y=400)
        self.searchlist.bind('<<ListboxSelect>>', self.cdcd)
        self.conn4 = sqlite3.connect("myweb.db")
        self.cccc = self.conn4.cursor()



    def bbb(self):
        self.cccc.execute("delete from "+self.google2)
        print "google"


    def cdcd(self,*e):
        listww = self.searchlist.curselection()
        for vv in listww:
            print vv



f = Start()


def main():
    f


main()
