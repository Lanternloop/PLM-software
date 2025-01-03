"""PLM-applicatie GUI module"""
#Importeerd tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Importeerd functies en class van main_1 module
from main_1 import get_full_collection
from main_1 import ManageStyle

root = tk.Tk()
root.title("PLM-application")
root.columnconfigure(0, weight=1)
root.geometry("750x750")

# Treeview widget voor het laten zien van toegevoegde styles
tree_frame = ttk.Frame(root)
tree_frame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

input_frame = ttk.Frame(root, padding=10)
input_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

tree = ttk.Treeview(tree_frame, columns=("Style ID", "Style Name", "Product Type"), show="headings")
tree.grid(column=0, row=0, columnspan=3, sticky=(tk.E + tk.W), padx=10, pady=10)

# Treeview columns headings.
tree.heading("Style ID", text="Style ID", anchor="center")
tree.heading("Style Name", text="Style Name", anchor="center")
tree.heading("Product Type", text="Product Type", anchor="center")

# Text variabel aan label en label frame dynamisch tekst verandering van titel voor style inputs
text_frame_1 = tk.StringVar(value="Custom settings")
text_var = ttk.Label(tree_frame, textvariable=text_frame_1, font=("arial", 11, "bold"))
frame_style_input = tk.LabelFrame(tree_frame, labelwidget=text_var)
frame_style_input.grid(row=1, column=0, columnspan=3, sticky=(tk.E + tk.W), padx=10, pady=10)
frame_style_input.columnconfigure(1, weight=1)
text_frame_1.set("Add new style")

#Text variabel aan label en label frame dynamisch tekst verandering van titel van delete style
text_frame_2 = tk.StringVar(value="Custom settings")
text_var = ttk.Label(frame_style_input, textvariable=text_frame_2, font=("arial", 11, "bold"))
delete_choice= tk.LabelFrame(frame_style_input, labelwidget=text_var)
delete_choice.grid(row=7, column=0, columnspan=3, sticky=(tk.E + tk.W), padx=10, pady=10)
delete_choice.columnconfigure(1, weight=1)
text_frame_2.set("Delete style")

#Label en Entries
label_style_name = tk.Label(frame_style_input, text="Style name")
label_style_name.grid(column=0, row=0, padx=10, pady=5, sticky=tk.W)
entry_style_name = tk.Entry(frame_style_input)
entry_style_name.grid(column=1, row=0, padx=10, pady=5, sticky="ew")

choice_product_type = ("Jackets", "Shirts", "Pants", "Shorts", "Sweaters", "Vests")
label_product_type = tk.Label(frame_style_input, text="Product type")
label_product_type.grid(column=0, row=1, padx=10, pady=5, sticky=tk.W)
button_product_type = ttk.Combobox(frame_style_input, values=choice_product_type)
button_product_type.grid(column=1, row=1, padx=10, pady=5, sticky="ew")

choice_textile = (
    "Organic Cotton", "Recycled Polyester (rPET)", "Hemp",
    "Tencel (Lyocell)", "Recycled Nylon", "Merino Wool"
    "Alpaca Wool", "Corozo", "Piñatex", "Econyl"
    "Polartec Power Air" "Yulex Natural Rubber", "Recycled Wool"
    "SeaCell", "Kapok", "Bamboo Lyocell", "Cork", "Upcycled Denim"
    "WOOL+PLA", "Soy Silk Fiber)"
    )
label_textiles = tk.Label(frame_style_input, text="Textile(s)")
label_textiles.grid(column=0, row=2, padx=10, pady=5, sticky=tk.W)
button_textiles = ttk.Combobox(frame_style_input, values=choice_textile)
button_textiles.grid(column=1, row=2, padx=10, pady=5, sticky="ew")

choice_size_range = ("Mens", "Womens")
label_size_range = tk.Label(frame_style_input, text="Size range")
label_size_range.grid(column=0, row=3, padx=10, pady=5, sticky=tk.W)
button_size_range = ttk.Combobox(frame_style_input, values=choice_size_range)
button_size_range.grid(column=1, row=3, padx=10, pady=5, sticky="ew")

choice_size = ("XXS, XS, S, M, L, XL, XXL",
               "XS, S, M, L, XL, XXL",
               "28, 30, 32, 34, 36, 38",
               "26, 28, 30, 32, 34, 36, 38"
               )
label_sizes = tk.Label(frame_style_input, text="Sizes")
label_sizes.grid(column=0, row=4, padx=10, pady=5, sticky=tk.W)
button_sizes = ttk.Combobox(frame_style_input, values=choice_size)
button_sizes.grid(column=1, row=4, padx=10, pady=5, sticky="ew")

