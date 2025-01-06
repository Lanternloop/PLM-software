"""PLM-applicatie GUI module"""
#Importeerd tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Importeer functies en class van main_1 module
from main_crud_functions import get_full_collection
from main_crud_functions import ManageStyle

root = tk.Tk()
root.title("PLM-application")
root.columnconfigure(0, weight=1)
root.geometry("700x800")


def clear_fields():
    """Verwijdert alle data in de input velden."""
    button_style_name.delete(0, tk.END)
    button_product_type.set('')
    button_textiles.selection_clear(0, tk.END)
    button_size_range.set('')
    button_sizes.set('')
    button_remarks.delete("1.0", tk.END)

def save_data():
    """Opslaan van style in CSV bestand en treeview met uniek ID."""
    style_name = button_style_name.get().strip()
    product_type = button_product_type.get().strip()
    textiles = get_selected_textiles()
    size_range = button_size_range.get().strip()
    sizes = button_sizes.get().strip()
    remarks = button_remarks.get("1.0", "end-1c").strip()

    # Valideer user input
    if not style_name or not product_type or not textiles or not size_range or not sizes:
        messagebox.showinfo("Error","Please fill in all the input fields!")
        return

    # Genereer uniek id en voegt het toe in de treeview
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
    """Verwijdert gekozen style van CSV bestand en treeview."""
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

def view_full_collection():
    """Maakt een pop-up window met de volledige collectie en al zijn fieldnames met bijhorende data."""
    collection_window = tk.Toplevel(root)
    collection_window.title("Full Collection")
    collection_window.geometry("1800x400")

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

    try:
        styles = get_full_collection()
        for style in styles:
            full_tree.insert("", tk.END, values=(
            style['Style ID'], style['Style name'], style['Product type'], style['Textiles'], style['Size range'],
            style['Sizes'], style['Remarks']))
    except Exception as e:
        messagebox.showerror("Error", f"Could not load collection: {e}", parent=collection_window)

def load_data_into_treeview():
    """Laad data dynamisch in treeview tijdens de run van de applicatie."""
    # Verwijder oude of dubbele info uit de treeview
    for item in tree.get_children():
        tree.delete(item)

    # Lees stijlen uit het CSV-bestand
    try:
        styles = get_full_collection()
        for style in styles:
            tree.insert("", tk.END, iid=style['Style ID'], values=(style['Style ID'], style['Style name'], style['Product type']))
    except Exception as e:
        messagebox.showerror("Error", f"Error loading data: {e}")

def get_selected_textiles():
    selected_indices = button_textiles.curselection()
    selected_textiles = []

    for i in selected_indices:
        selected_textiles.append(button_textiles.get(i))

    return ", ".join(selected_textiles)

# Input velden frame voor stijl
input_frame = ttk.Frame(root, padding=10)
input_frame.grid(column=0, row=1, columnspan=2, sticky="ew", padx=10, pady=10)

# Treeview widget voor het laten zien van toegevoegde styles
tree_frame = ttk.Frame(root)
tree_frame.grid(column=0, row=0, columnspan=2, sticky="nsew", padx=10, pady=10)
root.rowconfigure(0, weight=3)
root.columnconfigure(0, weight=1)

tree = ttk.Treeview(tree_frame, columns=("Style ID", "Style Name", "Product Type"), show="headings")
tree.grid(column=0, row=0, columnspan=3, sticky=(tk.E + tk.W), padx=10, pady=10)

# Treeview columns headings.
tree.heading("Style ID", text="Style ID", anchor="center")
tree.heading("Style Name", text="Style Name", anchor="center")
tree.heading("Product Type", text="Product Type", anchor="center")

# Text variabel, stringvar voor text frame tekst
text_frame_1 = tk.StringVar(value="Custom settings")
text_var = ttk.Label(input_frame, textvariable=text_frame_1, font=("arial", 11, "bold"))
frame_style_input = tk.LabelFrame(input_frame, labelwidget=text_var)
frame_style_input.grid(column=0, row=1, columnspan=3, sticky=(tk.E + tk.W), padx=10, pady=10)
frame_style_input.columnconfigure(1, weight=1)
text_frame_1.set("Add new style")

