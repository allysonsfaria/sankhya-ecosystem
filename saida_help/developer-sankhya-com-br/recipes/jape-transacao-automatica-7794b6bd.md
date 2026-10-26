---
id: "https://developer.sankhya.com.br/recipes/jape-transação-automática"
titulo: "Jape - Transação automática"
url: "https://developer.sankhya.com.br/recipes/jape-transação-automática"
atualizado_em: "2025-11-10T23:38:34.000Z"
---

# Jape - Transação automática

```java Java
/*
	 * @ejb.interface-method tview-type="remote"
	 * @ejb.transaction type="Required"
	*/
	public void servTransAutomatica(ServiceContext ctx) throws MGEModelException {
		JapeSession.SessionHandle hnd = null;
		try {
			hnd = JapeSession.open();
			JapeWrapper servidorDAO = JapeFactory.dao(DynamicEntityNames.SERVIDOR_SMTP);

			servidorDAO.create()
			.set("CODSMTP", BigDecimal.valueOf(1))
			.set("SERVIDOR", "smtp.gmail.com")
			.set("REMETENTE", "time@gmail.com")
			.set("PORTA", BigDecimal.valueOf(36))
			.save();

			servidorDAO.create()
			.set("CODSMTP", BigDecimal.valueOf(2))
			.set("SERVIDOR", "smtp.gmail.com")
			.set("REMETENTE", "equipe@gmail.com")
			.set("PORTA", BigDecimal.valueOf(587))
			.save();

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

# Comentário transação automática (default)

<!-- java@1-4 -->

Comentário informando a transação automática.

# Abertura da sessão

<!-- java@5-6 -->



# Abertura do dao

<!-- java@9 -->

Abertura do DAO para o SERVIDOR_SMTP

# Inserção de campos na tabela

<!-- java@11-23 -->

Os dados são atribuídos e salvos em 2 blocos.

# Prevenção de erros

<!-- java@26 -->

Se houver algum erro o mesmo é apresentado ao usuário.

# Fim da transação

<!-- java@27-30 -->
