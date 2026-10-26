---
id: "https://developer.sankhya.com.br/recipes/japewrapper-buscar-coleção-pelo-find"
titulo: "Japewrapper - Buscar coleção pelo find"
url: "https://developer.sankhya.com.br/recipes/japewrapper-buscar-coleção-pelo-find"
atualizado_em: "2025-11-10T23:38:34.000Z"
---

# Japewrapper - Buscar coleção pelo find

```java Java
/*
	 * @ejb.interface-method tview-type="remote"
	 * @ejb.transaction type="Required"
	*/
	public void findColection(ServiceContext ctx) throws MGEModelException {

		JapeSession.SessionHandle hnd = null;
		try {
			hnd = JapeSession.open();
			JapeWrapper empresaDAO = JapeFactory.dao(DynamicEntityNames.EMPRESA);
			Collection<DynamicVO> dynamicVOs = empresaDAO.find("RAZAOSOCIAL = ?", "EMPRESA MODELO");
			for (DynamicVO empVO : dynamicVOs) {
				System.out.println(empVO.asBigDecimal("CODEMP"));
			}
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

# Atribuição collection

<!-- java@11 -->

Os resultados do DAO.find, são guardados na Collection<DynamicVO>

# Execução das regras de negocio

<!-- java@12-13 -->

As regras serão executadas, neste exemplo estamos apenas imprimindo o "CODEMP"

# ThrowMe - Erro

<!-- java@16 -->

Prevenção de erros

# Finalização da sessão

<!-- java@17-20 -->
