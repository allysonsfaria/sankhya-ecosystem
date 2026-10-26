---
id: "https://developer.sankhya.com.br/recipes/jape-nativesqlwithbatch-1"
titulo: "Jape - NativeSQLWithBatch"
url: "https://developer.sankhya.com.br/recipes/jape-nativesqlwithbatch-1"
atualizado_em: "2025-11-10T23:38:32.000Z"
---

# Jape - NativeSQLWithBatch

```java Java
public void usandoNativeSqlWithBatch(ServiceContext ctx) throws MGEModelException {
		JapeSession.SessionHandle hnd = null;
		JdbcWrapper jdbc = null;
		try{
			hnd = JapeSession.open();
			jdbc = EntityFacadeFactory.getDWFFacade().getJdbcWrapper();
			jdbc.openSession();
			
			Element produtos = XMLUtils.getRequiredChild(ctx.getRequestBody(), "produtos");
			String grupoDesconto = XMLUtils.getAttributeAsString(produtos, "grupodesconto");
			
			NativeSql queryUpd = new NativeSql(jdbc);
			queryUpd.appendSql("UPDATE TGFPRO SET GRUPODESCPROD = :GRUPODESCONTO WHERE CODPROD = :CODPROD");
			queryUpd.setReuseStatements(true);
			queryUpd.setBatchUpdateSize(500);
			
			for(Object produto : produtos.getChildren()){
				BigDecimal codProd = XMLUtils.getAttributeAsBigDecimal((Element) produto, "codprod");
				queryUpd.setNamedParameter("CODPROD", codProd);
				queryUpd.setNamedParameter("GRUPODESCONTO", grupoDesconto);
				queryUpd.addBatch();
				queryUpd.cleanParameters();
			}
			queryUpd.flushBatchTail();
			NativeSql.releaseResources(queryUpd);
			
		} catch(Exception e) {
			throwExceptionRollingBack(e);
		} finally {
			JdbcWrapper.closeSession(jdbc);
			JapeSession.close(hnd);
		}
	}
```

```json Response Example
{"success":true}
```

# Inicio do código

<!-- java@1 -->

Inicio do código. processando de x em x os elementos, evitando a ida ao banco a cada update.

# Instanciamento da sessão

<!-- java@2 -->

A sessão hnd instanciada;

# Instanciamento do objeto

<!-- java@3 -->

Jdbc é instanciado.

# Try catch finally- Prevenção de erros

<!-- java@4-31 -->

Por padrão. é criado um try para garantir que a sessão será fechada, prevenindo erros.

# Abertura da sessão

<!-- java@5 -->

Abertura da sessão

# Atribuição do objeto jdcb do Wrapper do framework

<!-- java@6 -->

Atribuição do objeto jdcb do Wrapper do framework

# Abertura de sessão para o jdbc

<!-- java@7 -->

Abertura de sessão para o jdbc

# Atribuição da entidade pelo RequestBody

<!-- java@9 -->

A entidade "produtos" é atribuída ao RequestBody

# Leitura do conteúdo da TAG

<!-- java@10 -->

É feita a leitura do conteúdo da TAG "grupodesconto", que esta dentro de "produtos"

# Inicialização do objeto de NativeSQL

<!-- java@12 -->

O objeto é inicializado passando o jdbc.

# Montagem do UPDATE a ser executado.

<!-- java@13 -->

registro do update da "TGFPRO" setando o "GRUPODESCPROD" (string) para todos os "CODPROD"

# ReuseStatements - Utilização do argumento varias vezes

<!-- java@14 -->

Utilizado para consumir menos memoria

# Atribuição do tamanho do batch

<!-- java@15 -->

A cada 500 updates armazenados, será feito um commit (flush) do comando.

# Interação da TAG de Produtos

<!-- java@17 -->

Interação da TAG de Produtos

# Atribuição de argumentos

<!-- java@18 -->

são utilizados os argumentos "codprod" e  "grupoDesconto"

# Atribuição de parâmetros

<!-- java@19-20 -->

Serão setados os parâmetros "CODPROD" e "GRUPODESCONTO",

# AddBatch - Contagem

<!-- java@21 -->

Insere um elemento e confere se chegou no tamanho do batch. Se sim o commite é feito, se não o update é registrado até completar 500

# CleanParameters - Zeragem dos parâmetros

<!-- java@22 -->

Utilizado para zerar os parâmetros  e ser possível seu preenchimento novamente.

# FlushBatchTail - Limpa comandos em memória

<!-- java@24 -->

Limpa comandos não executados em memória

# Liberação do objeto de nativeSQL

<!-- java@25 -->

Uma vez que todos os comandos foram executados, o objeto de nativeSQL pode ser liberado.

# Finalização - limpeza da memória jdbc e hnd

<!-- java@29-32 -->

é feita a finalização, limpando a memória dojdbc e hnd
