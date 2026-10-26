---
id: "https://developer.sankhya.com.br/recipes/japewrapper-buscar-um-registro-pelo-find"
titulo: "Japewrapper - Buscar um registro pelo find"
url: "https://developer.sankhya.com.br/recipes/japewrapper-buscar-um-registro-pelo-find"
atualizado_em: "2025-11-10T23:38:34.000Z"
---

# Japewrapper - Buscar um registro pelo find

```java Java
/*
	 * @ejb.interface-method tview-type="remote"
	 * @ejb.transaction type="Required"
	*/
	public void findOneByFind(ServiceContext ctx) throws MGEModelException {

		JapeSession.SessionHandle hnd = null;
		try {
			hnd = JapeSession.open();
			JapeWrapper empresaDAO = JapeFactory.dao(DynamicEntityNames.EMPRESA);
			DynamicVO empresa = empresaDAO.findOne(" UPPER(NOMEFANTASIA) = 'SANKHYA TECNOLOGIA EM SISTEMAS LTDA'");
			System.out.println(empresa.asBigDecimal("CODEMP"));
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

Abertura do objeto de handle

# Abertura da sessão

<!-- java@9 -->

Abertura da sessão

# Instanciamento do JapeWrapper

<!-- java@10 -->

O instanciamento é feito através do DAO,  para usar a tabela "empresa"

# Find one

<!-- java@11 -->

O SELECT é executado através de parâmetros. Traz apenas o primeiro resultado.

# Execução das regras de negocio

<!-- java@12 -->

As regras serão executadas, neste exemplo estamos apenas imprimindo o "CODEMP"

# ThrowMe - Erro

<!-- java@14 -->

Prevenção de erros

# Finalização da sessão

<!-- java@15-18 -->
