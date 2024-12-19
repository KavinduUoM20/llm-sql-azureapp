import os
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase

# Load environment variables
load_dotenv()

def test_azure_sql_connection():
    # Fetch the connection string from .env
    db_uri = os.getenv("AZURE_SQL_URI")
    
    if not db_uri:
        raise ValueError("AZURE_SQL_URI is not defined in the environment variables.")
    
    try:
        # Initialize the connection using SQLDatabase
        db = SQLDatabase.from_uri(db_uri)
        
        # Execute a test query
        test_query = "SELECT TOP 5 * FROM Album;"
        print("Executing test query...")
        result = db.run(test_query)
        
        # Print the results
        print("Connection successful! Test query result:")
        print(result)
    except Exception as e:
        print("Connection failed. Error:")
        print(e)

if __name__ == "__main__":
    test_azure_sql_connection()
