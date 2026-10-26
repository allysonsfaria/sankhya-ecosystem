---
id: "43548035882775"
titulo: "Erro ao finalizar Ordem de Produção - Estoque insuficiente devido à dependência de PI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43548035882775-Erro-ao-finalizar-Ordem-de-Produ%C3%A7%C3%A3o-Estoque-insuficiente-devido-%C3%A0-depend%C3%AAncia-de-PI"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-10-09T11:33:43Z"
rotulos: ["Artigo criado KCS", "Produção - KCS"]
---

# Erro ao finalizar Ordem de Produção - Estoque insuficiente devido à dependência de PI

**MENSAGEM**

Ao tentar finalizar uma Ordem de Produção, o sistema apresenta a mensagem:

> **Erro**
>
> **Estoque insuficiente.**
> **Empresa: x**
> **Produto: x**
> **Local: x**
> **Controle: x**
> **Validação do** **Estoque:** empresa/local

**SITUAÇÃO**

O erro ocorre ao tentar especificamente **finalizar uma Ordem de Produção que possui dependência de um Produto Intermediário (PI)**, quando a Ordem de Produção responsável pela fabricação desse PI ainda não foi produzida/finalizada.

Durante a análise da OP, na aba **"Dependências"**, é possível identificar uma Ordem de Produção vinculada ao PI utilizado pela OP principal.

Nesse cenário, embora os apontamentos da OP principal já estejam confirmados, o PI ainda não está disponível em estoque, pois a OP responsável por sua fabricação ainda não foi executada ou finalizada.

O **Produto Intermediário (PI)** é um produto acabado proveniente de outra produção e utilizado como matéria-prima na fabricação de um Produto Acabado (PA). Dessa forma, o PI precisa existir antes de ser consumido na produção do PA.

**SOLUÇÃO**

**(1)** Acesse a tela **"Ordens de Produção - NOVA"** e localize a OP que apresenta a mensagem de estoque insuficiente.

**(2)** Acesse a aba **"Dependências"** e verifique as Ordens de Produção vinculadas à OP.

**(3)** Identifique a Ordem de Produção responsável pela fabricação do **Produto Intermediário (PI)** utilizado pela OP principal.

**(4)** Verifique o status da OP do PI. Caso ela ainda não tenha sido iniciada ou finalizada, realize o processo de produção do PI conforme o fluxo produtivo configurado.

**(5)** Após a produção do PI, confirme se a quantidade necessária está disponível no **local/controle de estoque indicado na mensagem**.

**(6)** Com o PI disponível em estoque, retorne à OP principal e tente novamente realizar a finalização.

**CAUSA**

A mensagem ocorre porque a Ordem de Produção que está sendo finalizada possui uma necessidade de consumo de **Produto Intermediário (PI)**, porém o PI ainda não está disponível na quantidade necessária no estoque.
