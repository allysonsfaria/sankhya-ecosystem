---
id: "30545125979159"
titulo: "Acerto de Frete não existe ou não pode ser usado aqui"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30545125979159-Acerto-de-Frete-n%C3%A3o-existe-ou-n%C3%A3o-pode-ser-usado-aqui"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:35:40Z"
rotulos: ["Configuração", "Movimentação Financeira", "Financeiro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Nro compensação/acerto", "Acerto de Frete não existe ou não pode ser usado aqui", "TIPACERTO", "Erro", "Acerto de Frete"]
---

# Acerto de Frete não existe ou não pode ser usado aqui

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/30545128990999) **MENSAGEM:**

Acerto de Frete não existe ou não pode ser usado aqui.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30545125973527)SOLUÇÃO:**

Execute um **SELECT** no **DBExplorer** (Caminho: Configurações » Avançado » DBExplorer), na tabela **TGFFRE**, utilizando os campos **NUACERTO** (Número de compensação/acerto) ou **NUFIN** (Número único).

O número de acerto pode ser encontrado no campo "**Nro compensação/acerto**" da tela **"Movimentação Financeira"**.

![Imagem 3: O número de acerto pode ser encontrado no campo " Nro compensação/acerto " da tela "Movimentação Financeira" .](https://ajuda.sankhya.com.br/hc/article_attachments/30545125974423)

**(1)** **Select a ser realizado:**

**SELECT \* FROM TGFFRE WHERE NUACERTO = XX**

![Imagem 4: O número de acerto pode ser encontrado no campo " Nro compensação/acerto " da tela "Movimentação Financeira" .](https://ajuda.sankhya.com.br/hc/article_attachments/30590851146263)

Identifique o campo **TIPACERTO** e valide em qual tela foi realizado o processo para seguir com a tratativa:

**A=** Adiantamento/empréstimo

**P=** Baixa Parcial

**C=** Compensação (tela compensação financeira)

**G=** Compensação Garantia

**F=** Pagamento de Frete/ Pagamento de Frete por OC

**L=** Acerto com fornecedores

**N=**Antecipação de baixa

**X=** Crédito a compensar (Baixa de movimentação financeira com valor superior ao da receita gerando crédito a compensar)

**D=** Desconto de Títulos / Devolução de Pagamento

**R=** Renegociação de Títulos

**V=** Compensar devolução

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30545125974935)CAUSA:**

Ocorre quando se tenta localizar um **Nro de Acerto** em uma tela onde ele não foi criado.
