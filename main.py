from pathlib import Path
import json

#Maakt connectie met de json file.
path = Path("database.json")

def create_file():
    """Kijkt of json file bestaat, anders maakt nieuwe file en importeer lege list."""
    if path.exists():
        empty_list = []
        data = json.dumps(empty_list, indent=4)
        path.write_text(data)


def get_collections():
    """Toont alle mode collecties met kledingstukken die in de json file zitten."""
    try:
        if path.exists():
            database_json = path.read_text()
            collections_list = json.loads(database_json)
            return json.dumps(collections_list, indent=4)
    except FileNotFoundError:
        create_file()


print(get_collections())
def add_collection(collection_id, collection_name):
    """Voegt nieuwe mode collectie aan lijst in json file."""
    fashion_collections_json = get_collections()
    fashion_collections_python = json.loads(fashion_collections_json)

    new_collection = {"collections_id": collection_id, #dictionary van nieuwe collectie die wordt toegevoegd.
                      "collection_name": collection_name,
                      "styles": []
    }

    # voegt nieuw collectie aan json file list en schrijft het erin.
    fashion_collections_python.append(new_collection)
    path.write_text(json.dumps(fashion_collections_python, indent=4))

    # print bericht dat nieuwe collectie is toegevoegd.
    print(f"Collection with {collection_id} has been added!")
    return get_collections()

print(add_collection(2, "Summer 2025"))
print(add_collection(3, "Summer 2026"))





































# class Collection:
#     """Beschrijft een collection"""
#
#     def __init__(self, season_id, season_name, styles):
#         self.season = season_id
#         self.season_name = season_name
#         self.styles = styles
#
#
#
#
#
#
#
#
# class Style:
#     """Een class om een kledingstuk te beschrijven"""
#
#     def __init__(self, style_id, style_name, product_type, textile, textile_certifications, size_range, sizes):
#         self.style_id = style_id
#         self.style_name = style_name
#         self.product_type = product_type
#         self.textile = textile
#         self.textile_certifications = textile_certifications
#         self.size_range = size_range
#         self.sizes = sizes
#         self.remarks = ""
#
#     def get_description_style(self):
#         """Toont een volledig beschrijf van kledingstuk"""
#         print(f"Style ID: style: {self.style_id}")
#         print(f"Style name: {self.style_name}")
#         print(f"Product type: {self.product_type}")
#         print(f"Textile: {self.textile}")
#         print(f"Textile certifications: {self.textile_certifications}")
#         print(f"Size range: {self.size_range}")
#         print(f"sizes: {self.sizes}")
#         print(f"Remarks: {self.remarks}")
#
#


