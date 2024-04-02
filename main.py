from sklearn.neighbors import LocalOutlierFactor
import matplotlib.pyplot as plt
import psycopg2

# Informasi koneksi ke database PostgreSQL di cloud Aiven

# Membuat koneksi ke database PostgreSQL
conn = psycopg2.connect(
    host=hostname,
    port=port,
    user=username,
    password=password,
    database=database
)

# Membaca data dari database menggunakan Pandas
cursor = conn.cursor()
cursor.execute(query)
rows = cursor.fetchall()
x = [[row[0], row[1]] for row in rows]

# Menutup koneksi ke database
conn.close()
