"""PLM-applicatie GUI module"""
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox, simpledialog

#import functie van module second.
from main_1 import add_style
from main_1 import get_style_ids
from main_1 import delete_style

root = tk.Tk()
root.title("PLM-applicatie")
root.columnconfigure(0, weight=1)
root.geometry("800x600")


#Text variabel aan label en label frame dynamisch tekst verandering van titel voor style imputs.
text_frame_1 = tk.StringVar(value="Custom settings")
text_var = ttk.Label(root, textvariable=text_frame_1, font=("arial", 11, "bold"))
frame_style_input = tk.LabelFrame(root, labelwidget=text_var)
frame_style_input.grid(padx=10, sticky=(tk.E + tk.W))
frame_style_input.columnconfigure(0, weight=1)
text_frame_1.set("Add new clothing piece")

#Text variabel aan label en label frame dynamisch tekst verandering van titel van delete style.
text_frame_2 = tk.StringVar(value="Custom settings")
text_var = ttk.Label(root, textvariable=text_frame_2, font=("arial", 11, "bold"))
delete_choice= tk.LabelFrame(root, labelwidget=text_var)
delete_choice.grid(padx=10, sticky=(tk.E + tk.W))
delete_choice.columnconfigure(1, weight=1)
text_frame_2.set("Delete style")

#Label en Entries
label_style_id = tk.Label(frame_style_input, text="Style ID")
label_style_id.grid(column=1, row=2, padx=10, pady=10)
button_style_id = tk.Entry(frame_style_input)
button_style_id.grid(column=2, row=2, padx=10, pady=10)

label_style_name = tk.Label(frame_style_input, text="Style name")
label_style_name.grid(column=1, row=3, padx=10, pady=10)
entry_style_name = tk.Entry(frame_style_input)
entry_style_name.grid(column=2, row=3, padx=10, pady=10)

choice_product_type = ("Jackets", "Shirts", "Pants", "Shorts", "Sweaters", "Vests")
label_product_type = tk.Label(frame_style_input, text="Product type")
label_product_type.grid(column=1, row=4, padx=10, pady=10)
button_product_type = ttk.Combobox(frame_style_input, values=choice_product_type)
button_product_type.grid(column=2, row=4, padx=10, pady=10)

choice_textile = (
    "Organic Cotton", "Recycled Polyester (rPET)", "Hemp",
    "Tencel™ (Lyocell)", "Recycled Nylon", "Merino Wool"
    "Alpaca Wool", "Corozo", "Piñatex®", "Econyl®"
    "Polartec® Power Air™", "Yulex® Natural Rubber", "Recycled Wool"
    "SeaCell™", "Kapok", "Bamboo Lyocell", "Cork", "Upcycled Denim"
    "WOOL+PLA", "Soy Silk Fiber)"
)
label_textiles = tk.Label(frame_style_input, text="Textile(s)")
label_textiles.grid(column=1, row=5, padx=10, pady=10)
button_textiles = ttk.Combobox(frame_style_input, values=choice_textile)
button_textiles.grid(column=2, row=5,  padx=10, pady=10)

#text label met wat de sizes input moet aan houden.
choice_size_range = ("Mens", "Womens")
label_size_range = tk.Label(frame_style_input, text="Size range")
label_size_range.grid(column=1, row=6,  padx=10, pady=10)
button_size_range = ttk.Combobox(frame_style_input, values=choice_size_range)
button_size_range.grid(column=2, row=6,  padx=10, pady=10)

label_example_text = tk.Label(frame_style_input, text="(S,M,L,XL clothing or 30,32,34,36 pants e.g.)")
label_example_text.grid(column=3, row=7)

label_sizes = tk.Label(frame_style_input, text="Sizes")
label_sizes.grid(column=1, row=7, padx=10, pady=10)
button_sizes = tk.Entry(frame_style_input)
button_sizes.grid(column=2, row=7, padx=10, pady=10)

label_remarks = tk.Label(frame_style_input, text="Remarks")
label_remarks.grid(column=1, row=8, padx=10, pady=10)
button_remarks = tk.Text(frame_style_input, width=30, height=5)
button_remarks.grid(column=2, row=8, padx=10, pady=10)


label_delete_style = tk.Label(delete_choice, text="Delete style")
label_delete_style.grid(column=0, row=6,  padx=10, pady=10)
button_delete_style = ttk.Combobox(delete_choice, values=get_style_ids())
button_delete_style.grid(column=1, row=6,  padx=10, pady=10)

def save_data():
    style_id = button_style_id.get().strip()
    style_name = entry_style_name.get().strip()
    product_type = button_product_type.get().strip()
    textiles = button_textiles.get().strip()
    size_range = button_size_range.get().strip()
    sizes = button_sizes.get().strip()
    remarks = button_remarks.get("1.0", "end-1c").strip()

    if not style_id or not style_name:
        messagebox.showinfo("Error", "Please fill in Style ID and Style name")

    add_style(style_id, style_name, product_type, textiles, size_range, sizes, remarks)
    messagebox.showinfo("Success", f"Data for style {style_id} saved successfully.")

def clear_fields():
    button_style_id.delete(0, tk.END)
    entry_style_name.delete(0, tk.END)
    button_product_type.set('')
    button_textiles.set('')
    button_size_range.set('')
    button_sizes.delete(0, tk.END)
    button_remarks.delete("1.0", tk.END)

def delete_data():
    selected_style_id = button_delete_style.get()
    deleted = delete_style(selected_style_id)
    if deleted:
        messagebox.showinfo("Success", f"Style ID {selected_style_id} has been deleted.")
    else:
        messagebox.showinfo("Info", f"Style ID {selected_style_id} not found.")

    button_delete_style.set('')
    button_delete_style['values'] = get_style_ids()

#Save button and clear filled record button.
save_to_csv = tk.Button(frame_style_input, text="SAVE", command=save_data)
save_to_csv.grid(column=1, row=10, padx=10, pady=10)
clear_button = tk.Button(frame_style_input, text="CLEAR", command= clear_fields)
clear_button.grid(column=2, row=10, padx=10, pady=10)

#Delete button.
delete_record_csv = tk.Button(delete_choice, text="DELETE", command=delete_data)
delete_record_csv.grid(column=2, row=10)



root.mainloop()


