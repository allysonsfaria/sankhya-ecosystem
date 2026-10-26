---
id: "https://developer.sankhya.com.br/recipes/jape-nativesql"
titulo: "Jape - NativeSQL"
url: "https://developer.sankhya.com.br/recipes/jape-nativesql"
atualizado_em: "2025-11-10T23:38:33.000Z"
---

# Jape - NativeSQL

```java Java
/**
	 * @throws MGEModelException
	 * @ejb.interface-method tview-type="remote"
	 */
	public void exemploNativeSql(ServiceContext ctx) throws MGEModelException {
		
		JdbcWrapper jdbc = null;
		NativeSql sql = null;
		ResultSet rset = null;
		SessionHandle hnd = null;

		try {
			hnd = JapeSession.open();
			hnd.setFindersMaxRows(-1);
			EntityFacade entity = EntityFacadeFactory.getDWFFacade();
			jdbc = entity.getJdbcWrapper();
			jdbc.openSession();

			sql = new NativeSql(jdbc);

			sql.appendSql("SELECT * FROM TSIPAR WHERE CHAVE = :CHAVE AND CODUSU = :CODUSU");

			sql.setNamedParameter("CHAVE", "UTILIZAHTML5");
			sql.setNamedParameter("CODUSU", BigDecimal.ZERO);

			rset = sql.executeQuery();

			if (rset.next()) {
				boolean utilizaHtml = "S".equals(rset.getString("LOGICO"));
			}

		} catch (Exception e) {
			MGEModelException.throwMe(e);
		} finally {
			JdbcUtils.closeResultSet(rset);
			NativeSql.releaseResources(sql);
			JdbcWrapper.closeSession(jdbc);
			JapeSession.close(hnd);

		}
	}
```

```json Response Example
{"success":true}
```

# Setar Objetos

<!-- java@7-10 -->

Inicializando JdbcWrapper, NativeSql, ResultSet e SessionHandle

# Inicializando hnd

<!-- java@13 -->

Inicializando hnd, abrindo sessão

# jdbc é recebido

<!-- java@16 -->

jdbc é recebido

# Abertura da sessão

<!-- java@17 -->

Abertura da sessão

# Inicialização do objeto do NativeSQL

<!-- java@19 -->

Inicialização do objeto do NativeSQL

# Possibilidade de adicionar string , setando qual SELECT será executado no banco de dados, ou parâmetros

<!-- java@21 -->

Possibilidade de adicionar string , setando qual SELECT será executado no banco de dados

Parâmetros são antecedidos de ":" neste exemplo temos os parâmetros CHAVE e CODUSU

# Setar parâmetros p/ valor real

<!-- java@23-24 -->

É relevante utilizar os parâmetros quando é necessário usar tipos de variáveis diferentes.

# Execução dos parâmetros (query)

<!-- java@26 -->

Execução dos parâmetros (query)

# Primeiro valor é recebido

<!-- java@28-29 -->

Primeiro valor é recebido

# Prevenção de erros

<!-- java@32-33 -->

Prevenção de erros

# Fechamento de todos os objetos

<!-- java@35-38 -->

Boa prática de fechamento de todos os objetos
