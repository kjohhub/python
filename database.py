# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 11:43:25 2021

@author: 경진
"""

import sqlite3


### create table & insert
con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute("DROP TABLE IF EXISTS tblAddr")
cursor.execute("CREATE TABLE tblAddr \
               (name CHAR(16) PRIMARY KEY, phone CHAR(16), addr TEXT)")

cursor.execute("INSERT INTO tblAddr VALUES ('김상형', '123-4567', '오산')")
cursor.execute("INSERT INTO tblAddr VALUES ('한경은', '555-1004', '수원')")
cursor.execute("INSERT INTO tblAddr VALUES ('한주완', '444-1092', '대전')")

con.commit()

cursor.close()
con.close()


### select : fetchall
con = sqlite3.connect("addr.db")
cursor = con.cursor()

cursor.execute("SELECT * FROM tblAddr")
table = cursor.fetchall()
for record in table:
    print("이름 : %s, 전화 : %s, 주소: %s" % record)
    
cursor.close()
con.close()


### select2 : fetchone
con = sqlite3.connect("addr.db")
cursor = con.cursor()

cursor.execute("SELECT * FROM tblAddr ORDER BY addr DESC")
while True:
    record = cursor.fetchone()
    if record == None:
        break
    else:
        print("이름 : %s, 전화 : %s, 주소 :%s" % record)

cursor.close()
con.close()


### update
con = sqlite3.connect("addr.db")
cursor = con.cursor()

cursor.execute("UPDATE tblAddr SET addr = '제주도' WHERE name = '김상형'")
con.commit()

cursor.close()
con.close()


### delete
con = sqlite3.connect("addr.db")
cursor = con.cursor()

cursor.execute("DELETE FROM tblAddr WHERE name = '한경은'")
con.commit()


cursor.close()
con.close()




