import tkinter
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo

# Instalasi
window = tkinter.Tk()
window.configure(bg="black")
icon_img = PhotoImage(file='C:\\Users\\Febri S\\Desktop\\Matakuliah pak fajar hardeka\\Asset\\robin.png')
window.iconphoto(False, icon_img)
window.geometry("400x300")
window.resizable(False,False)
window.title("Pendaftaran Menikah")

#Header
header_label = ttk.Label(window, text="Form Pengisian", font=(15), background="red", foreground="black")
header_label.pack(pady=15)
# Variable dan Function
NAMA_LENGKAP = tkinter.StringVar()
ALAMAT_RUMAH = tkinter.StringVar()
JENIS_KELAMIN = tkinter.StringVar()
UMUR = tkinter.StringVar()
KEWARGANEGARAAN = tkinter.StringVar()

# Fungsi Tombol
def tombol_click():
 if not NAMA_LENGKAP.get() or not ALAMAT_RUMAH.get() or not JENIS_KELAMIN.get() or not UMUR.get() or not KEWARGANEGARAAN.get():
        showinfo(title="Error!", message="Mohon Lengkapi Semua Form")
 else:
        pesan = f"Hallo {NAMA_LENGKAP.get()}, Kamu Sudah Terdaftar!"
        showinfo(title="Selamat!", message=pesan)
# Frame input
style =ttk.Style()
style.configure("Custom.TEntry", fieldbackground="white")
input_frame = ttk.Frame(window)

# Penempatan grit, pack, place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)
# Komponen nama lengkap
nama_depan_label = ttk.Label(input_frame,text="Nama Lengkap :")
nama_depan_label.pack(padx=10,fill="x",expand=True)
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_LENGKAP)
nama_depan_entry.pack(padx=10,fill="x",expand=True)

# Komponen alamat rumah
alamat_rumah_label = ttk.Label(input_frame,text="Alamat Rumah :")
alamat_rumah_label.pack(padx=10,fill="x",expand=True)
alamat_rumah_entry = ttk.Entry(input_frame,textvariable=ALAMAT_RUMAH)
alamat_rumah_entry.pack(padx=10,fill="x",expand=True)

# Komponen jenis kelamin
jenis_kelamin_label = ttk.Label(input_frame,text="Jenis Kelamin :")
jenis_kelamin_label.pack(padx=10,fill="x",expand=True)
jenis_kelamin_entry = ttk.Entry(input_frame,textvariable=JENIS_KELAMIN)
jenis_kelamin_entry.pack(padx=10,fill="x",expand=True)

# Komponen umur
umur_label = ttk.Label(input_frame,text="Umur :")
umur_label.pack(padx=10,fill="x",expand=True)
umur_entry = ttk.Entry(input_frame,textvariable=UMUR)
umur_entry.pack(padx=10,fill="x",expand=True)

# Komponen kewarganegaraan
kewarganegaraan_label = ttk.Label(input_frame,text="Kewarganegaraan :")
kewarganegaraan_label.pack(padx=10,fill="x",expand=True)
kewarganegaraan_entry = ttk.Entry(input_frame,textvariable=KEWARGANEGARAAN)
kewarganegaraan_entry.pack(padx=10,fill="x",expand=True)

#tombol
tombol_daftar =ttk.Button(input_frame,text="Daftar",command=tombol_click)
tombol_daftar.pack(fill="x",expand=True, padx=10,pady=10)


window.mainloop()