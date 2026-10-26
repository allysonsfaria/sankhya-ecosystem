---
id: "30451505691927"
titulo: "Processo financeiro das operações"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30451505691927-Processo-financeiro-das-opera%C3%A7%C3%B5es"
trilha: "Manual do Produto > Financeiro e Patrimônio > Sankhya Fintech > Venda Mais"
atualizado_em: "2026-07-29T13:12:52Z"
rotulos: ["Parceiro", "NF-e", "Movimentação Financeira", "Crédito", "Financeiro", "Parceiro de crédito", "Configurações Venda Mais", "Venda Mais", "Taxa venda Mais", "VERTITRENEG", "Contrato sem antecipação", "Contrato com antecipação"]
---

# Processo financeiro das operações

Quando uma Nota Fiscal Eletrônica (NF-e) tem o crédito aprovado, os títulos financeiros dessa operação são registrados como **A Receber** em nome do **parceiro de crédito**. Dessa forma, ao ser aprovada, a operação passa por um processo de **renegociação**, no qual:

**(2)** Os títulos financeiros originados da NF-e (vinculados ao cliente da venda) tornam-se títulos renegociados:

- o campo **Receita/Despesa** fica vazio;
- o campo **Nro da Renegociação** é preenchido.

**(2)** São gerados novos títulos de destino na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753) seguindo as regras abaixo:

- o campo **Parceiro** é preenchido com o parceiro de crédito (ex: Trademaster) habilitado para essa operação;
- o **Valor Desdobramento** é preenchido com o valor líquido do título original;
- a **Data de Vencimento** é calculada conforme os seguintes tipos de contratos:
  - **com antecipação** = Data da aprovação da operação + Dias de antecipação (Configurações Venda Mais > aba Dados contratuais);
  - **sem antecipação** = Data do vencimento do título original + Dias para recebimento (Configurações Venda Mais > aba Dados contratuais).
- os campos **Tipo de título**, **Natureza**, **Centro de resultado** e **Lançamento**, recebem as informações configuradas na tela Configurações Venda Mais > aba Processos > Configurar rotinas > Financeiro;
- o campo **Histórico** é preenchido com o número da nota (ex: VM-54);
- o campo **Nosso número** é preenchido com um identificador do parceiro de crédito para este título (Ticket Number).
- Os campos da **seção Venda Mais** serão preenchidos da seguinte forma:
  - **Dt Aprovação**: data em que a operação foi aprovada junto ao parceiro de crédito;
  - **Taxa Venda Mais**: é calculada conforme contrato com parceiro de crédito. (cálculo detalhado nos próximos tópicos);
  - **Código da Operação**: número identificador do parceiro de crédito para esta operação;
  - **Venda Mais**: estará marcada, sempre que se tratar de um título aprovado por operações Venda Mais.

![Imagem 1: Venda Mais : estará marcada, sempre que se tratar de um título aprovado por operações Venda Mais.](https://ajuda.sankhya.com.br/hc/article_attachments/30451505687319)

**Importante:** para visualizar os títulos originais (renegociados), é necessário:

- ligar o parâmetro **Visualizar títulos renegociados? - VERTITRENEG** na tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834);
- habilitar a opção **Mostrar renegociados** no botão **Preferências** da tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753).

### Taxa Venda Mais

A taxa Venda Mais é calculada conforme o tipo de contrato firmado com o parceiro de crédito.

#### **(1)** Contrato com antecipação

**Fórmula:**

```
Taxa Venda Mais = [(Dias Operacionais * (Taxa/30)) * Valor do Desdobramento] / 100
```

Onde:

- **Dias Operacionais** = Data de Vencimento - Data de Aprovação
- **Taxa** = Taxa de antecipação configurada na aba **Dados Contratuais** da tela **Configurações Venda Mais**, produto **Venda Mais com Antecipação**

#### **(1)** Contrato sem antecipação

**Fórmula:**

```
Taxa Venda Mais = (Valor do Desdobramento * Taxa Fixa) + [(Dias Operacionais *
(Taxa Variável/30)) * Valor do Desdobramento]
```

Onde:

- **Dias Operacionais** = Data de Vencimento - Data da Operação - 30
- **Taxa Fixa** e **Taxa Variável** = Valor configurado na aba **Dados Contratuais** da tela **Configurações Venda Mais**, produto **Venda Mais sem Antecipação**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/30451505691927-Processo-financeiro-das-opera%C3%A7%C3%B5es#top)
