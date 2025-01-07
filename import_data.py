import pandas as pd
import sqlite3
from pathlib import Path

data_dir = Path('/app/data')
db_dir = Path('/app/db')

def import_excel():
    excel_files = list(data_dir.glob('*.xlsx'))
    
    if not excel_files:
        print("No Excel files found")
        return False
        
    try:
        print(f"Processing file: {excel_files[0]}")
        df = pd.read_excel(excel_files[0], engine='openpyxl')
        db_path = db_dir / 'registros.db'
        
        with sqlite3.connect(db_path) as conn:
            df.to_sql('registros', conn, if_exists='replace', index=False)
        print("Data imported successfully")
        return True
    except Exception as e:
        print(f"Error processing file: {e}")
        return False
        
if __name__ == '__main__':
    success = import_excel()
    if not success:
        print("Failed to import data")

