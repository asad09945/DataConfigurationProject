import mysql.connector
import xml.etree.ElementTree as ET

def load_xml_to_database(xml_file):
    # Connect to the SQLite database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="As@d9852",
        database="LocalDB",
    )
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute('''
           CREATE TABLE IF NOT EXISTS ER_bills (
             total_amount INT,
             copay INT,
             payable_amount INT
           )
       ''')

    # Parse XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Insert data into database
    for visit in root.findall("Bill"):
        total_amount = visit.find("total_amount").text
        copay = visit.find("copay").text
        payable_amount = visit.find("payable_amount").text
        cursor.execute('''
            INSERT INTO ER_bills (total_amount, copay, payable_amount) 
            VALUES (%s, %s, %s)
        ''', (total_amount, copay, payable_amount) )

    conn.commit()
    conn.close()

load_xml_to_database("/Users/asadejaz/PycharmProjects/DataConfigurationProject/BillsF.xml")
