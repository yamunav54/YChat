import tkinter, sqlite3
db = "YChat.db"
usr, pwd = None, None

win = tkinter.Tk()
win.title("Signup Window")

user_label = tkinter.Label(win, text="User Id")
user_txt = tkinter.Text(win, height=1)
user_label.pack()
user_txt.pack()

pwd_label = tkinter.Label(win, text="Password")
pwd_txt = tkinter.Text(win, height=1)
pwd_label.pack()
pwd_txt.pack()

def insert_new_user():
    dbcon = sqlite3.connect(db)
    cur = dbcon.cursor()
    query = "insert into auth values ( '%s', '%s' )"
    usr = user_txt.get('1.0', tkinter.END).strip()
    pwd = pwd_txt.get('1.0', tkinter.END).strip()
    query = query%(usr, pwd)
    print(query)
    cur.execute(query)
    cur.execute("commit")
    

signup_button = tkinter.Button(win, text="Signup", command=insert_new_user)
signup_button.pack()



tkinter.mainloop()
