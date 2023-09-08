import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="*****",
    database="Iris"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE iristb (Id INT AUTO_INCREMENT PRIMARY KEY, SepalLengthCm DECIMAL(10, 1), SepalWidthCm DECIMAL(10, 1), PetalLengthCm DECIMAL(10, 1), PetalWidthCm DECIMAL(10, 1), Species VARCHAR(255))")

# Pandas kullanarak CSV'den veri yükleme
df=pd.read_csv('C:/Peace/Kişisel/Code/Iris.csv')


# DataFrame üzerinde dolaşıp verileri MySQL tablosuna ekliyoruz
for index, row in df.iterrows():
    sql = "INSERT INTO iristb (SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm, Species) VALUES (%s, %s, %s, %s, %s)"
    val = (row['SepalLengthCm'], row['SepalWidthCm'], row['PetalLengthCm'], row['PetalWidthCm'], row['Species'])
    mycursor.execute(sql, val)

# Veritabanındaki değişiklikleri kaydediyoruz
mydb.commit()

