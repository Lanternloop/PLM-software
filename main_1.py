"""Main code voor crud functionaliteiten functies."""
import os
import csv


class ManageStyle:
    """Class voor crud functionaliteiten voor stylen in collectie."""

    def __init__(self, style_id, style_name, product_type, textiles, size_range, sizes, remarks):
        """Creert attributen die gebruikt zal worden voor het toevoegen van een style in het CSV bestand."""
        self.style_id = style_id
        self.style_name = style_name
        self.product_type = product_type
        self.textiles = textiles
        self.size_range = size_range
        self.sizes = sizes
        self.remarks = remarks


    def add_style(self):
        """Voegt een nieuwe stijl toe aan het CSV bestand."""
        file_exists = os.path.exists(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv")  # Controleert of het bestand bestaat

        with open(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv", mode='a', newline='',
                    encoding='utf-8') as dict_file:
            fieldnames = ['Style ID', 'Style name', 'Product type', 'Textiles', 'Size range', 'Sizes', 'Remarks']
            writer = csv.DictWriter(dict_file, fieldnames=fieldnames)

            # Schrijft een kopregel als het bestand nieuw is
            if not file_exists:
                writer.writeheader()

            # Schrijft de nieuwe stijl naar het bestand
            writer.writerow({
                'Style ID': self.style_id,
                'Style name': self.style_name,
                'Product type': self.product_type,
                'Textiles': self.textiles,
                'Size range': self.size_range,
                'Sizes': self.sizes,
                'Remarks': self.remarks
            })


    @staticmethod
    def delete_style(style_id_to_delete):
        """Verwijdert een stijl uit het CSV bestand op basis van het ID."""
        with open(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv", mode='r', newline='',
                    encoding='utf-8') as dict_file:
            rows = list(csv.DictReader(dict_file))

        # Schrijf alle rijen behalve degene die verwijderd moet worden
        with open(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv", mode='w', newline='',
                    encoding='utf-8') as dict_file:
            fieldnames = ['Style ID', 'Style name', 'Product type', 'Textiles', 'Size range', 'Sizes', 'Remarks']
            writer = csv.DictWriter(dict_file, fieldnames=fieldnames)
            writer.writeheader()

            for row in rows:
                if row['Style ID'] != style_id_to_delete:
                    writer.writerow(row)

        return True

def get_full_collection():
    """Leest de volledige collectie van het CSV bestand."""
    if not os.path.exists(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv"):
        return []

    with open(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv", mode='r', newline='',
              encoding='utf-8') as dict_file:
        reader = csv.DictReader(dict_file)
        return list(reader)












###ORIGINEEL CODE ZONDER CLASS!!!!
# # Voegt een nieuwe stijl toe aan de CSV-bestand
# def add_style(style_id, style_name, product_type, textiles, size_range, sizes, remarks):
#     """Voegt een nieuwe stijl toe aan de CSV-bestand."""
#     file_exists = os.path.exists(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv")  # Controleert of het bestand bestaat
#
#     with open(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv", mode='a', newline='',
#               encoding='utf-8') as dict_file:
#         fieldnames = ['Style ID', 'Style name', 'Product type', 'Textiles', 'Size range', 'Sizes', 'Remarks']
#         writer = csv.DictWriter(dict_file, fieldnames=fieldnames)
#
#         # Schrijft een kopregel als het bestand nieuw is
#         if not file_exists:
#             writer.writeheader()
#
#         # Schrijft de nieuwe stijl naar het bestand
#         writer.writerow({
#             'Style ID': style_id,
#             'Style name': style_name,
#             'Product type': product_type,
#             'Textiles': textiles,
#             'Size range': size_range,
#             'Sizes': sizes,
#             'Remarks': remarks
#         })
#
# # Verwijdert een stijl uit de CSV-bestand
# def delete_style(style_id_to_delete):
#     """Verwijdert een stijl uit de CSV-bestand op basis van het ID."""
#     with open(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv", mode='r', newline='',
#               encoding='utf-8') as dict_file:
#         rows = list(csv.DictReader(dict_file))
#
#     # Schrijf alle rijen behalve degene die verwijderd moet worden
#     with open(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv", mode='w', newline='',
#               encoding='utf-8') as dict_file:
#         fieldnames = ['Style ID', 'Style name', 'Product type', 'Textiles', 'Size range', 'Sizes', 'Remarks']
#         writer = csv.DictWriter(dict_file, fieldnames=fieldnames)
#         writer.writeheader()
#
#         for row in rows:
#             if row['Style ID'] != style_id_to_delete:
#                 writer.writerow(row)
#
#     return True
#
# def update_style(style_to_update):
#     with open(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv", mode='r', newline='',
#               encoding='utf-8') as dict_file:
#         rows = list(csv.DictReader(dict_file))
#
#     with open(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv", mode='w', newline='',
#               encoding='utf-8') as dict_file:
#         fieldnames = ['Style ID', 'Style name', 'Product type', 'Textiles', 'Size range', 'Sizes', 'Remarks']
#         writer = csv.DictWriter(dict_file, fieldnames=fieldnames)
#         writer.writeheader()
#
#         for row in rows:
#             if row['Style ID'] != style_to_update:
#                 writer.writerow(style_to_update)
#
# # Leest de volledige collectie van de CSV-bestand
# def get_full_collection():
#     """Leest de volledige collectie van het CSV-bestand."""
#     if not os.path.exists(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv"):
#         return []
#
#     with open(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv", mode='r', newline='',
#               encoding='utf-8') as dict_file:
#         reader = csv.DictReader(dict_file)
#         return list(reader)
