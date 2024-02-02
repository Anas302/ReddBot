import tkinter as tk
from InstaBot import login_into_instagram_and_upload_images


class Application(tk.Frame):
    disapproved = False

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.approve = tk.Button(self, text="\n      APPROVE      \n", fg="white", bd=5, bg="green", font="calibri", command=self.approve)
        self.approve.pack(side="left")

        self.disapprove = tk.Button(self, text="\n    DISAPPROVE    \n", fg="white",bd=5, bg="red", font="calibri", command=self.disapprove)
        self.disapprove.pack(side="right")

        self.quit = tk.Button(self, text="\n   Quit   \n", fg="red", bd=3, font="calibri", command=self.master.destroy)
        self.quit.pack()

        self.canvas = tk.Canvas(self.master, width=750, height=750)
        self.canvas.place(x=150, y=150)
        self.img = tk.PhotoImage(file="mainpost.png")
        self.canvas.create_image(50, 50, anchor=tk.NW, image=self.img)

    def approve(self):
        self.master.destroy()
        Application.disapproved = False
        print("-=-=-=--=--=-=-=-=-=-=-=-=-=-   APPROVED ✅  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        login_into_instagram_and_upload_images(image="mainpost.jpg")

    def disapprove(self):
        self.master.destroy()
        Application.disapproved = True
        print("-=-=-=--=--=-=-=-=-=-=-=-=-=-   DISAPPROVED ❌  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")


def initate_interface():
    root = tk.Tk()
    root.geometry("1000x1000")
    app = Application(master=root)
    app.mainloop()
