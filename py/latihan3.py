import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo

# Instalasi
window = tkinter.Tk()
window.configure(bg="white")
window.geometry("400x200")
window.resizable(False,False)
window.title("Pendaftaran Menikah")

# Variable dan Function
NAMA_LENGKAP = tkinter.StringVar()
ALAMAT_RUMAH = tkinter.StringVar()
JENIS_KELAMIN = tkinter.StringVar()
UMUR = tkinter.StringVar()
NOMOR_INDUK_KEPENDUDUKAN = tkinter.IntVar()

# Fungsi Tombol
def tombol_click():
    pesan = f"Hallo {NAMA_LENGKAP.get()}, Kamu Sudah Terdaftar!"
    showinfo(title="Selamat",message=pesan)
# Frame input
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



#tombol
tombol_daftar =ttk.Button(input_frame,text="Daftar",command=tombol_click)
tombol_daftar.pack(fill="x",expand=True, padx=10,pady=10)


window.mainloop()