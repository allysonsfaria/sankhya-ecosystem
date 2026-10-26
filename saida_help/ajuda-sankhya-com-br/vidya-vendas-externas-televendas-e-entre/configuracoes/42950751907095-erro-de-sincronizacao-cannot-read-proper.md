---
id: "42950751907095"
titulo: "Erro de Sincronização — \"Cannot read property 'user' of undefined\" / \"Erro na requisição\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950751907095-Erro-de-Sincroniza%C3%A7%C3%A3o-Cannot-read-property-user-of-undefined-Erro-na-requisi%C3%A7%C3%A3o"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Configurações"
atualizado_em: "2026-08-24T17:03:15Z"
rotulos: ["sync_hc", "vidya", "vidya_600119", "sync_hash_1b377f6f3092"]
---

# Erro de Sincronização — "Cannot read property 'user' of undefined" / "Erro na requisição"

## 1. Sintoma

Ao tentar sincronizar dados no aplicativo, o usuário perde a conexão com o ERP Sankhya durante a sincronização e recebe a mensagem **"Dados não sincronizados! Perdemos conexão com o ERP Sankhya durante a sincronização de dados. Por favor, sincronize novamente."**

Ao abrir os **Logs de sincronização**, aparecem erros como:

- **Produtos** → `Error: Erro na requisição`
- **Preços** → `Error: Cannot read property 'user' of undefined`
- **Cabeçalho** → `Error: Cannot read property 'user' of undefined`
- **Parceiros** → sem log de erro específico (`--`), pois o processo é interrompido antes de chegar nessa etapa

  ![Imagem 1: Parceiros → sem log de erro específico ( -- ), pois o processo é interrompido antes de chegar nessa etapa](https://ajuda.sankhya.com.br/hc/article_attachments/42957638970391)

## 2. Causa

Esse erro ocorre quando o **tipo de banco de dados cadastrado para o cliente está invertido** em relação ao banco real do ambiente dele. Ou seja:

- O cliente utiliza banco **SQL Server**, mas foi cadastrado no backend unificado como **Oracle**; **ou**
- O cliente utiliza banco **Oracle**, mas foi cadastrado no backend unificado como **SQL Server**.

Essa inconsistência normalmente acontece em dois pontos:

1. No **arquivo `.war`** gerado no Spring Tools para o cliente, quando ele é gerado com o banco errado; ou
2. No **cadastro do cliente no backend unificado**, quando alguém seleciona o tipo de banco incorreto na hora de cadastrar.

Como o app tenta se comunicar com o backend usando as chamadas/queries do banco configurado (que não corresponde ao banco real do cliente), as requisições falham — e é isso que gera os erros `Erro na requisição` e `Cannot read property 'user' of undefined` durante a sincronização de Produtos, Preços e Cabeçalho.

## 3. Diagnóstico

Antes de aplicar a correção, confirme a causa:

1. Verifique qual é o banco de dados real do cliente (Oracle ou SQL Server) — pode confirmar com o time responsável pelo ambiente do cliente ou pela string de conexão usada.
2. Verifique como o cliente está cadastrado hoje:
   - No **backend unificado**, checar o tipo de banco selecionado no cadastro do cliente.
   - Ou, se o acesso foi feito via `.war` gerado manualmente no Spring Tools, checar com qual configuração de banco esse `.war` foi gerado.
3. Se o tipo cadastrado for diferente do banco real do cliente, essa é a causa do erro.

## 4. Solução

A correção consiste em **recadastrar/regerar com o banco correto**:

- Se o problema estiver no **cadastro do backend unificado**: corrigir o cadastro do cliente, ajustando o campo de tipo de banco para o valor correto (Oracle ou SQL, conforme o ambiente real do cliente).
- Se o problema estiver no **arquivo `.war`**: gerar um **novo `.war`** no Spring Tools, desta vez com a configuração de banco correta (Oracle ou SQL Server, conforme o ambiente real do cliente), e substituir o arquivo anterior.

Após a correção, orientar o usuário a sincronizar novamente o aplicativo.

## 5. Prevenção

- Ao cadastrar um novo cliente no backend unificado, **sempre confirmar previamente** com o time de implantação/infra qual é o banco de dados real do ambiente (Oracle ou SQL Server) antes de salvar o cadastro.
- Ao gerar um `.war` manualmente no Spring Tools, conferir a configuração de banco selecionada antes de disponibilizar o arquivo, evitando gerar com o tipo trocado.
- Caso o erro apareça em um cliente já em produção, esse é o primeiro ponto a ser checado, antes de investigar outras causas (rede, credenciais, etc.), já que o padrão de erro (`Erro na requisição` + `Cannot read property 'user' of undefined` nas etapas de Produtos/Preços/Cabeçalho) é bastante característico desse cenário.