# Style name button, Entry widget
label_style_name = tk.Label(frame_style_input, text="Style name")
label_style_name.grid(column=0, row=0, padx=10, pady=5, sticky=tk.W)
button_style_name = tk.Entry(frame_style_input)
button_style_name.grid(column=1, row=0, padx=10, pady=5, sticky="ew")

# Product type button, Combobox widget met list van verschillende soorten kleding categorieën
choice_product_type = ("Jackets", "Shirts", "Pants", "Shorts", "Sweaters", "Vests")
label_product_type = tk.Label(frame_style_input, text="Product type")
label_product_type.grid(column=0, row=1, padx=10, pady=5, sticky=tk.W)
button_product_type = ttk.Combobox(frame_style_input, values=choice_product_type)
button_product_type.grid(column=1, row=1, padx=10, pady=5, sticky="ew")

# Textiles button, Listbox widget met list van verschillende soorten kleding textielen
choice_textiles = (
    "Organic Cotton", "Recycled Polyester (rPET)", "Hemp",
    "Tencel (Lyocell)", "Recycled Nylon", "Merino Wool"
    "Alpaca Wool", "Corozo", "Piñatex", "Econyl"
    "Polartec Power Air" "Yulex Natural Rubber", "Recycled Wool"
    "SeaCell", "Kapok", "Bamboo Lyocell", "Cork", "Upcycled Denim"
    "WOOL+PLA", "Soy Silk Fiber)"
    )
label_textiles = tk.Label(frame_style_input, text="Textile(s)")
label_textiles.grid(column=0, row=4, padx=10, pady=5, sticky=tk.W)
button_textiles = tk.Listbox(frame_style_input, selectmode=tk.MULTIPLE, height=8)
button_textiles.grid(column=1, row=4, padx=10, pady=5, sticky="ew")
for textile in choice_textiles:
    button_textiles.insert(tk.END, textile)

# Size range button, Combobox widget met list opties "Mens", "Womens"
choice_size_range = ("Mens", "Womens")
label_size_range = tk.Label(frame_style_input, text="Size range")
label_size_range.grid(column=0, row=3, padx=10, pady=5, sticky=tk.W)
button_size_range = ttk.Combobox(frame_style_input, values=choice_size_range)
button_size_range.grid(column=1, row=3, padx=10, pady=5, sticky="ew")

# Sizes button, Combobox widget met list maten
choice_size = ("XXS, XS, S, M, L, XL, XXL",
               "XS, S, M, L, XL, XXL",
               "28, 30, 32, 34, 36, 38",
               "26, 28, 30, 32, 34, 36, 38"
               )
label_sizes = tk.Label(frame_style_input, text="Sizes")
label_sizes.grid(column=0, row=2, padx=10, pady=5, sticky=tk.W)
button_sizes = ttk.Combobox(frame_style_input, values=choice_size)
button_sizes.grid(column=1, row=2, padx=10, pady=5, sticky="ew")

# Remarks button, text widget
label_remarks = tk.Label(frame_style_input, text="Remarks")
label_remarks.grid(column=0, row=5, padx=10, pady=5, sticky=tk.W)
button_remarks = tk.Text(frame_style_input, width=30, height=5)
button_remarks.grid(column=1, row=5, padx=10, pady=5, sticky="ew")

# Save button in frame_style_input
save_to_csv = tk.Button(frame_style_input, text="SAVE", command=save_data)
save_to_csv.grid(column=1, row=6, padx=10, pady=10, sticky=tk.W)

# Delete button in tree_frame
delete_record_csv = tk.Button(tree_frame, text="DELETE", command=delete_data)
delete_record_csv.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)

# View full collection button in tree_frame
view_full_button = tk.Button(tree_frame, text="VIEW", command=view_full_collection, width=8)
view_full_button.grid(column=1, row=1, columnspan=3, pady=5, padx=5, sticky=tk.W)


load_data_into_treeview()
root.mainloop()


