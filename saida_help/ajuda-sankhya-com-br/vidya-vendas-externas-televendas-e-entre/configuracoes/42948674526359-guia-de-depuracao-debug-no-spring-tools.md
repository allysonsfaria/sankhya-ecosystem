---
id: "42948674526359"
titulo: "Guia de Depuração (DEBUG) no Spring Tools"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42948674526359-Guia-de-Depura%C3%A7%C3%A3o-DEBUG-no-Spring-Tools"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Configurações"
atualizado_em: "2026-08-24T15:40:06Z"
rotulos: ["sync_hc", "vidya", "sync_hash_e86822e16410", "vidya_525803"]
---

# Guia de Depuração (DEBUG) no Spring Tools

**VIDEO DA APRESENTAÇÃO: <https://drive.google.com/file/d/16ayrLtLIzL3F2yEL6x-Ha6k4IEBctcyz/view?usp=drive_link>**

A depuração (“debug”) é um processo essencial para identificar e corrigir erros em sistemas desenvolvidos com **Spring Tools**. Durante a reunião, discutimos diferentes formas de depurar erros em pedidos, banco de dados e requisições no Spring. Este guia resume as principais abordagens apresentadas.

## Identificação de Erros em Pedidos

### 1) Erro de atributo incorreto

- Um problema comum é quando um atributo não tem o formato esperado.
- Exemplo: O **código local de origem** enviado não está no formato de texto esperado.
- Solução: Ativar **DEBUG FRONT** para capturar o JSON enviado pelo frontend.

### 2) Logs de pedidos

- Ativar **log de pedidos** para visualizar quais informações estão sendo enviadas ao backend.
- Se a falha ocorre no backend, utilizar **DEBUG SK** para analisar as requisições enviadas ao sistema.

## Depuração de Queries (SQL)

### 1) Quando utilizar DEBUG CARY?

- Quando for necessário validar uma consulta SQL.
- Se os dados não estão aparecendo no sistema, ativar **DEBUG CARY** para visualizar a consulta executada no banco.

### 2) Localização de erros em consultas SQL

- Se a query retorna **zero resultados**, verificar os **filtros aplicados**.
- Para isolar o problema, testar a consulta removendo filtros até encontrar qual impede o retorno dos dados.
- Consultas podem ser testadas diretamente no banco usando ferramentas como **SQL Formatter** para melhorar a legibilidade.

## Erros em Resultados (ResultSet)

### 1) Quando utilizar DEBUG RESULT SET?

- Quando os dados estão corrompidos ou mal formatados.
- O **DEBUG RESULT SET** imprime cada campo e seu respectivo valor, ajudando a identificar informações inconsistentes.
- Exemplo: Se um campo **Complemento** está retornando valores inesperados, ativar o debug pode mostrar o erro diretamente.

## Depuração de Requisições HTTP

### 1) Quando utilizar DEBUG HEADER?

- Quando há problemas no cabeçalho da requisição.
- Exemplo: A requisição demora indefinidamente ou retorna resposta inesperada.
- O **DEBUG HEADER** permite ver a última operação antes da falha.

### 2) Depuração de login e sessão

- Se o problema está relacionado à sessão do usuário, ativar **DEBUG LOGIN** pode ajudar a verificar o momento exato da autenticação.
- Em sistemas onde múltiplas sessões podem ficar presas, esse debug permite encontrar e corrigir o problema.

## Testes e Simulações

### 1) Utilização do Postman para testar requisições

- O Postman permite enviar requisições manualmente para testar diferentes cenários.
- Para pedidos enviados pelo aplicativo, capturar o JSON da requisição com **DEBUG FRONT** e testá-lo no Postman.

### 2) Logs no AWS

- Em servidores AWS, é possível obter logs de execução para analisar erros que ocorreram diretamente na infraestrutura.
- A recomendação é ativar logs apenas temporariamente, pois podem gerar um grande volume de dados.

## Visualização de Logs no Sistema

### 1) Logs de pedidos no banco

- A tela **Log de Pedidos** permite visualizar todas as requisições enviadas ao sistema.
- Se um pedido desapareceu ou um item não foi salvo corretamente, essa ferramenta ajuda a localizar onde ocorreu o problema.
- O código do pedido pode ser decodificado via **Base64** para facilitar a análise.

## Conclusão

Os diferentes tipos de debug permitem diagnosticar e resolver problemas de forma eficiente. Recomenda-se:

1. **Ativar logs específicos** dependendo do erro encontrado.
2. **Testar requisições manualmente** utilizando Postman quando necessário.
3. **Analisar consultas SQL** para detectar filtros incorretos ou erros de sintaxe.
4. **Utilizar logs do sistema** para obter mais informações sobre erros ocorridos em produção.

Seguindo esses passos, a depuração no Spring Tools se torna mais eficiente e estruturada.
