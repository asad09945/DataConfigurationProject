import mysql.connector
import xml.etree.ElementTree as ET

def load_xml_to_patient_information(xml_file):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="As@d9852",
        database="LocalDB",
    )
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patient_information (
            patient_id INT PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            date_of_birth DATE
        )
    ''')

    # Parse XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Insert data into database
    for patient in root.findall("Patient"):
        patient_id = patient.find("patient_id").text
        first_name = patient.find("first_name").text
        last_name = patient.find("last_name").text
        date_of_birth = patient.find("date_of_birth").text

        cursor.execute('''
            INSERT INTO patient_information (patient_id, first_name, last_name, date_of_birth) 
            VALUES (%s, %s, %s, %s)
        ''', (patient_id, first_name, last_name, date_of_birth))

    conn.commit()
    conn.close()

# Example usage:
load_xml_to_patient_information("/Users/asadejaz/PycharmProjects/DataConfigurationProject/Patients_information.xml")