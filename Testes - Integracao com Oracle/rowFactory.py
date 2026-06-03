import collections
import cx_Oracle

#
# Exemplo de consulta 1
#
con = cx_Oracle.connect('pythonhol/welcome@127.0.0.1/orcl')

c_pes = con.cursor()
c_pes.execute("SELECT pes.nome, pes.telefone FROM pessoas pes WHERE pes.datanasc = TO_DATE('06/03/1978','DD/MM/YYYY')")
c_pes.rowfactory = collections.namedtuple("Pessoas", ["nome", "telefone"])

rows = c_pes.fetchall()
for row in rows:
    print(row.nome,',', row.telefone)

c_pes.close()