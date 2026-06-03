import cx_Oracle

#---------------------------------------------------------
# OBS: Ver também a stored procedure bd\exibe_Msg_MRJ.prc
#---------------------------------------------------------

con = cx_Oracle.connect('pythonhol/welcome@127.0.0.1/orcl')

c_pes = con.cursor()

# Variável de retorno (OUT)
l_out_msg = c_pes.var(cx_Oracle.STRING)

# Chamada da Stored Procedure - último parâmetro é o retorno
c_pes.callproc('exibe_Msg_MRJ', ['Justo', l_out_msg])
print(l_out_msg.getvalue())
c_pes.close()

con.close()