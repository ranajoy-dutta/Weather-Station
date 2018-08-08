import sqlite3

try:
    conn = sqlite3.connect("ws_db.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE dataTable_losant ("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, humidity TEXT(5), timestamps TEXT(5))")

    conn.commit()
    cur.close()
    conn.close()
    print("Table Successfully Created!")
except Exception as e:
    print("An error occurred!\n",
          "Reason : ",e)
