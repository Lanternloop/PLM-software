"""Main code voor crud functionaliteiten functies."""
from pathlib import Path
import os
import csv
import pandas


#Nieuwe file naam dat gebruikt wordt als file niet bestaat.
file_path = "data_base_fashion_collection.csv"

#data frame view with pandas using the fashion collections column csv file.
def dataframe_fashion_collection():
    df = pandas.read_csv(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv", sep=',', quotechar='"', encoding='utf-8')
    print(df.to_string())

#Check als file bestaat en voegt nieuwe style toe aan csv file.
#Anders maakt het een nieuwe csv file en schrijft deze style erin.
def add_style(style_id, style_name, product_type, textiles, size_range, sizes, remarks):
    try:
        with open(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv", mode='a', newline='') as dict_file:
            fieldnames = ['Style ID', 'Style name', 'Product type', 'Textiles', 'Size range', 'Sizes', 'Remarks']
            writer = csv.DictWriter(dict_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, fieldnames=fieldnames)

            #Schrijft row in csv file
            writer.writerow(
                {'Style ID': style_id,
                 'Style name': style_name,
                 'Product type': product_type,
                 'Textiles': textiles,
                 'Size range': size_range,
                 'Sizes': sizes,
                 'Remarks': remarks}
            )

    except FileNotFoundError:
        with open(file_path, mode='a', newline='') as new_file:
            fieldnames = ['Style ID', 'Style name', 'Product type', 'Textiles', 'Size range', 'Sizes', 'Remarks']
            writer = csv.DictWriter(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow(
                {'Style ID': style_id,
                 'Style name': style_name,
                 'Product type': product_type,
                 'Textiles': textiles,
                 'Size range': size_range,
                 'Sizes': sizes,
                 'Remarks': remarks}
            )

#Verwijdert style van csv file.
def remove_style():
        with open(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv", mode='r',newline='') as dict_file:
            fieldnames = ['Style ID', 'Style name', 'Product type', 'Textiles', 'Size range', 'Sizes', 'Remarks']
            contents_file = csv.DictReader(dict_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, fieldnames=fieldnames)

            next(contents_file)
            copy_contents_file = contents_file

def get_style_ids():
    style_ids = []
    try:
        with open(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv", mode='r', newline='') as dict_file:
            reader = csv.DictReader(dict_file, delimiter=',', quotechar='"')
            for row in reader:
                if row['Style ID']:
                    style_ids.append(row['Style ID'])
    except FileNotFoundError:
        pass
    return style_ids

def delete_style(style_id_to_delete):
    rows = []
    deleted = False
    with open(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv", mode='r', newline='', encoding='utf-8') as dict_file:
        reader = csv.DictReader(dict_file)
        fieldnames = reader.fieldnames
        for row in reader:
            if row['Style ID'] != style_id_to_delete:
                rows.append(row)
            else:
                deleted = True

    with open(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv", mode='w', newline='', encoding='utf-8') as dict_file:
        writer = csv.DictWriter(dict_file, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    return deleted

def get_collection():
    with open(r"C:\Users\Zeph\Desktop\Programming basics\Fashion_Collection_Proper_Columns.csv", mode='r', encoding='utf-8-sig') as dict_file:
        csv_reader = csv.DictReader(dict_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for row in csv_reader:
            print(row)



