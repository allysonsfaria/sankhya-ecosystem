---
id: "26410464511255"
titulo: "Compensação manual de crédito não ocorre na venda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26410464511255-Compensa%C3%A7%C3%A3o-manual-de-cr%C3%A9dito-n%C3%A3o-ocorre-na-venda"
trilha: "Melhores Práticas > Vendas"
atualizado_em: "2026-07-22T14:42:14Z"
rotulos: ["Configuração", "Parceiro", "Movimentação Financeira", "Crédito", "Preferências", "Financeiro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "AVISARCREDCLI - Avisar que o cliente possui Crédito", "COMPENSACREDCLI - Compensar crédito do cliente automaticamente", "TIPTITCREDCLI - Tipo de título para compensação de Crédito", "Compensação manual de crédito não ocorre na venda", "Artigo atualizado KCS", "Financeiro - KCS", "Varejo - KCS"]
---

# Compensação manual de crédito não ocorre na venda

O objetivo deste artigo é realizar as corretas configurações e resolver problemas de compensação de crédito do cliente. Utilizando como exemplo uma venda na qual ocorreu devolução, o sistema gera um crédito para o parceiro para que, em uma venda futura, este valor seja compensado.

Algumas configurações são necessárias para o correto funcionamento. Então, se por algum motivo o sistema não sugira o crédito, verifique as seguintes configurações:

**(1)** Verifique os parâmetros na tela **"Preferências"** (Configurações >> Avançado >> Preferências):

**AVISARCREDCLI - Avisar que o cliente possui crédito?: Ligado.**

Com esse parâmetro ligado o sistema exibirá um Pop-up na confirmação da nota, informando o valor que o cliente tem disponível  em crédito a ser abatido e se deseja ou não compensar.

**COMPENSACREDCLI** - **Compensar crédito do cliente automaticamente: Desligado.**

Este parâmetro substitui a funcionalidade do parâmetro AVISARCREDCLI. Assim, caso exista crédito, além de mostrar os avisos de crédito do cliente, ele também fará com que o sistema execute a compensação do crédito de maneira automática, ou seja, sem perguntar ao usuário se ele deseja compensar o crédito. 

**TIPTITCREDCLI - Tipo de título para compensação de crédito**

Neste parâmetro, é definido o tipo de título que a parcela de devolução deverá possuir, para que o crédito seja reconhecido de forma correta pelo sistema.

**(2)** Se o sistema não sugere o crédito, valide as movimentações financeiras na tela **Movimentação Financeira** (Financeiro >> Rotinas >> Movimentação Financeira). Filtre no financeiro por:

**Parceiro:** X

**Provisão:** Não

**Tipo de título (mesmo informado no parâmetro TIPTITCREDCLI):** Y

**Data e Hora da Baixa:** Vazio (Apenas o que ainda não foi baixado)

A pesquisa acima deve retornar apenas despesas, que são equivalentes ao crédito gerado para o parceiro. Caso tenha alguma receita é necessário analisar o porque foi gerada e alterar seu tipo de título para algum que não seja de crédito junto ao responsável financeiro.

**CAUSA:**

Configurações incorretas fazem com que o crédito não seja compensado corretamente, ou que compense de forma incorreta, causando divergência nas movimentações financeiras.