label_remarks = tk.Label(frame_style_input, text="Remarks")
label_remarks.grid(column=0, row=5, padx=10, pady=5, sticky=tk.W)
button_remarks = tk.Text(frame_style_input, width=30, height=5)
button_remarks.grid(column=1, row=5, padx=10, pady=5, sticky="ew")

def clear_fields():
    entry_style_name.delete(0, tk.END)
    button_product_type.set('')
    button_textiles.set('')
    button_size_range.set('')
    button_sizes.set('')
    button_remarks.delete("1.0", tk.END)

def save_data():
    style_name = entry_style_name.get().strip()
    product_type = button_product_type.get().strip()
    textiles = button_textiles.get().strip()
    size_range = button_size_range.get().strip()
    sizes = button_sizes.get().strip()
    remarks = button_remarks.get("1.0", "end-1c").strip()

    # Valideerd user input
    if not style_name or not product_type or not textiles or not size_range or not sizes:
        messagebox.showinfo("Error","Please fill in all the input fields!")
        return

    # Genereerd uniek id en voegt het toe in de treeview
    new_iid = tree.insert("", tk.END, values=("", style_name, product_type, textiles, size_range, sizes, remarks))

    tree.item(new_iid, values=(new_iid, style_name, product_type, textiles, size_range, sizes, remarks))

    style = ManageStyle(
        style_id=new_iid,
        style_name=style_name,
        product_type=product_type,
        textiles=textiles,
        size_range=size_range,
        sizes=sizes,
        remarks=remarks
    )
    # Voeg de nieuwe stijl toe aan het CSV-bestand
    try:
        style.add_style()
        messagebox.showinfo("Success", f"Style with ID {new_iid} added!")
        clear_fields()
    except Exception as e:
        messagebox.showerror("Error", f"Could not save style: {e}")

def delete_data():
    selected_item = tree.selection()

    # Controleer of een stijl is geselecteerd
    if not selected_item:
        messagebox.showerror("Error", "Please select a style to delete.")
        return

    iid_to_delete = selected_item[0]
    tree.delete(iid_to_delete)

    # Verwijder de stijl uit het CSV-bestand en de Treeview
    try:
        deleted = ManageStyle.delete_style(iid_to_delete)  # Gebruik de statische methode
        if deleted:
            messagebox.showinfo("Success", f"Style with ID {iid_to_delete} deleted!")
        else:
            messagebox.showwarning("Warning", "No file found. Nothing to delete.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not delete style: {e}")

def load_data_into_treeview():
    # Verwijder bestaande items in de Treeview
    for item in tree.get_children():
        tree.delete(item)

    # Lees stijlen uit het CSV-bestand
    try:
        styles = get_full_collection()
        for style in styles:
            tree.insert("", tk.END, iid=style['Style ID'], values=(style['Style ID'], style['Style name'], style['Product type']))
    except Exception as e:
        messagebox.showerror("Error", f"Error loading data: {e}")

def view_full_collection():
    # Creert nieuw pop-up window
    collection_window = tk.Toplevel(root)
    collection_window.title("Full Collection")
    collection_window.geometry("1800x400")

    # Voegt treeview widget om collectie te laten zien
    full_tree = ttk.Treeview(collection_window, columns=(
    "Style ID", "Style Name", "Product Type", "Textiles", "Size Range", "Sizes", "Remarks"), show="headings")
    full_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    full_tree.heading("Style ID", text="Style ID", anchor="center")
    full_tree.heading("Style Name", text="Style Name", anchor="center")
    full_tree.heading("Product Type", text="Product Type", anchor="center")
    full_tree.heading("Textiles", text="Textiles", anchor="center")
    full_tree.heading("Size Range", text="Size Range", anchor="center")
    full_tree.heading("Sizes", text="Sizes", anchor="center")
    full_tree.heading("Remarks", text="Remarks", anchor="center")

    # Load the data from the CSV file
    try:
        styles = get_full_collection()
        for style in styles:
            full_tree.insert("", tk.END, values=(
            style['Style ID'], style['Style name'], style['Product type'], style['Textiles'], style['Size range'],
            style['Sizes'], style['Remarks']))
    except Exception as e:
        messagebox.showerror("Error", f"Could not load collection: {e}", parent=collection_window)

# Save button
save_to_csv = tk.Button(frame_style_input, text="SAVE", command=save_data)
save_to_csv.grid(column=0, row=6, padx=10, pady=10, sticky=tk.W)

# Delete button
delete_record_csv = tk.Button(frame_style_input, text="DELETE", command=delete_data)
delete_record_csv.grid(column=1, row=6, padx=10, pady=10, sticky=tk.E)

# View full collection button
view_full_button = tk.Button(frame_style_input, text="VIEW", command=view_full_collection, width=8)
view_full_button.grid(column=0, row=8, columnspan=3, pady=5, padx=5, sticky=tk.W)


load_data_into_treeview()

root.mainloop()


