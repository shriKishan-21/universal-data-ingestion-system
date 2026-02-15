from src.loader import load_data , load_files_from_folder
from src.cleaner import clean_data
from src.db_handler import store_to_database, read_from_database
from src.logger import log_info, log_error
import os

def main():
    file_path = input("Enter the file path: ")
    table_name = input("Enter the table name to store data: ")
    
    log_info("Pipeline Started")
    
    try:
        if os.path.isdir(file_path):
            log_info(f"Folder detected:{file_path}")
            
            data_list = load_files_from_folder(file_path)

            for file_name, df in data_list:
                log_info(f"Processing file: {file_name}")

                df = clean_data(df)
                table = f"{table_name}_{file_name.split('.')[0]}"

                store_to_database(df, table)

                log_info(f"Stored data in table: {table}")

        else:
            log_info(f"Single file detected: {file_path}")
            df = load_data(file_path)
            df = clean_data(df)
            store_to_database(df, table_name)
            log_info(f"Stored data in table: {table_name}")
            
        log_info("Pipeline completed successfully")
        print("\n✅ Process completed successfully.")

    except Exception as e:
        log_error(str(e))
        print("❌ Error:", e)


if __name__ == "__main__":
    main()