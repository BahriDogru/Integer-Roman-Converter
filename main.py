import tkinter as tk


#integer to roman numbers
def int_to_roman(number_entry):
    int_number = int(number_entry)

    # Storing roman values of digits from 0-9
    # when placed at different places
    m = ["", "M", "MM", "MMM", "MMMM", "MMMMM"]
    c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM "]
    x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]

    # Converting to roman
    thousands = m[int_number // 1000]
    hundreds = c[(int_number % 1000) // 100]
    tens = x[(int_number % 100) // 10]
    ones = i[int_number % 10]

    roman_number = (thousands + hundreds +
                    tens + ones)
    result_label.config(text=f"{int_number} = {roman_number}")


def roman_to_int(string_entry):
    roman_number = string_entry.upper()
    roman_number_list_input = []
    roman_number_list = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for char in roman_number:
        roman_number_list_input.append(char)

    total = 0
    prev_total = 0
    roman_number_list_input.reverse()

    for num in roman_number_list_input:
        value = roman_number_list[num]

        if value < prev_total:
            total -= value
        else:
            total += value

        prev_total = value
    result_label.config(text=f"{roman_number} = {total}")


# Ana pencereyi oluşturma
root = tk.Tk()
root.title("Input Example")
root.geometry("300x300")

# Sayı girişi için etiket ve giriş alanı
tk.Label(root, text="Number:").grid(row=0, column=3, padx=10, pady=10)
number_entry = tk.Entry(root)
number_entry.grid(row=0, column=4, padx=10, pady=10)

# Metin girişi için etiket ve giriş alanı
tk.Label(root, text="String:").grid(row=1, column=3, padx=10, pady=10)
string_entry = tk.Entry(root)
value = string_entry.get()

string_entry.grid(row=1, column=4, padx=10, pady=10)

# Gönder butonu
submit_button = tk.Button(root, text="Submit Roman Number", command=lambda: roman_to_int(string_entry.get()))
submit_button.grid(row=2, column=4, columnspan=2, pady=10)

submit_button = tk.Button(root, text="Submit Number", command=lambda: int_to_roman(number_entry.get()))
submit_button.grid(row=3, column=4, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=4, columnspan=2, pady=10)


# Tkinter ana döngüsünü başlatma
root.mainloop()




