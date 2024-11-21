import sqlite3
con = sqlite3.connect("fashion_collection")
cur = con.cursor()


#creates the table collection
cur.execute('''
CREATE TABLE IF NOT EXISTS clothing_collection (
            collection_id INTEGER PRIMARY KEY NOT NULL, 
            season_name TEXT NOT NULL, 
            production_status TEXT NOT NULL
)
''')

cur.execute('''
    INSERT INTO clothing_collection VALUES
        (1, "fall winter 2022", "completed")      
''')

con.commit()

res = cur.execute("SELECT season_name FROM clothing_collection")
print(res.fetchall())


