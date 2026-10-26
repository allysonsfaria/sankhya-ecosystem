---
id: "360043697273"
titulo: "Venda a prazo bloqueada. Motivo não informado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043697273-Venda-a-prazo-bloqueada-Motivo-n%C3%A3o-informado"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-08-10T19:22:22Z"
rotulos: ["#PUBLIFER", "CORE_E04511", "Configuração", "Parceiro", "Crédito", "Financeiro", "CORE_E04510", "Bloqueio de venda a prazo motivo não informado", "Preencher motivo de bloqueio na tela \"Parceiros\" ou desmarcar bloqueio", "Campo \"Motivo do bloqueio\" não preenchido na aba \"Crédito\"", "Erro", "Artigo atualizado KCS", "Financeiro - KCS"]
---

# Venda a prazo bloqueada. Motivo não informado

**MENSAGEM:**

[CORE\_E04511] Venda a prazo bloqueada. Motivo não informado
[CORE\_E04510] Venda a prazo bloqueada

**SITUAÇÃO:**

O sistema permite bloquear automaticamente vendas a prazo para clientes inadimplentes. Em alguns casos, o campo **"Motivo de bloqueio"** pode não ser preenchido automaticamente, exibindo mensagens genéricas.

**SOLUÇÃO:**

Para correção e configuração, siga os passos abaixo:

### Configuração manual do motivo de bloqueio

Acesse a tela **"Parceiros"** (Configurações >> Cadastros >> Parceiros).

Selecione o parceiro utilizado no lançamento.

Na aba **"Crédito"**, marque o campo **"Bloquear venda a prazo"**.

Preencha o campo **"Motivo de bloqueio"** com a justificativa adequada e salve.

![Imagem 1: Preencha o campo "Motivo de bloqueio" com a justificativa adequada e salve.](https://ajuda.sankhya.com.br/hc/article_attachments/14499109765527)

### Parâmetros complementares

• **"DIASCAR"**: Define a carência para considerar o cliente em atraso.
• **"BLOQMATRIZ"**: Se ativo, o bloqueio da matriz reflete automaticamente em todas as filiais.

**CAUSA:**

Ocorre quando, no cadastro do parceiro, a opção **"Bloquear venda a prazo"** está selecionada e o campo **"Motivo de bloqueio"** não foi preenchido manualmente ou via processo automático de régua de cobrança.
