---
id: "https://developer.sankhya.com.br/recipes/japewrapper-remover-um-registro-pela-pk"
titulo: "Japewrapper - Remover um registro pela PK"
url: "https://developer.sankhya.com.br/recipes/japewrapper-remover-um-registro-pela-pk"
atualizado_em: "2025-11-10T23:38:35.000Z"
---

# Japewrapper - Remover um registro pela PK

```java Java
/*
	 * @ejb.interface-method tview-type="remote"
	 * @ejb.transaction type="Required"
	*/
	public void deleteUsingPK(ServiceContext ctx) throws MGEModelException {

		JapeSession.SessionHandle hnd = null;
		try {
			hnd = JapeSession.open();
			JapeWrapper empresaDAO = JapeFactory.dao(DynamicEntityNames.EMPRESA);
			empresaDAO.delete(BigDecimal.valueOf(14));
		} catch (Exception e) {
			MGEModelException.throwMe(e);
		} finally {
			JapeSession.close(hnd);
		}
	}
```

```json Response Example
{"success":true}
```

# Indicação de transação automática

<!-- java@1-4 -->

Comentário padrão indicando a transação automática.

# Abertura da sessão

<!-- java@7 -->



# Vinculação ao JapeWrapper a entidade de empresa

<!-- java@10 -->



# Declaração do tipo de variável

<!-- java@11 -->

BigDecimal - Coluna numérica

# ThrowMe - Erro

<!-- java@13 -->

Prevenção de erros

# Finalização da sessão

<!-- java@14-17 -->
