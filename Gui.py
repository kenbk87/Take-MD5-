from tkinter import *
from tkinter import filedialog, Menu
import os
import hashlib


cuasochinh = Tk()
cuasochinh.title("Coded by Ken")
cuasochinh.wm_iconbitmap('')


def donothing():
    pass


#Hàm tính mã MD5 của file:
def generate_file_md5(rootdir, filename, blocksize=2**20):
    m = hashlib.md5()
    with open(os.path.join(rootdir, filename), "rb") as f:
        while True:
            buf = f.read(blocksize)
            if not buf:
                break
            m.update(buf)
    return m.hexdigest()


def thoat():
    cuasochinh.quit()


#Liệt kê các file trong thư mục được chọn, hiển thị nội dung lên của sổ Text:
def hienthi():
    dd = filedialog.askdirectory()
    ds = os.listdir(dd)
    dem = 1
    for i in ds:
        #Sử dụng đường dẫn tuyệt đối
        dd_tuyet_doi = os.path.join(dd, i)

        #Kiểm tra có phải là tập tin hay không:
        if os.path.isfile(dd_tuyet_doi):
            noidung.insert(INSERT, '-' + str(dem) +': ' + str(i) + ', dung lượng: ' + str(os.path.getsize(dd_tuyet_doi)) + ' Bytes \n')
            ma_md5 = generate_file_md5(dd, str(i), blocksize=2**20)
            noidung.insert(INSERT, "    Mã MD5: " + ma_md5 + '\n')
            dem = dem + 1


def quet():
    pass


#Hàm để xóa nội dung trong ô text:
def xoa():
    noidung.delete('1.0', END)


def luu():
    pass


def xem():
    pass
    # o_dia = sys.



frame1 = Frame()
lb1 = Label(frame1, text="Choose a folder which contain files:")
lb1.pack(side=LEFT)

chon = Button(frame1, text="Choose", command=hienthi, width=10, padx=5, pady=5)
chon.pack(side=LEFT)

xoa = Button(frame1, text="Delete", command=xoa, width=10, padx=5, pady=5)
xoa.pack(side=LEFT)

luu = Button(frame1, text="Save", command=luu, width=10, padx=5, pady=5)
luu.pack(side=LEFT)

quet = Button(frame1, text="Find", command=quet, width=10, padx=5, pady=5)
quet.pack(side=LEFT)

xem = Button(frame1, text="View", command=xem, width=10, padx=5, pady=5)
xem.pack(side=LEFT)

frame1.grid(row=0,  columnspan=2,  padx=5, pady=5)

lb2 = Label(cuasochinh, text="Danh sách các tập tin có trong thư mục: ")
lb2.grid(row=1, column=0)

noidung = Text(cuasochinh, width=100, height=25)
noidung.grid(columnspan=2, row=1)

cuasochinh.resizable(width='FALSE', height='FALSE')
#Khai báo 1 Menu của của sổ chính:
menu1 = Menu(cuasochinh)
cuasochinh.config(menu=menu1)

#Khai báo các sub Menu:
subMenu1 = Menu(menu1)
subMenu2 = Menu(menu1)
subMenu3 = Menu(menu1)

#Đặt tên cho các subMenu:
menu1.add_cascade(label="File", menu=subMenu1)
menu1.add_cascade(label="Edit", menu=subMenu2)
menu1.add_cascade(label="About", menu=subMenu3)

#Thêm các mục trong mỗi subMenu:
subMenu1.add_command(label="Open", command=donothing())
subMenu1.add_command(label="Save", command=donothing())
subMenu1.add_separator()
subMenu1.add_command(label="Exit", command=thoat())

cuasochinh.mainloop()

