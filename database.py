import sqlite3

def get_connection():
    """create fashion collection database and enable foreign key enforcement"""
    con = sqlite3.connect(":memory:")
    con.execute("PRAGMA foreign_keys = ON;")
    return con


def create_tables():
    """Create fashion collection and product tables"""
    con = get_connection()
    cur = con.cursor()

    # create table for fashion collection using cur.execute() method
    cur.execute("""
    CREATE TABLE IF NOT EXISTS collections (
        collection_id INTEGER PRIMARY KEY AUTOINCREMENT,
        season_name TEXT NOT NULL,
        production_status TEXT NOT NULL
             )""")

    # create table for products
    cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        collection_id INTEGER,
        name TEXT NOT NULL,
        materials TEXT NOT NULL,
        fit TEXT NOT NULL,
        material_certifications TEXT NOT NULL,
        colors TEXT NOT NULL,
        processes TEXT,
        supplier TEXT NOT NULL,
        gender TEXT NOT NULL, 
        FOREIGN KEY (collection_id) REFERENCES clothing_collection(collection_id) ON DELETE CASCADE
                )""")





    # res = cur.execute("SELECT name FROM sqlite_master")
    # res.fetchone()

    #commit changes and close connection to database
    con.commit()
    con.close()









# #Refreshes database so that I can run and test code multiple times
# con = sqlite3.connect(':memory:')
