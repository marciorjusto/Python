CREATE PROCEDURE exibe_Msg_MRJ( p_nome IN PESSOAS.nome%TYPE
                              , p_msg OUT VARCHAR2
                              )
IS
  /**************************************************************
   Teste de retorno de mensagem
   %author Marcio Justo
   %created 02/06/2026
   **************************************************************/
BEGIN
  --
  p_msg := 'Mensagem enviada de ' || p_nome || ' para MRJ';
  --
END exibe_Msg_MRJ;
/
