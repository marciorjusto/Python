CREATE OR REPLACE PACKAGE PKG_PESSOAS
IS
  /*********************************************
   Validações referentes ao Cadastro de pessoas
   %author  Marcio Justo
   %created 02/06/2026
   *********************************************/

  --=== Métodos - Procedures ou Funções

  /**
   Retorna nome da pessoa a partir do código
   %Author Marcio Justo
   %created 02/06/2026
   %param p_codigo PESSOAS.codigo
   %return PESSOAS.nome%TYPE
   */
  FUNCTION nomeByCod(p_codigo IN PESSOAS.codigo%TYPE)
    RETURN PESSOAS.nome%TYPE;

END PKG_PESSOAS;