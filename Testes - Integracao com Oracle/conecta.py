import cx_Oracle

# Inicia conexão
con = cx_Oracle.connect('pythonhol/welcome@127.0.0.1/orcl')

print(con.version)

# Encerra conexão
con.close()