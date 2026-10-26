---
id: "https://developer.sankhya.com.br/recipes/japewrapper-remover-um-registro-pelo-finder"
titulo: "Japewrapper - Remover um registro pelo finder"
url: "https://developer.sankhya.com.br/recipes/japewrapper-remover-um-registro-pelo-finder"
atualizado_em: "2025-11-10T23:38:35.000Z"
---

# Japewrapper - Remover um registro pelo finder

```java Java
/** 
	 * @throws MGEModelException
	 * @ejb.interface-method tview-type="remote"
	 * @ejb.transaction type="Required"
	 * */
	public void removeSearchConfig(ServiceContext ctx) throws MGEModelException {	
		SessionHandle hnd = null;
		// DESCRIPTOR_CONFIG_KEY	= "PesqCfg:com.sankhya.search.descriptor.{entityName}"
		try {
			hnd = JapeSession.open();
			String entityName = ctx.getJsonRequestBody().get("entityName").getAsString();
					
			BigDecimal codUsu = ((AuthenticationInfo) ctx.getAutentication()).getUserID();
			
			String key = PesquisaHelper.DESCRIPTOR_CONFIG_KEY.replace("{entityName}", entityName);
			JapeWrapper configDao = JapeFactory.dao(DynamicEntityNames.CONFIGURACAO_RECURSO);
			configDao.deleteByCriteria("CHAVE = ? AND CODUSU = ?", key, codUsu);
			
		} catch (Exception e) {
			MGEModelException.throwMe(e);
		}finally {
			JapeSession.close(hnd);
		}
	}
```

```json Response Example
{"success":true}
```

# Indicação de transação automática

<!-- java@1-5 -->

Comentário padrão indicando a transação automática.

# Abertura do objeto

<!-- java@7 -->

Abertura do objeto de handle

# Descrição string

<!-- java@8 -->

String que será utilizada no codigo

# Inicialização da sessão

<!-- java@10 -->



# Atribuição da entidade que será deletada

<!-- java@12 -->



# Retorno do cod de usuário que solicitou o serviço

<!-- java@13 -->



# Construção do objeto string

<!-- java@15 -->



# Remoção do registro

<!-- java@16-17 -->



# ThrowMe - Erro

<!-- java@20 -->

Prevenção de erros

# Finalização da sessão
