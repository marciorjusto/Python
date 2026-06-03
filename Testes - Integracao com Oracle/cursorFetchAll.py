import cx_Oracle

#
# Exemplo de consulta 1
#
con = cx_Oracle.connect('pythonhol/welcome@127.0.0.1/orcl')

c_Eleitos = con.cursor()
c_Eleitos.execute("SELECT pes.nome FROM pessoas pes WHERE pes.datanasc = TO_DATE('06/03/1978','DD/MM/YYYY')")
lst_nascidos = c_Eleitos.fetchall()
print(lst_nascidos)
for l_pessoa in lst_nascidos:
    print("Pessoa que faz aniversário no mesmo dia que eu: " + l_pessoa[0])
c_Eleitos.close()

#
# Exemplo de consulta 2
#
print("----")
c_Eleitos = con.cursor()
c_Eleitos.execute("SELECT pes.nome, pes.telefone, pes.email FROM pessoas pes WHERE pes.codigo = 1")
for l_nome, l_telefone, l_email in c_Eleitos:
    print("Nome....: ", l_nome)
    print("Telefone: ", l_telefone)
    print("E-mail..: ", l_email)

c_Eleitos.close()