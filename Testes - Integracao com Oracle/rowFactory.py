import collections
import cx_Oracle

#
# Exemplo de consulta 1
#
con = cx_Oracle.connect('pythonhol/welcome@127.0.0.1/orcl')

c_Eleitos = con.cursor()
c_Eleitos.execute("SELECT pes.nome, pes.telefone FROM pessoas pes WHERE pes.datanasc = TO_DATE('06/03/1978','DD/MM/YYYY')")
c_Eleitos.rowfactory = collections.namedtuple("Pessoas", ["nome", "telefone"])

lst_pessoas = c_Eleitos.fetchall()
for l_pessoa in lst_pessoas:
    print(l_pessoa.nome,',', l_pessoa.telefone)

c_Eleitos.close()