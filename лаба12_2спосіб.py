from tkinter import *
from tkinter import messagebox

def show():
    global photo
    try:
        photo = PhotoImage(file="11.gif")  # Перевір, що файл існує в тій самій папці
        label5.configure(image=photo)
        label5.image = photo  # Зберігаємо посилання на зображення
    except Exception as e:
        messagebox.showerror("Помилка", f"Не вдалося завантажити фото:\n{e}")

def inf():
    s = edit4.get().strip()
    if s == "111M":
        messagebox.showinfo("Про спеціальність", s + '\nСпеціальність 111 Математика\n'
                                                     'Освітня програма Комп’ютерна математика')
    elif s == "COM":
        messagebox.showinfo("Про спеціальність", s + '\nСпеціальність 014 Середня освіта\n'
                                                     'Освітня програма Середня освіта. Математика, інформатика')
    else:
        messagebox.showinfo("Про спеціальність", s + '\nТакої спеціальності на факультеті немає')

# Головне вікно
root = Tk()
root.title("Анкета")
root.geometry("400x600+500+100")
root['bg'] = 'gray1'

# Віджет "Прізвище"
Label(root, text="Прізвище", bg='gray1', fg='white').grid(row=0, column=0, sticky=W, padx=10, pady=5)
edit1 = Entry(root, width=30)
edit1.grid(row=0, column=1, pady=5)

# Віджет "Ім'я"
Label(root, text="Ім'я", bg='gray1', fg='white').grid(row=1, column=0, sticky=W, padx=10, pady=5)
edit2 = Entry(root, width=30)
edit2.grid(row=1, column=1, pady=5)

# Віджет "По батькові"
Label(root, text="По батькові", bg='gray1', fg='white').grid(row=2, column=0, sticky=W, padx=10, pady=5)
edit3 = Entry(root, width=30)
edit3.grid(row=2, column=1, pady=5)

# Стать
Label(root, text="Стать", bg='gray1', fg='white').grid(row=3, column=0, sticky=W, padx=10, pady=5)
checkbutton1 = Checkbutton(root, text="Ч", bg='gray1', fg='white')
checkbutton1.grid(row=3, column=1, sticky=W)
checkbutton2 = Checkbutton(root, text="Ж", bg='gray1', fg='white')
checkbutton2.grid(row=3, column=1)

# Курс
Label(root, text="Виберіть курс:", bg='gray1', fg='white').grid(row=4, column=0, sticky=W, padx=10, pady=5)
result1 = IntVar(value=1)
for i in range(1, 5):
    Radiobutton(root, text=str(i), variable=result1, value=i, bg='gray1', fg='white').grid(row=4, column=i)

# Спеціальність
Label(root, text="Спеціальність", bg='gray1', fg='white').grid(row=5, column=0, sticky=W, padx=10, pady=5)
edit4 = Entry(root, width=30)
edit4.grid(row=5, column=1, pady=5)

# Кнопка "Про спеціальність"
button1 = Button(root, text="Про спеціальність", width=20, command=inf)
button1.grid(row=6, column=0, columnspan=2, pady=10)

# Зображення
label5 = Label(root, bg='gray1')
label5.grid(row=7, column=0, columnspan=2)

# Кнопка "Фото"
button2 = Button(root, text="Фото", width=20, command=show)
button2.grid(row=8, column=0, columnspan=2, pady=10)

# Запуск програми
root.mainloop()
