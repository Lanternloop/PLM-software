"""PLM-applicatie GUI module"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from main_1 import add_style, get_full_collection, delete_style

root = tk.Tk()
root.title("PLM-application")
root.columnconfigure(0, weight=1)
root.geometry("800x600")

# TAB VIEW NUMMER 1.
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0, sticky="nsew")

functions_tab = ttk.Frame(notebook)
notebook.add(functions_tab, text="Manage styles")

# TAB VIEW NUMMER 2.
treeview_tab = ttk.Frame(notebook)
treeview_tab.columnconfigure(0, weight=1)
notebook.add(treeview_tab, text="View collection")

tree = ttk.Treeview(treeview_tab, columns=("Style ID", "Style Name", "Product Type"), show="headings")
tree.grid(column=0, row=1, sticky=(tk.E + tk.W), padx=10, pady=10)

# Treeview columns headings.
tree.heading("Style ID", text="Style ID", anchor="center")
tree.heading("Style Name", text="Style Name", anchor="center")
tree.heading("Product Type", text="Product Type", anchor="center")

# Text variabel aan label en label frame dynamisch tekst verandering van titel voor style inputs
text_frame_1 = tk.StringVar(value="Custom settings")
text_var = ttk.Label(functions_tab, textvariable=text_frame_1, font=("arial", 11, "bold"))
frame_style_input = tk.LabelFrame(functions_tab, labelwidget=text_var)
frame_style_input.grid(padx=10, sticky=(tk.E + tk.W))
frame_style_input.columnconfigure(0, weight=1)
text_frame_1.set("Add new style")

#Text variabel aan label en label frame dynamisch tekst verandering van titel van delete style
text_frame_2 = tk.StringVar(value="Custom settings")
text_var = ttk.Label(functions_tab, textvariable=text_frame_2, font=("arial", 11, "bold"))
delete_choice= tk.LabelFrame(functions_tab, labelwidget=text_var)
delete_choice.grid(padx=10, sticky=(tk.E + tk.W))
delete_choice.columnconfigure(1, weight=1)
text_frame_2.set("Delete style")

#Label en Entries
label_style_id = tk.Label(frame_style_input, text="Style ID")
label_style_id.grid(column=1, row=2, padx=10, pady=10)
button_style_id = tk.Entry(frame_style_input)
button_style_id.grid(column=2, row=2, padx=10, pady=10)

label_style_name = tk.Label(frame_style_input, text="Style name")
label_style_name.grid(column=1, row=2, padx=10, pady=10)
entry_style_name = tk.Entry(frame_style_input)
entry_style_name.grid(column=2, row=2, padx=10, pady=10)

choice_product_type = ("Jackets", "Shirts", "Pants", "Shorts", "Sweaters", "Vests")
label_product_type = tk.Label(frame_style_input, text="Product type")
label_product_type.grid(column=1, row=4, padx=10, pady=10)
button_product_type = ttk.Combobox(frame_style_input, values=choice_product_type)
button_product_type.grid(column=2, row=4, padx=10, pady=10)

choice_textile = (
    "Organic Cotton", "Recycled Polyester (rPET)", "Hemp",
    "Tencel (Lyocell)", "Recycled Nylon", "Merino Wool"
    "Alpaca Wool", "Corozo", "Piñatex", "Econyl"
    "Polartec Power Air" "Yulex Natural Rubber", "Recycled Wool"
    "SeaCell", "Kapok", "Bamboo Lyocell", "Cork", "Upcycled Denim"
    "WOOL+PLA", "Soy Silk Fiber)"
    )
label_textiles = tk.Label(frame_style_input, text="Textile(s)")
label_textiles.grid(column=1, row=5, padx=10, pady=10)
button_textiles = ttk.Combobox(frame_style_input, values=choice_textile)
button_textiles.grid(column=2, row=5,  padx=10, pady=10)

choice_size_range = ("Mens", "Womens")
label_size_range = tk.Label(frame_style_input, text="Size range")
label_size_range.grid(column=1, row=6,  padx=10, pady=10)
button_size_range = ttk.Combobox(frame_style_input, values=choice_size_range)
button_size_range.grid(column=2, row=6,  padx=10, pady=10)

choice_size = ("XXS, XS, S, M, L, XL, XXL",
               "XS, S, M, L, XL, XXL",
               "28, 30, 32, 34, 36, 38",
               "26, 28, 30, 32, 34, 36, 38"
               )
label_sizes = tk.Label(frame_style_input, text="Sizes")
label_sizes.grid(column=1, row=7, padx=10, pady=10)
button_sizes = ttk.Combobox(frame_style_input, values=choice_size)
button_sizes.grid(column=2, row=7, padx=10, pady=10)

label_remarks = tk.Label(frame_style_input, text="Remarks")
label_remarks.grid(column=1, row=8, padx=10, pady=10)
button_remarks = tk.Text(frame_style_input, width=30, height=5)
button_remarks.grid(column=2, row=8, padx=10, pady=10)

def clear_fields():
    entry_style_name.delete(0, tk.END)
    button_product_type.set('')
    button_textiles.set('')
    button_size_range.set('')
    button_sizes.set('')
    button_remarks.delete("1.0", tk.END)

def save_data():
    # Verzamelt data van input velden in tkinter
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
    new_iid = str(len(tree.get_children()) + 1)
    tree.insert("", tk.END, iid=new_iid, values=(new_iid, style_name, product_type))

    # Voeg de nieuwe stijl toe aan het CSV-bestand
    try:
        add_style(new_iid, style_name, product_type, textiles, size_range, sizes, remarks)
        messagebox.showinfo("Success", f"Style with ID {new_iid} added!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save style: {e}")

    # Clear the input fields
    clear_fields()

def delete_data():
    selected_item = tree.selection()

    # Controleer of een stijl is geselecteerd
    if not selected_item:
        messagebox.showerror("Error", "Please select a style to delete.")
        return

    # Haal het unieke ID van de geselecteerde stijl op
    style_id = tree.item(selected_item[0], "values")[0]

    # Verwijder de stijl uit het CSV-bestand en de Treeview
    try:
        deleted = delete_style(style_id)
        if deleted:
            tree.delete(selected_item[0])
            messagebox.showinfo("Success", f"Style with ID {style_id} deleted!")
        else:
            messagebox.showerror("Error", f"Could not delete style with ID {style_id}.")
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
    # Maak een nieuw venster aan voor het tonen van de volledige collectie
    collection_window = tk.Toplevel(root)
    collection_window.title("Full Collection")
    collection_window.geometry("1600x400")

    # Voeg een Treeview-widget toe om de gegevens weer te geven
    full_tree = ttk.Treeview(collection_window, columns=(
    "Style ID", "Style Name", "Product Type", "Textiles", "Size Range", "Sizes", "Remarks"), show="headings")
    full_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Definieer de koppen van de Treeview
    full_tree.heading("Style ID", text="Style ID", anchor="center")
    full_tree.heading("Style Name", text="Style Name", anchor="center")
    full_tree.heading("Product Type", text="Product Type", anchor="center")
    full_tree.heading("Textiles", text="Textiles", anchor="center")
    full_tree.heading("Size Range", text="Size Range", anchor="center")
    full_tree.heading("Sizes", text="Sizes", anchor="center")
    full_tree.heading("Remarks", text="Remarks", anchor="center")

    # Laad de gegevens uit het CSV-bestand
    try:
        styles = get_full_collection()  # Gebruik de functie uit main_1.py
        for style in styles:
            full_tree.insert("", tk.END, values=(
            style['Style ID'], style['Style name'], style['Product type'], style['Textiles'], style['Size range'],
            style['Sizes'], style['Remarks']))
    except Exception as e:
        messagebox.showerror("Error", f"Could not load collection: {e}", parent=collection_window)

    # Voeg een verticale scrollbar toe aan de Treeview
    scrollbar = ttk.Scrollbar(collection_window, orient=tk.VERTICAL, command=full_tree.yview)
    full_tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#Save button
save_to_csv = tk.Button(frame_style_input, text="SAVE", command=save_data)
save_to_csv.grid(column=2, row=10, padx=10, pady=10)

#Delete button
delete_record_csv = tk.Button(treeview_tab, text="DELETE", command=delete_data)
delete_record_csv.grid(column=0, row=2, columnspan=3, pady=10, sticky=tk.N)

# View full collection knop
view_full_button = tk.Button(treeview_tab, text="VIEW FULL COLLECTION", command=view_full_collection)
view_full_button.grid(column=0, row=3, columnspan=3, pady=10, sticky=tk.N)


load_data_into_treeview()

root.mainloop()


