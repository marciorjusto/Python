import cx_Oracle

con = cx_Oracle.connect('pythonhol/welcome@127.0.0.1/orcl')

c_Eleitos = con.cursor()
c_Eleitos.execute('SELECT pes.nome FROM pessoas pes WHERE pes.codigo = 1')
for r_Eleito in c_Eleitos:
    print('Nome: ' + r_Eleito[0])
c_Eleitos.close()

con.close()