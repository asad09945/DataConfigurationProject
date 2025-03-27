import mysql.connector
import xml.etree.ElementTree as ET

def load_xml_to_ER_visits(xml_file):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="As@d9852",
        database="LocalDB",
    )
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ER_visits (
            id INT AUTO_INCREMENT PRIMARY KEY,
            date_admitted DATE,
            date_discharged DATE,
            reason_for_visit VARCHAR(255),
            total_length_of_stay INT,
            diagnosis VARCHAR(255),
            discharge_notes VARCHAR(255)
        )
    ''')

    # Parse XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Insert data into database
    for visit in root.findall("Visit"):
        date_admitted = visit.find("date_admitted").text
        date_discharged = visit.find("date_discharged").text
        reason_for_visit = visit.find("reason_for_visit").text
        total_length_of_stay = visit.find("total_length_of_stay").text
        diagnosis = visit.find("diagnosis").text
        discharge_notes = visit.find("discharge_notes").text

        cursor.execute('''
            INSERT INTO ER_visits (date_admitted, date_discharged, reason_for_visit, total_length_of_stay, diagnosis, discharge_notes) 
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', (date_admitted, date_discharged, reason_for_visit, total_length_of_stay, diagnosis, discharge_notes))

    conn.commit()
    conn.close()

# Example usage:
load_xml_to_ER_visits("/Users/asadejaz/PycharmProjects/DataConfigurationProject/ER_isitsF.xml")