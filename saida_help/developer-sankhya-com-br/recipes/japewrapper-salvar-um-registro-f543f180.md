---
id: "https://developer.sankhya.com.br/recipes/japewrapper-salvar-um-registro"
titulo: "Japewrapper - Salvar um registro"
url: "https://developer.sankhya.com.br/recipes/japewrapper-salvar-um-registro"
atualizado_em: "2025-11-10T23:38:35.000Z"
---

# Japewrapper - Salvar um registro

```java Java
/*
	 * @ejb.interface-method tview-type="remote"
	 * @ejb.transaction type="Required"
	*/
	public void saveUsingJape(ServiceContext ctx) throws MGEModelException {

		JapeSession.SessionHandle hnd = null;
		try {
			hnd = JapeSession.open();
			JapeWrapper empresaDAO = JapeFactory.dao("Empresa");
			DynamicVO save = empresaDAO.create()
				.set("RAZAOABREV", "Sankhya")
				.set("NOMEFANTASIA", "Sankhya gestão")
				.set("RAZAOSOCIAL", "Sankhya Gestão de Negócios")
				.set("TELEFONE", "(34) 3239-0700")
				.save();
			
			JsonObject jr = new JsonObject();
			jr.addProperty("codempsaved", save.asBigDecimal("CODEMP").toString());
			ctx.setJsonResponse(jr);
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

# Abertura do objeto

<!-- java@7 -->

Abertura do objeto de sessionHandle

# Abertura da sessão

<!-- java@9 -->



# Instanciamento do JapeWrapper

<!-- java@10 -->

O instanciamento é feito através do DAO, para usar a tabela "empresa"

# Criação das colunas da tabela

<!-- java@12-16 -->

O objeto é criado, criando uma coluna vazia no campo, setando as colunas que deseja preencher e o dado a ser inserido.

# Acessando o objeto de retorno

<!-- java@18-20 -->

O objeto é setado no json e é retornado.

# ThrowMe - Erro

<!-- java@22 -->

Prevenção de erros

# Finalização da sessão

<!-- java@23-26 -->
