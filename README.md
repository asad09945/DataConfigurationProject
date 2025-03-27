# DataConfigurationProject
# Data Configuration Project

## Project Overview
This project focuses on efficient data exchange and extraction using XML files and MySQL. The key objectives include:
- Creating XML files for structured data storage.
- Automating data extraction from XML and loading it into MySQL.
- Designing a relational database through reverse engineering.
- Running advanced queries to extract meaningful insights from the data.

## Technologies Used
- **Python**: Automating data extraction and loading.
- **MySQL**: Storing and querying structured data.
- **XML**: Structured data exchange format.

## Project Structure
```
├── LoadDataIntoSQL/         # Python scripts for data extraction & loading
├── ExampleQueries/          # Sample SQL queries and screenshots
├── CreatingRelationalDatabase.png  # Visualization of relational database
├── BillsF.xml               # Sample XML file
├── ER_visitsF.xml           # Sample XML file
├── Patient_information.xml  # Sample XML file
└── README.md                # Project documentation
```

## How It Works
### 1. XML Data Creation
- Custom XML files (`BillsF.xml`, `ER_visitsF.xml`, `Patient_information.xml`) were created for efficient data exchange.

### 2. Automated Data Extraction & Loading
- Python scripts automate the extraction of XML data and insert it into a MySQL database.
- The extraction scripts can be found in the `LoadDataIntoSQL` folder.

### 3. Creating a Relational Database
- Reverse engineering was used to convert the extracted data into a relational database.
- Database schema can be viewed in `CreatingRelationalDatabase.png`.

### 4. Running SQL Queries
- Initial queries were executed on the loaded data (`ExampleQueries/Screenshot1.png`).
- Advanced queries were performed after establishing the relational database (`ExampleQueries/Screenshot3.png`).

## Getting Started
### Prerequisites
Ensure you have the following installed:
- Python (3.x)
- MySQL Server
- MySQL Connector for Python (`pip install mysql-connector-python`)

### Setup Instructions
1. Clone the repository:
   ```sh
   git clone <your-repo-link>
   ```
2. Navigate to the project directory:
   ```sh
   cd <project-folder>
   ```
3. Run the Python script to load XML data into MySQL:
   ```sh
   python LoadDataIntoSQL/load_data.py
   ```
4. Execute queries on the MySQL database using the provided SQL scripts in `ExampleQueries`.

## Project Link
https://github.com/asad09945/DataConfigurationProject/edit/main/README.md

## Contact
For any questions or contributions, feel free to open an issue or reach out!

