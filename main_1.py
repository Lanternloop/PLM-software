"""Main code voor crud functionaliteiten functies."""
import os
import csv


# Leest de volledige collectie van de CSV-bestand
def get_full_collection():
    """Leest de volledige collectie van het CSV-bestand."""
    if not os.path.exists(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv"):
        return []

    with open(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv", mode='r', newline='', encoding='utf-8') as dict_file:
        reader = csv.DictReader(dict_file)
        return list(reader)

# Voegt een nieuwe stijl toe aan de CSV-bestand
def add_style(style_id, style_name, product_type, textiles, size_range, sizes, remarks):
    """Voegt een nieuwe stijl toe aan de CSV-bestand."""
    file_exists = os.path.exists(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv")  # Controleert of het bestand bestaat

    with open(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv", mode='a', newline='', encoding='utf-8') as dict_file:
        fieldnames = ['Style ID', 'Style name', 'Product type', 'Textiles', 'Size range', 'Sizes', 'Remarks']
        writer = csv.DictWriter(dict_file, fieldnames=fieldnames)

        # Schrijft een kopregel als het bestand nieuw is
        if not file_exists:
            writer.writeheader()

        # Schrijft de nieuwe stijl naar het bestand
        writer.writerow({
            'Style ID': style_id,
            'Style name': style_name,
            'Product type': product_type,
            'Textiles': textiles,
            'Size range': size_range,
            'Sizes': sizes,
            'Remarks': remarks
        })

# Verwijdert een stijl uit de CSV-bestand
def delete_style(style_id_to_delete):
    """Verwijdert een stijl uit de CSV-bestand op basis van het ID."""
    if not os.path.exists(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv"):
        return False

    # Lees alle rijen uit het bestand
    with open(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv", mode='r', newline='', encoding='utf-8') as dict_file:
        rows = list(csv.DictReader(dict_file))

    # Schrijf alle rijen behalve degene die verwijderd moet worden
    with open(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv", mode='w', newline='', encoding='utf-8') as dict_file:
        fieldnames = ['Style ID', 'Style name', 'Product type', 'Textiles', 'Size range', 'Sizes', 'Remarks']
        writer = csv.DictWriter(dict_file, fieldnames=fieldnames)
        writer.writeheader()

        for row in rows:
            if row['Style ID'] != style_id_to_delete:
                writer.writerow(row)

    return True





