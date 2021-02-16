import tkinter as tk
from ocr import fileSearch
from PIL import ImageTk,Image





h=480
w=720
root=tk.Tk()

canvas=tk.Canvas(root,height=h,width=w)
canvas.pack()

bg_img=ImageTk.PhotoImage(Image.open("bg.jpg"))
bg_lbl=tk.Label(root,image=bg_img)
bg_lbl.place(relwidth=1,relheight=1)

upper_frame=tk.Frame(root,bg='#99ff99',bd=4)
upper_frame.place(relx=0.05,rely=0.05,relheight=0.3,relwidth=0.9)

label_path=tk.Label(upper_frame,text='Enter directory path :')
label_path.place(relx=0.03,rely=0.05,relwidth=0.4,relheight=0.4)

label_text=tk.Label(upper_frame,text='Enter text to search :')
label_text.place(relx=0.03,rely=0.55,relwidth=0.4,relheight=0.4)

entry_path=tk.Entry(upper_frame,font=('courier',20))
entry_path.place(relx=0.45,rely=0.05,relwidth=0.54,relheight=0.4)

entry_text=tk.Entry(upper_frame,font=('courier',20))
entry_text.place(relx=0.45,rely=0.55,relwidth=0.54,relheight=0.4)

search_button=tk.Button(root,text='Search',command=lambda:fileSearch(entry_text.get(),entry_path.get()))
search_button.place(relx=0.4,rely=0.36,relwidth=0.2,relheight=0.05)

root.mainloop()