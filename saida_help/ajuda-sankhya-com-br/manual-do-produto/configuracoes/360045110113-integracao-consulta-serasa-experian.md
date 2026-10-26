---
id: "360045110113"
titulo: "Integração Consulta SERASA EXPERIAN"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110113-Integra%C3%A7%C3%A3o-Consulta-SERASA-EXPERIAN"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:56:19Z"
rotulos: ["Configuração", "Consulta", "Parceiro", "Crédito", "Integração", "TOP", "Experian", "Serasa", "Integração Consulta SERASA EXPERIAN manual", "Financeiro", "Integração SERASA Experian: Configuração e Consultas"]
---

# Integração Consulta SERASA EXPERIAN

**Importante:** as configurações aqui descritas estarão disponibilizadas, caso a empresa possua o opcional **30720 - CONSULTA SERASA/W**.

O objetivo dessa integração é permitir que a empresa realize consultas no [SERASA EXPERIAN](https://www.serasaexperian.com.br/), utilizando os serviços:

- Relato Analítico (consulta por CNPJ);
- Credit Bureau (consulta por CPF).

Tais consultas irão ocorrer através do Sankhya-Om, que irá registrar no banco de dados todas as pesquisas realizadas para àquele parceiro e alertar os vendedores no momento da negociação, caso a consulta ao Serasa já esteja vencida.

É possível utilizar a consulta no [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros) e [Prospects](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612814-Prospects), independente da realização de movimentações de pedido ou venda.

Esta integração ocorre com base em algumas configurações essenciais no sistema. Vejamos:

[Configuração Serasa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110113-Integra%C3%A7%C3%A3o-Consulta-SERASA-EXPERIAN#configuraoserasa)                                                          [Análise de Risco Serasa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110113-Integra%C3%A7%C3%A3o-Consulta-SERASA-EXPERIAN#anlisederisco)

[Cadastro de Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110113-Integra%C3%A7%C3%A3o-Consulta-SERASA-EXPERIAN#cadastrodetiposdeoperao-top)                           [Liberação de Limites](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110113-Integra%C3%A7%C3%A3o-Consulta-SERASA-EXPERIAN#liberaodelimites)

## Configuração Serasa

Através da tela Configuração Serasa, realizam-se as configurações iniciais que irão possibilitar a consulta ao [Serasa Experian](https://www.serasaexperian.com.br/). Basicamente, tem-se as marcações que definem quais consultas serão efetuadas, o Usuário e sua respectiva Senha, e se tal consulta será realizada em Ambiente de Homologação.

**Importante:** é necessário que o usuário e a senha sejam obtidos diretamente com a Serasa. Sendo que, o usuário solicitado deverá ser específico para a integração via STRING HTTPS.

![Imagem 1: Importante: é necessário que o usuário e a senha sejam obtidos diretamente com a Serasa. Sendo que, o usuário…](https://ajuda.sankhya.com.br/hc/article_attachments/9777858731543)

Os detalhes acerca desta tela, podem ser visualizados por meio do link [Configuração Serasa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602434-Configura%C3%A7%C3%A3o-Serasa).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110113-Integra%C3%A7%C3%A3o-Consulta-SERASA-EXPERIAN#top)

## Análise de Risco Serasa

A tela Análise de Risco Serasa é responsável pela realização da consulta da situação do parceiro junto ao Serasa. Além disso, ela permite atualizações cadastrais em [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros) e [Prospects](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612814-Prospects), bloqueios de vendas a prazo, redefinições de limites de crédito, dentre outras funcionalidades.

![Imagem 2: A tela Análise de Risco Serasa é responsável pela realização da consulta da situação do parceiro junto ao Serasa. Além…](https://ajuda.sankhya.com.br/hc/article_attachments/9777891703191)

Os detalhes acerca desta tela, podem ser visualizados por meio do link [Análise de Risco Serasa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115753-An%C3%A1lise-de-Risco).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110113-Integra%C3%A7%C3%A3o-Consulta-SERASA-EXPERIAN#top)

## Cadastro de Tipos de Operação - TOP

No cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), na aba [Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abafinanceiro), tem-se a marcação **"Exige análise de crédito"**:

![Imagem 3: No cadastro de Tipos de Operação - TOP , na aba Financeiro , tem-se a marcação "Exige análise de crédito" :](https://ajuda.sankhya.com.br/hc/article_attachments/9778044105879)

Se esta marcação estiver realizada, no lançamento de uma venda em que esta TOP for utilizada, será necessário que uma consulta junto ao [Serasa Experian](https://www.serasaexperian.com.br/) seja efetuada para o [Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros) em questão, antes da concretização da negociação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110113-Integra%C3%A7%C3%A3o-Consulta-SERASA-EXPERIAN#top)

## Liberação de Limites

Como mencionado no tópico anterior, ao trabalhar-se com um [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) com a marcação Exige análise de crédito realizada, será obrigatória a consulta ao Serasa Experian a respeito dos dados do Parceiro, Prospect ou CPF/CNPJ.

Somando-se a isso, tem-se dois casos acerca dessa rotina, em que será necessário proceder com a Liberação de Limites para continuidade no processo (na tela [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), deve-se configurar um Usuário Liberador e por meio do Botão Outras Opções..., Limites para Liberação, incluir o evento [77 - Análise de crédito expirada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites#77-anlisedecrditoexpirada) para tal usuário). Observe:

**1º caso:** Ao proceder com uma venda, pode ser que a Data da consulta realizada em outro momento para o parceiro junto ao Serasa, tenha expirado (Data de Expiração menor que a Data de Negociação), sendo necessário que um Usuário Liberador autorize a continuidade da nova negociação, por meio da [Liberação de Limites](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites). Esta solicitação de liberação irá acontecer na tentativa de Confirmação da nota de venda.

**2º caso:** Na realização de uma venda, pode ser que para o Parceiro em questão, não tenha-se efetuado nenhuma consulta junto ao Serasa; para seguimento na venda para um Parceiro nesta situação, também será necessário que um Usuário Liberador permita a operação através da liberação do evento [77 - Análise de crédito expirada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites#77-anlisedecrditoexpirada). Assim como a situação anterior, a solicitação de liberação irá ocorrer quando na Confirmação da nota de venda.

Em ambos os casos apresentados, quando o Usuário Liberador der o seu parecer quanto à solicitação, será possível dar sequência ao processo de venda, que pode ser a Confirmação da nota e efetivação da negociação (Usuário Liberador autorizou a venda), ou anulação da venda (Usuário Liberador não permitiu a negociação).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110113-Integra%C3%A7%C3%A3o-Consulta-SERASA-EXPERIAN#top)
