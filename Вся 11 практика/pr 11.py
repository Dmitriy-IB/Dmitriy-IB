from tkinter import *
from tkinter import ttk, filedialog, messagebox

def calculate():
    try:
        n1 = float(calc1.get()) # первое число в калькуляторе
        n2 = float(calc2.get()) # второе число в калькуляторе
        operacia = oper.get() # операция + - * /
        if operacia == '+':
            result = n1 + n2
        elif operacia == '-':
            result = n1 - n2
        elif operacia == '*':
            result = n1 * n2
        elif operacia == '/':
            if n2 == 0:
                messagebox.showerror('Ахтунг', 'Делить на 0 нельзя')
            result = n1 / n2
        messagebox.showinfo('Результат', f'Результат: {result}')
    except ValueError:
        messagebox.showerror("Ахтунг", "Введите числа")

def vibor_chec():
    vibor = [] # пустой список
    if perv.get() == 1:
        vibor.append("Вариант 1")
    if vtor.get() == 1:
        vibor.append("Вариант 2")
    if tret.get() == 1:
        vibor.append("Вариант 3")
    if vibor:
        messagebox.showinfo("Ваш выбор", f'Вы выбрали: {vibor}')
    else:
        messagebox.showinfo("Ваш выбор", "Вы ничего не выбрали")

def otr_file():
    yourfile = filedialog.askopenfilename() # открытие диалогового окна для выбора файла
    if yourfile:
        try:
            with open(yourfile, 'r', encoding='utf-8') as file: # encoder - процедура, помогающая преобразовывать файл в компьютерный язык
                text = file.read()
                text_zone.delete('1.0', END) # очищает текстовое поле
                text_zone.insert(END, text) # вставляет в текстовое поле
        except:
            messagebox.showerror('Ахтунг', 'Файл не удалось открыть')

root = Tk()
root.title('Джамалов Дмитрий Максимович')
root.geometry('400x300+750+375')
root.resizable(False, False)

win = ttk.Notebook() # отдельное окно в ткинтер
win.pack(expand=True, fill=BOTH)

calc = Frame(win)
calc.config(bg='#38A6E5')
win.add(calc, text='Калькулятор')
calc1 = ttk.Entry(calc) # поле для ввода однострочного текста
calc1.pack(side=LEFT)
operations = ['+', '-', '*', '/']
oper = StringVar()
oper.set(operations[0])
vibor_deistv = OptionMenu(calc, oper, *operations) # кнопки действия
vibor_deistv.config(bg='#4795B6')
vibor_deistv.pack(side=LEFT)
calc2 = ttk.Entry(calc)
calc2.pack(side=LEFT)
ravn = Button(calc, text='=', command=calculate, width=2) # кнопка =
ravn.config(bg='#2D799A')
ravn.pack(side=LEFT)

chec = Frame(win)
chec.config(bg='#3F9C2C')
win.add(chec, text='Три чекбокса')
perv = IntVar() # переменная для хранения целочисленных значений в Tkinter
but_perv = Checkbutton(chec, text="Первый", variable=perv)
but_perv.config(bg='#197622')
but_perv.pack(anchor=N)
vtor = IntVar()
but_vtor = Checkbutton(chec, text="Второй", variable=vtor)
but_vtor.config(bg='#197622')
but_vtor.pack(anchor=W)
tret = IntVar()
but_tret = Checkbutton(chec, text="Третий", variable=tret)
but_tret.config(bg='#197622')
but_tret.pack(anchor=E)
butt = Button(chec, text="Ваш выбор", command=vibor_chec)
butt.config(bg='#197622')
butt.pack(anchor=N)

text = Frame(win)
text.config(bg='#712779')
win.add(text, text='Работа с текстом')
text_zone = Text(text, width=40, height=15, wrap=WORD)
text_zone.pack()
but_zone = Button(text, text="Загрузить текст из файла", command=otr_file)
but_zone.config(bg='#E991F3')
but_zone.pack()
win.pack()

root.mainloop()