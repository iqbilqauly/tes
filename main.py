from sklearn.neighbors import LocalOutlierFactor
import matplotlib.pyplot as plt
import psycopg2

# Informasi koneksi ke database PostgreSQL di cloud Aiven
hostname = 'pg-3e119ea2-andi176.a.aivencloud.com'
port = 14814
username = 'avnadmin'
password = 'AVNS_8X2P-_6dzJylk3YECuH'
database = 'defaultdb'

# Membuat koneksi ke database PostgreSQL
conn = psycopg2.connect(
    host=hostname,
    port=port,
    user=username,
    password=password,
    database=database
)

# Membaca data dari database menggunakan Pandas
query = "SELECT sepallengthcm, sepalwidthcm FROM iris"
cursor = conn.cursor()
cursor.execute(query)
rows = cursor.fetchall()
x = [[row[0], row[1]] for row in rows]

# Menutup koneksi ke database
conn.close()
