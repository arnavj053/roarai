import sqlite3
import pickle
import sqlite_vss

def load_query_embedding(file_path):
    """Load a query embedding from a pickle file."""
    with open(file_path, 'rb') as file:
        return pickle.load(file)

def perform_similarity_search(conn, query_vector, num_dimensions):
    """Execute a similarity search using the provided query vector."""
    query_blob = sqlite3.Binary(pickle.dumps(query_vector))
    
    # Ensure the sqlite_vss extension is loaded
    sqlite_vss.load(conn)
    
    # Create a cursor object
    cursor = conn.cursor()
    
    # Create the virtual table for vss
    cursor.execute('''
        CREATE VIRTUAL TABLE IF NOT EXISTS vss_embeddings USING vss(vector BLOB, dimensions=?);
    ''', (num_dimensions,))
    
    # Perform the vector similarity search
    cursor.execute('''
        SELECT id, distance
        FROM vss_embeddings
        WHERE vss_search(vector, ?) ORDER BY distance LIMIT 10;
    ''', (query_blob,))
    
    # Fetch and return the results
    return cursor.fetchall()

def main():
    query_embedding_path = '/Users/arnavjain/Desktop/pkl_files_embeddings/seperate_paragraph_none_voyage_embedding.pkl'
    query_embedding = load_query_embedding(query_embedding_path)
    
    # Determine the number of dimensions of your query vector
    num_dimensions = len(query_embedding)
    
    # Connect to the SQLite database
    conn = sqlite3.connect('embeddings.db')
    conn.enable_load_extension(True)
    
    try:
        results = perform_similarity_search(conn, query_embedding, num_dimensions)
        for row in results:
            print(f"ID: {row[0]}, Distance: {row[1]}")
    finally:
        conn.close()

if __name__ == '__main__':
    main()
