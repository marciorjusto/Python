import cx_Oracle

con = cx_Oracle.connect('pythonhol/welcome@127.0.0.1/orcl')

c_func = con.cursor()
c_func.execute('SELECT pes.nome FROM pessoas pes WHERE pes.codigo = 1')
for r_func in c_func:
    print(r_func[0])
c_func.close()

con.close()