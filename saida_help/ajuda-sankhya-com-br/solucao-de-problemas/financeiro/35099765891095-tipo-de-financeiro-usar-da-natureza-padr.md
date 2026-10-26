---
id: "35099765891095"
titulo: "Tipo de Financeiro \"Usar da Natureza Padrão\" não está sendo respeitado no Financeiro. Saiba como resolver"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35099765891095-Tipo-de-Financeiro-Usar-da-Natureza-Padr%C3%A3o-n%C3%A3o-est%C3%A1-sendo-respeitado-no-Financeiro-Saiba-como-resolver"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:26:01Z"
rotulos: ["Configuração", "Parcelas", "Tipo de Negociação", "TOP", "Preferências", "Financeiro", "Natureza", "Tipo de Financeiro \"Usar da Natureza Padrão\" não está sendo respeitado no Financeiro", "não está sendo respeitado no Financeiro", "Tipo de Financeiro = \"Usar da Natureza Padrão\"", "Tipo de Financeiro \"Usar da Natureza Padrão\""]
---

# Tipo de Financeiro "Usar da Natureza Padrão" não está sendo respeitado no Financeiro. Saiba como resolver

**SITUAÇÃO:**

Ao configurar um **Tipo de Negociação** para que gere uma linha no Financeiro como **Despesa**, sendo que a **TOP** é de **Receita** (ou vice-versa), utilizando a opção de **Tipo de Financeiro = "Usar da Natureza Padrão"** na aba **"Parcelas"** do Tipo de Negociação**,** o lançamento continua sendo gerado incorretamente, sem respeitar a configuração esperada.

![Imagem 1: Ao configurar um Tipo de Negociação para que gere uma linha no Financeiro como Despesa , sendo que a TOP é de Receita…](https://ajuda.sankhya.com.br/hc/article_attachments/35099765882519)

**SOLUÇÃO:**

**(1)** Acesse a tela **Preferências** (Caminho: Configurações » Avançado » Preferências)

**(2)** Localize e verifique se o parâmetro **USACRPROJNATCAB** está habilitado.

![Imagem 2: (2) Localize e verifique se o parâmetro USACRPROJNATCAB está habilitado.](https://ajuda.sankhya.com.br/hc/article_attachments/35099734858775)

**(3)** Ajuste conforme a necessidade do processo:

- **Habilitado:** O Financeiro seguirá sempre a configuração do cabeçalho da nota.
- **Desabilitado:** O Financeiro respeitará a natureza definida individualmente na Aba Parcelas do Tipo de Negociação.

**CAUSA:**

Esse comportamento ocorre devido ao parâmetro:

**"Usar o mesmo CR/Projeto/Natureza da nota? - USACRPROJNATCAB"**

Quando **habilitado**, ele força que os campos **Projeto, Natureza e Centro de Resultado** do Financeiro sejam sempre iguais ao cabeçalho da nota.

Se houver qualquer alteração nesses campos no cabeçalho, o Financeiro será automaticamente atualizado.

Quando **desabilitado**, o sistema não altera esses dados no Financeiro, mesmo que sejam modificados no cabeçalho.

Assim, mesmo que uma natureza específica seja informada diretamente no Financeiro, o sistema sobrescreve essa informação com a **Natureza do cabeçalho da nota**, gerando o título incorretamente (sem considerar a informação **Tipo de Natureza** do cadastro de Naturezas de Receitas e Despesas).
