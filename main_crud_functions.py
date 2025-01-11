"""Main code voor crud functionaliteiten logica."""
import os
import csv

file_path = os.path.abspath("Season_1.csv")

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

    @staticmethod
    def get_next_id():
        """Bepaalt de volgende beschikbare style ID"""
        styles = get_full_collection()
        last_id = 0

        if styles:
            # Kijkt wat de volgende beschikbare Style ID is
            for style in styles:
                style_id = int(style['Style ID'])
                if style_id > last_id:
                    last_id = style_id

        return str(last_id + 1)

    def add_style(self):
        """Voegt een nieuwe stijl toe aan het CSV bestand."""
        file_exists = os.path.exists(file_path)  # Controleert of het bestand bestaat

        with open(file_path, mode='a', newline='',
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
        with open(file_path, mode='r', newline='',
                    encoding='utf-8') as dict_file:
            rows = list(csv.DictReader(dict_file))

        # Schrijf alle rijen behalve degene die verwijderd moet worden
        with open(file_path, mode='w', newline='',
                    encoding='utf-8') as dict_file:
            fieldnames = ['Style ID', 'Style name', 'Product type', 'Textiles', 'Size range', 'Sizes', 'Remarks']
            writer = csv.DictWriter(dict_file, fieldnames=fieldnames)
            writer.writeheader()

            for row in rows:
                if row['Style ID'] != style_id_to_delete:
                    writer.writerow(row)

        return True


def get_full_collection():
    """Leest de volledige collectie van het CSV bestand en return een list."""
    if not os.path.exists(file_path):
        return []

    with open(file_path, mode='r', newline='',
              encoding='utf-8') as dict_file:
        reader = csv.DictReader(dict_file)
        return list(reader)









