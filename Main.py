from tkinter import *
from PIL import Image, ImageTk

global img, imgobj, imgobj_2, img_2, imgobj_3, img_3, imgobj_4, img_4, imgobj_5, img_5, imgobj_6, img_6

def scheme():
    global img, imgobj, imgobj_2,img_2, imgobj_3, img_3, imgobj_4, img_4, imgobj_5, img_5, imgobj_6, img_6
    img = ImageTk.PhotoImage(Image.open("Элементы ГТУ\Турбины и турбинное оборудование\Турбина гидравлическая.png"))
    c.itemconfigure(imgobj, image=img, anchor="nw")
    img_2 = ImageTk.PhotoImage(Image.open("Элементы ГТУ\Котлы и камеры сгорания\Котел, камера сгорания ГТУ.png"))
    c.itemconfigure(imgobj_2, image=img_2, anchor="nw")
    img_3 = ImageTk.PhotoImage(Image.open("Элементы ГТУ\Арматура и линии трубопроводов\Циркуляционная вода.png"))
    c.itemconfigure(imgobj_3, image=img_3, anchor="nw")
    img_4 = ImageTk.PhotoImage(Image.open("Элементы ГТУ\Насосы, тяго-дутьевые машины и электрооборудование\Генератор трехфазного тока.png"))
    c.itemconfigure(imgobj_4, image=img_4, anchor="nw")
    img_5 = ImageTk.PhotoImage(Image.open("Элементы ГТУ\Турбины и турбинное оборудование\Конденсатор поверхностный.png"))
    c.itemconfigure(imgobj_5, image=img_5, anchor="nw")
    img_6 = ImageTk.PhotoImage(Image.open("Элементы ГТУ\Насосы, тяго-дутьевые машины и электрооборудование\Насос.png"))
    c.itemconfigure(imgobj_6, image=img_6, anchor="nw")

root = Tk()
root.title("Тренажерный комплекс газотурбинной установки")
root.geometry("1350x671+0+0")

main_menu = Menu(root)
main_menu.add_cascade(label="Схемы", command=scheme)
main_menu.add_cascade(label="Выход", command=root.destroy)
root.config(menu=main_menu)

frame=Frame(root,bg="white",bd=5)
frame.place(width="1350",height="671")

c = Canvas(root, width="450",height="400")
imgobj = c.create_image(260, 80)
imgobj_2 = c.create_image(60, 120)
imgobj_3 = c.create_image(313, 150)
imgobj_4 = c.create_image(390, 130)
imgobj_5 = c.create_image(260, 260)
imgobj_6 = c.create_image(160, 350)
c.place(x=0, y=0)

root.mainloop()