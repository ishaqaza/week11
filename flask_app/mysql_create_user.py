import mysql.connector as sql

conn = sql.connect(host="Ishaq", user="root")
cur = conn.cursor()

# Test connection
print(conn)

cmd = "CREATE USER 'flask'@'Ishaq' IDENTIFIED BY 'ubuntu';"
cur.execute(cmd)

cmd = "GRANT ALL PRIVILEGES ON *.* TO 'flask'@'Ishaq' WITH GRANT OPTION;"
cur.execute(cmd)

cmd = "FLUSH PRIVILEGES;"
cur.execute(cmd)

conn.close()
