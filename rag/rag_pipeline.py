import sqlite3
import os
import pickle
import sqlite_vss

# Function to load embeddings from a .pkl file
def load_embeddings(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)

# The directory where your .pkl files are located
embeddings_folder_path = '/Users/arnavjain/Desktop/pkl_files_embeddings'


# Establish a connection to an SQLite database file. This will create the file if it doesn't exist.
conn = sqlite3.connect('embeddings.db')

# Enable loading the sqlite-vss extension
conn.enable_load_extension(True)
# Load the sqlite-vss extension
sqlite_vss.load(conn)

# Create a table to store embeddings. If you have additional fields, you can add them to the table schema.
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS embeddings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vector BLOB NOT NULL
    )
''')
conn.commit()

# Insert embeddings into the SQLite database
for file_name in os.listdir(embeddings_folder_path):
    full_path = os.path.join(embeddings_folder_path, file_name)
    if os.path.isfile(full_path) and file_name.endswith('.pkl'):
        # Load the embeddings from the .pkl file
        vector = load_embeddings(full_path)
        # Inserting the vector into the database. The vector is converted to a binary blob.
        cursor.execute('INSERT INTO embeddings (vector) VALUES (?)', (sqlite3.Binary(pickle.dumps(vector)),))

conn.commit()

# Disable the sqlite-vss extension loading
conn.enable_load_extension(False)
conn.close()

