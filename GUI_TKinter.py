"""PLM-applicatie GUI module"""
import tkinter as tk
from tkinter import ttk
import csv
from pathlib import Path


root = tk.Tk()
root.title("PLM-applicatie")
root.geometry("800x500")


#Text variable assigned to label
text = tk.StringVar(value="Custom settings")
text_var = ttk.Label(root, textvariable=text, font=("arial", 12, "bold"))


#Label frame and dynamic text change
frame_clothing = tk.LabelFrame(root, labelwidget=text_var)
frame_clothing.grid()
text.set("Add new clothing piece")


#labels for data entry with associated buttons.
label_style_id = tk.Label(frame_clothing, text="Style ID")
label_style_id.grid(column=1, row=2)
button_style_id = tk.Entry(frame_clothing)
button_style_id.grid(column=2, row=2)


#Label and button for product type with dropdown list.
label_product_type = tk.Label(frame_clothing, text="Product type")
label_product_type.grid(column=1, row=3)
choice_product_type = (
    "Jackets", "Shirts", "Pants", "Shorts",
    "Sweaters", "Vests"
)
button_product_type = ttk.Combobox(frame_clothing, values=choice_product_type)
button_product_type.grid(column=2, row=3)


#Label and button for textile type with dropdown list.
label_textiles = tk.Label(frame_clothing, text="Textile(s)")
label_textiles.grid(column=1, row=4)
choice_textile = (
    "Organic Cotton", "Recycled Polyester (rPET)", "Hemp",
    "Tencel™ (Lyocell)", "Recycled Nylon", "Merino Wool"
    "Alpaca Wool", "Corozo", "Piñatex®", "Econyl®"
    "Polartec® Power Air™", "Yulex® Natural Rubber", "Recycled Wool"
    "SeaCell™", "Kapok", "Bamboo Lyocell", "Cork", "Upcycled Denim"
    "WOOL+PLA", "Soy Silk Fiber)"
)
button_textiles = ttk.Combobox(frame_clothing, values=choice_textile)
button_textiles.grid(column=2, row=4)


# NEED TO BE REVISED!!!!!
# label_textile_certifications = tk.Label(root, text="Textile certification(s)")
# label_textile_certifications.grid(column=1, row=5)
# button_textile_certifications = tk.Entry(root)
# button_textile_certifications.grid(column=2, row=5)


#Label and button for size range with dropdown list.
label_size_range = tk.Label(frame_clothing, text="Size range")
label_size_range.grid(column=1, row=5)
label_example_text = tk.Label(frame_clothing, text="(S,M,L,XL clothing or 30,32,34,36 pants e.g.)")
label_example_text.grid(column=2, row=7)
choice_size_range = ("Mens", "Womens")
button_size_range = ttk.Combobox(frame_clothing, values=choice_size_range)
button_size_range.grid(column=2, row=5)


#Label and button for sizes.
label_sizes = tk.Label(frame_clothing, text="Sizes")
label_sizes.grid(column=1, row=6)
button_sizes = tk.Entry(frame_clothing)
button_sizes.grid(column=2, row=6)


#Save button and clear filled record button
save_to_csv = tk.Button(frame_clothing, text="SAVE")
save_to_csv.grid(column=1, row=10)
clear_fields = tk.Button(frame_clothing, text="CLEAR")
clear_fields.grid(column=2, row=10)


#Delete button.
delete_record_csv = tk.Button(root, text="DELETE")
delete_record_csv.grid(column=2, row=10)



root.mainloop()


