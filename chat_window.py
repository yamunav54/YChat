import tkinter
win=tkinter.Tk()
win.title("chat")
history_txt=tkinter.Text(win)
history_txt.pack()
msg_txt=tkinter.Text(win,height=1)
msg_txt.pack()
def send_msg():
    global msg_txt
    msg=msg_txt.get('1.0',tkinter.END).strip()
    history_txt.insert(tkinter.CURRENT,msg)
    msg_txt.grid_remove()
    msg_txt = tkinter.Text(win,height=1)
submit_button=tkinter.Button(win,text="send",command=send_msg)
submit_button.pack()
tkinter.mainloop()
