---
id: "360044606394"
titulo: "Configuração da Fatura do Cartão"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606394-Configura%C3%A7%C3%A3o-da-Fatura-do-Cart%C3%A3o"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:39:23Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Parceiro", "Movimentação Financeira", "Rotina Específica de Parceiro", "Financeiro", "Natureza", "br.com.sankhya.configuracao.job.fatura.cartao", "Configuração da Fatura do Cartão manual", "Configuração de juros e multa", "Processo de baixa de título", "Geração da fatura do cartão", "Cartão de Crédito"]
---

# Configuração da Fatura do Cartão

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312297277591) Módulo: Financeiro > Rotinas > Operações de Crédito
```

---

**Importante:** esta rotina é exclusiva de um Parceiro e habilitada por parâmetro específico.

Nesta tela, temos alguns parâmetros para a configuração do processo de faturamento dos financeiros de cartão:

[Seção Configuração para o título de juros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606394-Configura%C3%A7%C3%A3o-da-Fatura-do-Cart%C3%A3o#se%C3%A7%C3%A3oconfigura%C3%A7%C3%A3oparaot%C3%ADtulodejuros)        [Seção Configuração para o título de multa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606394-Configura%C3%A7%C3%A3o-da-Fatura-do-Cart%C3%A3o#se%C3%A7%C3%A3oconfigura%C3%A7%C3%A3oparaot%C3%ADtulodemulta)

[Seção Configuração para a fatura do cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606394-Configura%C3%A7%C3%A3o-da-Fatura-do-Cart%C3%A3o#se%C3%A7%C3%A3oconfigura%C3%A7%C3%A3oparaafaturadocart%C3%A3o)    [Seção Configuração para a baixa de título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606394-Configura%C3%A7%C3%A3o-da-Fatura-do-Cart%C3%A3o#se%C3%A7%C3%A3oconfigura%C3%A7%C3%A3oparaabaixadet%C3%ADtulo)

![Imagem 2: Seção Configuração para a fatura do cartão Seção Configuração para a baixa de título](https://ajuda.sankhya.com.br/hc/article_attachments/360086777614)

## Seção Configuração para o título de juros

Quando um título for pago com atraso, ou restar algum valor para faturar no próximo mês, será calculado juros diários e o total do juro será lançado como um financeiro receita com o valor do desdobramento igual ao valor calculado. Por isso, é necessário indicar, para cadastrar este título, os seguintes parâmetros:

- Percentual de juro ao dia para o cartão;
- Natureza;
- Centro de resultado;
- Projeto;
- Tipo de título;
- Tipo de Operação deste título.

**Nota:** insira no parâmetro **"Natureza para juro do cartão - NATJUROCART"**, a natureza responsável para calcular os juros do cartão nesta tela.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606394-Configura%C3%A7%C3%A3o-da-Fatura-do-Cart%C3%A3o#top)

## Seção Configuração para o título de multa

Quando um título for pago em atraso, ou em dia com um valor menor que o valor mínimo, será calculado a multa que será lançada como um financeiro receita com o valor do desdobramento igual ao valor calculado. Por isso, é necessário indicar, para cadastrar este título, os seguintes parâmetros:

- Percentual de multa do cartão de crédito,
- Natureza,
- Centro de resultado,
- Projeto,
- Tipo de título,
- Tipo de Operação deste título e
- Conta bancária para geração do boleto.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606394-Configura%C3%A7%C3%A3o-da-Fatura-do-Cart%C3%A3o#top)

## Seção Configuração para a fatura do cartão

Para gerar a fatura, que será a renegociação dos títulos encontrados e/ou gerados (juro e multa), você deve possuir os valores padrão para serem inserido com os seguintes parâmetros:

- Natureza;
- Centro de Resultado;
- Projeto;
- Tipo de título e;
- Tipo de operação deste título.

Além dos parâmetros descritos acima o sistema necessitará:

No campo **"Horário para execução da fatura"**, preencha a hora que diariamente será executado o JOB, que gera as faturas automaticamente. Este procedimento é diário.

**Qtde de dias para o corte antes do vcto:** O dia de corte é a data do sistema subtraindo os dias configurado neste parâmetro, ou seja, se dia 20 você for gerar as faturas e o parâmetro estiver configurado para 15 dias, o sistema chegará na data de corte 5 (20 – 15) e selecionará todos os parceiros que possuem vencimento na data de corte dia 05.

**Percentual de pagamento mínimo do cartão:** O percentual de corte é utilizado para calcular se o sistema deve cobrar multa do parceiro, ou seja, se o parceiro pagar em atraso um valor menor do que o percentual de corte, o sistema deverá cobrar multa (com o percentual configurado); caso pague um valor entre o mínimo e o valor total da fatura, não deverá cobrar multa do parceiro.

O campo **"Modelo do relatório formatado da fatura do cartão"**deve ser preenchido com o código criado nos Relatórios Formatados que usará o iReport, através dos arquivos anexados, para gerar a fatura do cartão.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606394-Configura%C3%A7%C3%A3o-da-Fatura-do-Cart%C3%A3o#top)

## Seção Configuração para a baixa de título

A fatura pode ser gerada com valor igual a zero, pois pode existir crédito à compensar (um valor de despesa que deve ser deduzido do valor encontrado, pois o cliente pagou antecipadamente) e, se o valor da fatura for igual ao crédito à compensar, o valor da fatura ficará igual a zero. Neste caso, o financeiro fatura igual a zero, podendo ser baixado pela rotina de geração da fatura e gerando o movimento bancário, sendo necessário alguns valores padrão, respeitando o parâmetro **"Aceita valor de baixa igual a zero -VLRBAIXAZERO"**. Se o parâmetro estiver ligado, a baixa será feita; se estiver desligado, a baixa não será feita. Para a baixa ser feita, é necessário a configuração dos seguintes parâmetros:

- Tipo de operação;
- Conta bancária;
- Lançamento e;
- Histórico.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606394-Configura%C3%A7%C3%A3o-da-Fatura-do-Cart%C3%A3o#top)
