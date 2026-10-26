---
id: "https://developer.sankhya.com.br/recipes/japewrapper-atualizar-um-registro-pk"
titulo: "Japewrapper - Atualizar um registro PK"
url: "https://developer.sankhya.com.br/recipes/japewrapper-atualizar-um-registro-pk"
atualizado_em: "2025-11-10T23:38:35.000Z"
---

# Japewrapper - Atualizar um registro PK

```java Java
/*
	 * @ejb.interface-method tview-type="remote"
	 * @ejb.transaction type="Required"
	*/
	public void atualizandoSituacaoByPK(ServiceContext ctx) throws MGEModelException {
		SessionHandle hnd = null;
		try {
			hnd = JapeSession.open();
			JsonObject req = ctx.getJsonRequestBody();

			JapeFactory.dao(DynamicEntityNames.EMPRESA).
			prepareToUpdateByPK(req.get("CODEMP").getAsBigDecimal())
			.set("DHALTERACAO", new Timestamp(System.currentTimeMillis()))
			.set("ATIVO", req.get("ATIVO").getAsString())
			.update();

		} catch (Exception e) {
			throwExceptionRollingBack(e);
		} finally {
			JapeSession.close(hnd);
		}
	}
```

```json Response Example
{"success":true}
```

# Abertura da sessão

<!-- java@6 -->



# Indicação de transação automática

<!-- java@1-4 -->

Comentário padrão indicando a transação automática.

# Leitura dos parâmetros de entrada

<!-- java@9 -->



# Acesso ao DAO

<!-- java@11 -->



# Preparação de UPDATE

<!-- java@12 -->



# Alteração de campos

<!-- java@13-14 -->



# Update

<!-- java@15 -->



# RollingBack - Se houver erros

<!-- java@18 -->



# Finalização da sessão

<!-- java@19-22 -->
