import sqlite3

import sys


database = sqlite3.connect('preloaded_images.db')
cursor = database.cursor()
# cursor.execute("""CREATE TABLE Images(Id INTEGER PRIMARY KEY, Data BLOB);""")

def readImage(path):
    fin = open(path, "rb")
    img = fin.read()
    return img


def uploadPhoto2db(path):
    data = readImage(path)
    binary = sqlite3.Binary(data)
    cursor.execute("INSERT INTO Images(Data) VALUES (?)", (binary,))
    database.commit()
    database.close()

# uploadPhoto2db('C:/Users/Пользователь/Desktop/albert.jpg')
# for i in cursor.execute("SELECT * FROM Images"):
#     print(i)

def fromDB2Img(num):
    binar = cursor.execute(
        f"""SELECT Data FROM Images
        WHERE Id=={num}""")
    with open('to_edit.jpg', 'wb') as img:
        for i in binar:
            img.write(i[0])
