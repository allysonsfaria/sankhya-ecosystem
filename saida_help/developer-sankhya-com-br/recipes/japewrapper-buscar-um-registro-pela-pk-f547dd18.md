---
id: "https://developer.sankhya.com.br/recipes/japewrapper-buscar-um-registro-pela-pk"
titulo: "Japewrapper - Buscar um registro pela PK"
url: "https://developer.sankhya.com.br/recipes/japewrapper-buscar-um-registro-pela-pk"
atualizado_em: "2025-11-10T23:38:34.000Z"
---

# Japewrapper - Buscar um registro pela PK

```java Java
/*
	 * @ejb.interface-method tview-type="remote"
	 * @ejb.transaction type="Required"
	*/
	public void findEmpByPK(ServiceContext ctx) throws MGEModelException {

		JapeSession.SessionHandle hnd = null;
		try {
			hnd = JapeSession.open();
			JapeWrapper empresaDAO = JapeFactory.dao(DynamicEntityNames.EMPRESA);
			DynamicVO empresa = empresaDAO.findByPK(BigDecimal.ONE);
			System.out.println(empresa.asString("RAZAOSOCIAL"));
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

# Identificação de transação automática

<!-- java@1-4 -->

Comentário informando a transação automática.

# Inicio da busca pela PK

<!-- java@5 -->



# Instanciamento do objeto SessionHandle

<!-- java@7 -->



# Abertura da sessão com banco de dados

<!-- java@9 -->



# Preparação do DAO

<!-- java@10 -->

Objeto de acesso ao banco de dados , passando o nome da instancia que queremos trabalhar [EMPRESA)]

# Execução do método findByPK

<!-- java@11 -->

é passado o argumento que será buscado no banco de dados [BigDecimal.ONE] , o resultado será guardado no DynamicVO empresa

# Acesso aos campos usando asString

<!-- java@12 -->



# Prevenção de erros - Try catch

<!-- java@8-14 -->



# Finalização

<!-- java@15-18 -->

A sessão é fechada
