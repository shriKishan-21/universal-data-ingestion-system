import pandas as pd
import os
   
def detect_file_format(file_path):
    return os.path.splitext(file_path)[1].lower()

def load_data(file_path):
    file_ext = detect_file_format(file_path)
    
    if file_ext == '.csv':
        return pd.read_csv(file_path)
    elif file_ext in ['.xls', '.xlsx']:
        return pd.read_excel(file_path)
    elif file_ext == '.json':
        data = pd.read_json(file_path)
         
        if isinstance(data.iloc[0, 0], dict):
            data = pd.json_normalize(data.iloc[:, 0])
        return data
    
    else:
        raise ValueError("Unsupported file format")
    

SUPPORTED_EXTENSIONS = [".csv", ".xls", ".xlsx", ".json"]

def load_files_from_folder(folder_path):
    dataframes = []
    
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path,file)
        ext = os.path.splitext(file)[1].lower()
        
        if ext in SUPPORTED_EXTENSIONS:
            try:
                df=load_data(file_path)
                dataframes.append((file,df))
            except Exception as e:
                print("Error loading file:", file, "Error:", e)
                
    return dataframes
                