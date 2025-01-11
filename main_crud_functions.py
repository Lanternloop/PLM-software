"""Main code voor crud functionaliteiten logica."""
import os
import csv

file_path = os.path.abspath("Season_1.csv")
file_path_deleted_ids = os.path.abspath("deleted_ids.txt")

class ManageStyle:
    """Class voor crud functionaliteiten voor stylen in collectie."""
    # Houdt de verwijderde id's vast
    deleted_ids = []
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
    def load_deleted_ids():
        """Laad verwijderde style ids van de file, file_path_deleted_ids"""
        if os.path.exists(file_path_deleted_ids):
            with open(file_path_deleted_ids, mode="r", newline='', encoding='utf-8') as delete_id:
                for ids in delete_id:
                    ManageStyle.deleted_ids.append(int(ids.strip()))

    @staticmethod
    def get_next_id():
        """Bepaalt de volgende beschikbare style ID"""
        styles = get_full_collection()

        active_ids = set()
        if styles:
            for style in styles:
                active_ids.add(int(style['Style ID']))

        all_ids = set(active_ids).union(set(ManageStyle.deleted_ids))

        highest_id = 0
        for ids in all_ids:
            if ids > highest_id:
                highest_id = ids

        return str(highest_id + 1)

    def add_style(self):
        """Voegt een nieuwe stijl toe aan het CSV bestand."""
        file_exists = os.path.exists(file_path)  # Controleert of het bestand bestaat

        with open(file_path, mode='a', newline='', encoding='utf-8') as dict_file:
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
        with open(file_path, mode='r', newline='', encoding='utf-8') as dict_file:
            rows = list(csv.DictReader(dict_file))

        # Schrijf alle rijen behalve degene die verwijderd moet worden
        with open(file_path, mode='w', newline='', encoding='utf-8') as dict_file:
            fieldnames = ['Style ID', 'Style name', 'Product type', 'Textiles', 'Size range', 'Sizes', 'Remarks']
            writer = csv.DictWriter(dict_file, fieldnames=fieldnames)
            writer.writeheader()

            deleted = False
            for row in rows:
                if row['Style ID'] == str(style_id_to_delete):
                    deleted = True
                    ManageStyle.deleted_ids.append(int(row['Style ID']))

                    with open("deleted_ids.txt")
                else:
                    writer.writerow(row)

        return deleted


def get_full_collection():
    """Leest de volledige collectie van het CSV bestand en return een list."""
    if not os.path.exists(file_path):
        return []

    with open(file_path, mode='r', newline='', encoding='utf-8') as dict_file:
        reader = csv.DictReader(dict_file)
        return list(reader)









