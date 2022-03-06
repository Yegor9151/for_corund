from tkinter import *
import main

root = Tk()

user_frame = Frame()
user_frame.pack()

Label(user_frame, text="Path to token").grid(column=0, row=0)
Label(user_frame, text="Owner id").grid(column=0, row=1)
Label(user_frame, text="Post count").grid(column=0, row=2)

token_path = Entry(user_frame)
owner_id = Entry(user_frame)
past_count = Entry(user_frame)

token_path.grid(column=1, row=0)
owner_id.grid(column=1, row=1)
past_count.grid(column=1, row=2)


def close():
    root.destroy()
    raise SystemExit


def clear():
    token_path.delete(0, END)
    owner_id.delete(0, END)
    past_count.delete(0, END)


Button(text="Close", command=close).pack(side=RIGHT)
Button(text="Clear", command=clear).pack(side=RIGHT)
Button(text="Start", command=lambda: main.run(
    path=token_path.get(),
    owner_id=int(owner_id.get()),
    posts=int(past_count.get())
)).pack(side=RIGHT)

root.mainloop()

"""
E:\\token.txt
44273004
"""
