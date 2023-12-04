# בס״ד

from tkinter import Tk, Entry, Label, Button

from PIL import Image, ImageTk

PADX = 5
PADY = 10
FONT = ('Arial', 12)


def miles_to_km():
    km_value = entry_field.get().replace(',', '.')
    try:
        km = abs(float(km_value))
    except ValueError:
        return result_label.config(text='Not valid input')
    else:
        miles_value = round(km * 1.60934, 3)
        return result_label.config(text=f'{miles_value}')


converter = Tk()
converter.minsize(height=100, width=200)
converter.title('Mile to Kilometer Converter')
converter.config(padx=20, pady=20, bg='white')

ico = Image.open('icon.png')
photo = ImageTk.PhotoImage(ico)
converter.wm_iconphoto(False, photo)

entry_field = Entry(width=15)
entry_field.grid(column=1, row=0, padx=PADX, pady=PADY, ipady=6)

miles_label = Label(text='Miles', font=FONT)
miles_label.grid(column=2, row=0, padx=PADX, pady=PADY)
miles_label.config(bg='white')

equal_label = Label(text='is equal to', font=FONT)
equal_label.grid(column=0, row=1, padx=PADX, pady=PADY)
equal_label.config(bg='white')

result_label = Label(width=15, text='0', font=FONT)
result_label.grid(column=1, row=1, padx=PADX, pady=PADY)
result_label.config(bg='white')

km_label = Label(text='Km', font=FONT)
km_label.grid(column=2, row=1, padx=PADX, pady=PADY)
km_label.config(bg='white')

calculate_button = Button(text='Calculate', command=miles_to_km)
calculate_button.grid(column=1, row=2, padx=PADX, pady=PADY)
calculate_button.config(bg='orange', font=FONT)

converter.mainloop()
