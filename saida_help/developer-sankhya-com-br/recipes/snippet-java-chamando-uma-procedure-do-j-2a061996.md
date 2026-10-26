---
id: "https://developer.sankhya.com.br/recipes/snippet-java-chamando-uma-procedure-do-java"
titulo: "Snippet Java- Chamando uma procedure do JAVA"
url: "https://developer.sankhya.com.br/recipes/snippet-java-chamando-uma-procedure-do-java"
atualizado_em: "2025-11-10T23:38:36.000Z"
---

# Snippet Java- Chamando uma procedure do JAVA

```java Java
private void teste() {
	SessionHandle hnd = null;
	JdbcWrapper jdbc = null;

	try {
		hnd = JapeSession.open();
		EntityFacade dwfFacade = EntityFacadeFactory.getDWFFacade();

		jdbc = dwfFacade.getJdbcWrapper();
		jdbc.openSession();

		CallableStatement cstmt = jdbc.getConnection().prepareCall("{call STP_KEYGEN_TGFNUM(?,?,?,?,?,?)}");
		cstmt.setQueryTimeout(60);

		cstmt.setString(1, "TGFCAB");
		cstmt.setBigDecimal(2, BigDecimal.ONE);
		cstmt.setString(3, "TGFCAB");
		cstmt.setString(4, "NUNOTA");
		cstmt.setBigDecimal(5, BigDecimal.ZERO);
    
		cstmt.registerOutParameter(6, Types.BigDecimal);

		cstmt.execute();

		BigDecimal nunota = (BigDecimal) cstmt.getObject(6);

		System.out.println("Saida: " + nunota);
	} catch (Exception e) {
		e.printStackTrace();
	} finally {
		JdbcWrapper.closeSession(jdbc);
		JapeSession.close(hnd);
	}
}
```

```json Response Example
{"success":true}
```

# Instanciamento do Handle e jdbc

<!-- java@2-3 -->



# Abertura da sessão

<!-- java@6 -->



# Atribuição do DWFFacade

<!-- java@7 -->



# Jdbc recebe DWFFacade e é aberta a sessão no BD

<!-- java@9-10 -->



# Preparação da procedure

<!-- java@12 -->



# Configuração de timeout

<!-- java@13 -->



# Passagem dos parâmetros necessários

<!-- java@15-19 -->

"TGFCAB" nome da tabela
"TGFCAB" nome do arquivo
 "NUNOTA" nome do campo

# Passagem argumento de saida

<!-- java@21 -->



# Chamada da procedure

<!-- java@23 -->



# Leitura do argumento de saida

<!-- java@25 -->



# Impressão da saída

<!-- java@27 -->



# Finalização da sessão jdbc e handle

<!-- java@30-34 -->
