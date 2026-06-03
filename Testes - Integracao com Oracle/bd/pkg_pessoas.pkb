CREATE OR REPLACE PACKAGE BODY PKG_PESSOAS
IS
  /**************************************************************
   Validações referentes ao Cadastro de pessoas - Implementações
   %author  Marcio Justo
   %created 02/06/2026
   **************************************************************/

  --=== Métodos - Procedures ou Funções

  /** Implementação do método PKG_PESSOAS.nomeByCod */
  FUNCTION nomeByCod(p_codigo IN PESSOAS.codigo%TYPE)
    RETURN PESSOAS.nome%TYPE;
  IS
    v_nome PESSOAS.nome%TYPE;
  BEGIN
    SELECT pes.nome
      INTO v_nome
      FROM pessoas pes
     WHERE pes.codigo = p_codigo;

    RETURN v_nome;

  EXCEPTION
   WHEN OTHERS
    THEN RETURN(NULL);
  END nomeByCod;

END PKG_PESSOAS;