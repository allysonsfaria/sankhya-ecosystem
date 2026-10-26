---
id: "35317804809879"
titulo: "CORE_E00234 - O sistema não está validando a numeração repetida em um novo lançamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35317804809879-CORE-E00234-O-sistema-n%C3%A3o-est%C3%A1-validando-a-numera%C3%A7%C3%A3o-repetida-em-um-novo-lan%C3%A7amento"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T14:25:26Z"
rotulos: ["Configuração", "Parceiro", "Movimentação Financeira", "TOP", "Erro", "CORE_E00234", "Numeração já utilizada em outro lançamento", "Valida Numeração por", "PROIBIR", "VALNUMNOTACONF"]
---

# CORE_E00234 - O sistema não está validando a numeração repetida em um novo lançamento

**MENSAGEM:**

[CORE\_E00234] Numeração já utilizada em outro lançamento.

**SITUAÇÃO:**

Ao realizar lançamento em que a numeração já tenha sido utilizada em outro lançamento e a **"TOP"** está configurada para bloquear numeração repetida, com o campo **"Valida Numeração por"** definido em alguma opção **"PROIBIR"**.

**SOLUÇÃO:**

**(1)** Verifique se a opção selecionada no campo **"Valida Numeração por"** corresponde ao tipo de numeração da **"TOP"**. Por exemplo, se utiliza Empresa/Série, selecione uma opção que também valide a série. Caso a configuração não contemple a série, poderá ocorrer lançamento para o mesmo parceiro com o mesmo número se a série for diferente.

![Imagem 1: (1) Verifique se a opção selecionada no campo "Valida Numeração por" corresponde ao tipo de numeração da "TOP" . Por…](https://ajuda.sankhya.com.br/hc/article_attachments/35317793411223)

**(2)** Se a **"TOP"** estiver configurada com numeração automática (e se for esse o caso), além de configurar o campo **"Valida Numeração por"**, habilite o parâmetro **VALNUMNOTACONF**.

**CAUSA:**

A mensagem ocorre quando há mais de um lançamento com a mesma numeração, devido a:

- O campo **"Valida Numeração por"** da **"TOP"** não está configurado.
- O campo **"Valida Numeração por"** está configurado com uma opção que apenas faz a validação, mas não bloqueia.
- A numeração da **"TOP"** é automática.
