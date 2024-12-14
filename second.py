from pathlib import Path
import csv
import os



#Leest en print alle rows van de csv file, maar slaat de header over met NEXT.
def read_collection():
    with open(r"C:\Users\Zeph\Desktop\Programming basics\csv files\patagonia_collection.csv", mode='r') as fashion_collection:
        fashion_collection_reader = csv.reader(fashion_collection, delimiter=',')
        header_row_collection = next(fashion_collection_reader)
        for row in header_row_collection:
            print(row)

def get_collection():
    with open(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Winter_2025.csv", mode='r') as fashion_collection:
        fashion_collection_reader = csv.reader(fashion_collection, delimiter=',')
        header_row_collection = next(fashion_collection_reader)
        return header_row_collection


#Schrijft en voegt nieuwe style toe aan csv file.
def write_style(style_id, product_type, textiles, size_range, sizes):
    with open(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Winter_2025.csv", 'a', newline='') as fashion_collection:
        new_style = csv.writer(fashion_collection, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        new_style.writerow([style_id, product_type, textiles, size_range, sizes])


def rewrite_file(style_id, product_type, textiles, size_range, sizes):
    with open(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Winter_2025.csv", mode='w', newline='') as fashion_collection:
        style = csv.writer(fashion_collection, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        style.writerow([style_id, product_type, textiles, size_range, sizes])


# def delete_style(index):
#     with open("Fashion_Collection_Winter_2025.csv", mode="w")as fashion_collection:
#         removed_style = csv.writer(fashion_collection, delimiter=';', quoting=csv.QUOTE_MINIMAL

read_collection()


