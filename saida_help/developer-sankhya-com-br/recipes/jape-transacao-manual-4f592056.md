---
id: "https://developer.sankhya.com.br/recipes/jape-transação-manual"
titulo: "Jape - Transação manual"
url: "https://developer.sankhya.com.br/recipes/jape-transação-manual"
atualizado_em: "2025-11-10T23:38:34.000Z"
---

# Jape - Transação manual

```java Java
/**
	 * @ejb.interface-method tview-type="remote"
	 * @ejb.transaction type="NotSupported" 
	*/
	public void servTransManual(ServiceContext ctx) throws MGEModelException {
		JapeSession.SessionHandle hnd = null;
		try {
			hnd = JapeSession.open();
			hnd.setCanTimeout(false);

			hnd.execWithTX(new JapeSession.TXBlock() {
				public void doWithTx() throws Exception {
					chamadaMetodoInsert(param1,param2);
					chamadaMetodoInsert(param1,param2);
					chamadaMetodoInsert(param1,param2);
				}
			});

			hnd.execWithTX(new JapeSession.TXBlock() {
				public void doWithTx() throws Exception {
					try {
						chamadaMetodoDelete(param1,param2);
						chamadaMetodoDelete(param1,param2);
					} catch (Exception e) {
						// TODO: handle exception
						e.printStackTrace();
					}
					
				}
			});

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

# Comentário do método NotSuported

<!-- java@1-4 -->

Este comando explica que o serviço não ira receber uma transação automática. Sem este argumento o sistema abre uma transação automaticamente, isto ocasiona erro ao abrir uma manual, pois não é possível ter 2 transações.

# Inicio do método

<!-- java@5 -->

O método servTransManual é iniciado.

# Objeto de sessão

<!-- java@6 -->



# Abertura da Sessão

<!-- java@8 -->

A sessão hnd é aberta

# Marcação padrão de desativar timeout

<!-- java@9 -->

Por padrão o tempo timeout é de 5minutos, neste código atribuído como false.

# Abertura da transação

<!-- java@11 -->

A transação é aberta, através do [execWithTX,] passando um bloco transacional [new JapeSession.TXBlock()]

# Método doWithTx

<!-- java@12-16 -->

as chamadas de métodos são executadas, 3 inserts

# Try catch

<!-- java@21-27 -->

Permite ou não o hollback para tratamento de erros.

# Finalização

<!-- java@34 -->

A sessão é fechada.
