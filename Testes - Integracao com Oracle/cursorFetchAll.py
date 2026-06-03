import cx_Oracle

#
# Exemplo de consulta 1
#
con = cx_Oracle.connect('pythonhol/welcome@127.0.0.1/orcl')

c_func = con.cursor()
c_func.execute("SELECT pes.nome FROM pessoas pes WHERE pes.datanasc = TO_DATE('06/03/1978','DD/MM/YYYY')")
nascidos = c_func.fetchall()
print(nascidos)
for pessoa in nascidos:
    print("Pessoas que fazem aniversário no mesmo dia que eu:" + pessoa[0])
c_func.close()

#
# Exemplo de consulta 2
#
print("----")
c_dadospes = con.cursor()
c_dadospes.execute("SELECT pes.nome, pes.telefone, pes.email FROM pessoas pes WHERE pes.codigo = 1")
for nome, telefone, email in c_dadospes:
    print("Nome....: ", nome)
    print("Telefone: ", telefone)
    print("E-mail..: ", email)

c_dadospes.close()