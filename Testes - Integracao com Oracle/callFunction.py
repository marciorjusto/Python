import cx_Oracle

#---------------------------------------------------------
# OBS: Ver também a function bd\PKG_PESSOAS.nomeByCod()
#---------------------------------------------------------

con = cx_Oracle.connect('pythonhol/welcome@127.0.0.1/orcl')

c_pes = con.cursor()
l_nome = c_pes.callfunc('PKG_PESSOAS.nomeByCod', cx_Oracle.STRING, [3])
print(l_nome)
c_pes.close()

con.close()
