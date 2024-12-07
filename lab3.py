# Вариант 4

from tkinter import *
import random

def make_window():
    root = Tk()
    root.geometry('1295x725')
    root.title("Undertale Key Generation")
    bg_image = PhotoImage(file="img.png")
    label_bg = Label(root, image=bg_image)
    label_bg.place(x=0, y=0, relwidth=1, relheight=1)
    label_bg.image = bg_image
    return root

def char_weight_generation():
    numbers = [i for i in range(1, 27)]
    dict_char_weight = {}
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        num = random.choice(numbers)
        dict_char_weight[letter] = num
        numbers.remove(num)
    return dict_char_weight

def key_one_unit_generation():
    dict_char_weight = char_weight_generation()
    unit = ''
    weight = 0
    for _ in range(4):
        rand_letter = random.choice(list(dict_char_weight))
        unit += rand_letter
        weight += dict_char_weight[rand_letter]
    return unit, weight
    
def interval_generation():
    start = random.randint(4, 26*4+1)
    stop = random.randint(start, 26*4+1)
    return start, stop

def key_generation():
    start, stop = interval_generation()
    key = []
    while len(key) < 3:
        unit, weight = key_one_unit_generation()
        if start <= weight <= stop:
            key.append(unit)
    return '-'.join(key)

def pr_key():
    label_key = Label(window, text=key_generation(), bg="red")
    label_key.place(x=520, y=650, relwidth=0.2, relheight=0.05)
    image_flowey = PhotoImage(file="flowey.png")
    label_flowey = Label(window, image=image_flowey)
    label_flowey.place(x=600, y=380, relwidth=0.081, relheight=0.14)
    label_flowey.image = image_flowey

def btn():
    btn = Button(window, text='Сгенерировать ключ', command=pr_key)
    btn.place(x=520, y=600, relwidth=0.2, relheight=0.05)

window = make_window()
btn()
window.mainloop()