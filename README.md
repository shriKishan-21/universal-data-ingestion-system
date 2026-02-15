# Universal Data Ingestion System

A web-based and command-line **ETL (Extract–Transform–Load) system** that ingests datasets in multiple formats, cleans and normalizes them, stores them into a relational database, and allows users to execute SQL queries through an interactive interface.

This project is designed as a **final-year academic project** and also demonstrates **real-world data engineering practices**.

---

## 🚀 Features

- 📂 Upload datasets in **CSV, Excel, and JSON** formats
- 🧹 Automatic **data cleaning & normalization**
  - Duplicate removal
  - Column name standardization
  - Missing value handling
- 🔄 JSON normalization for semi-structured data
- 🗄️ Dynamic storage into **SQLite database**
- 📊 Automatic table creation (schema inferred from data)
- 📝 Logging of all operations
- 🌐 **Web application** for:
  - File upload
  - SQL query execution
  - Viewing query results
- 🖥️ Command-line support (CLI)
- 📁 Bulk ingestion (folder-level processing)

---

## 🏗️ System Architecture


---

## 🛠️ Technology Stack

| Layer | Technology |
|------|-----------|
| Programming Language | Python |
| Backend Framework | Flask |
| Data Processing | Pandas |
| Database | SQLite |
| ORM / DB Engine | SQLAlchemy |
| Frontend | HTML, CSS |
| Logging | Python logging module |

---

## 📂 Project Structure

SQL_PROJECT/  
│  
├── src/  
│ ├── app.py # Flask web application  
│ ├── main.py # CLI-based execution  
│ ├── loader.py # Data loading logic  
│ ├── cleaner.py # Data cleaning module  
│ ├── db_handler.py # Database operations  
│ ├── logger.py # Logging utilities  
│ └── init.py  
│  
├── templates/  
│ └── index.html # Web UI template  
│  
├── static/  
│ └── style.css # CSS styling  
│  
├── Data/ # Uploaded / raw datasets  
├── Database/  
│ └── data_store.db # SQLite database  
├── Logs/  
│ └── pipeline.log # Execution logs  
│  
├── requirements.txt  
└── README.md  
  
  
---



