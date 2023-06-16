import tkinter

window = tkinter.Tk()

labelNama = tkinter.Label(window, text= "Febri Sarif Hidayat")
labelKampus = tkinter.Label(window, text= "Kampus STIMIK Tunas Bangsa")
labelSemester = tkinter.Label(window, text= "Semester 4")
labelProdi = tkinter.Label(window, text= "Prodi Teknik Informatika A")


labelNama.grid(row=0, column=0)
labelKampus.grid(row=1, column=1)
labelSemester.grid(row=2, column=0)
labelProdi.grid(row=3, column=1)
window.mainloop()

#grit dan kolom#