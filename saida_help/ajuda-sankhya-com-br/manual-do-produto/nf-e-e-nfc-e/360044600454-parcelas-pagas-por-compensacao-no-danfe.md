---
id: "360044600454"
titulo: "Parcelas pagas por compensação no DANFE"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600454-Parcelas-pagas-por-compensa%C3%A7%C3%A3o-no-DANFE"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Documentos Fiscais Eletrônicos > NF-e e NFC-e"
atualizado_em: "2026-09-15T16:51:36Z"
rotulos: ["Configuração", "Impressão", "Movimentação Financeira", "Crédito", "DANFE", "Compensação", "Parcelas pagas por compensação no DANFE manual", "Financeiro", "Indicação de Parcelas Pagas no DANFE"]
---

# Parcelas pagas por compensação no DANFE

Nosso sistema conta com um recurso que permite a impressão do Danfe, e neste consta a verificação se o título está baixado e se o tipo de título utilizado em seu lançamento é compensação de crédito. Se estes casos forem atendidos, no final da descrição da seção **"Fatura/Duplicata"** no Danfe, será apresentada a palavra **"[pago]"**.

Para que esta impressão ocorra, é necessário que o processo de geração do Danfe de cada empresa seja analisado, pois é preciso que o parâmetro **"Imprimir faturas no DANFE pelo xml - FINANCEXMLDANFE"** esteja desativado. Além disso, deve-se realizar a ativação do parâmetro **"Destacar financeiro pago por compensação no danfe? - DESFINPGCOMPDNF"**.

Consideremos abaixo, o processo no sistema envolvido neste procedimento:

- Na tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) atente-se para a configuração dos seguintes parâmetros:

1. Avisar que o cliente possui Crédito? - AVISARCREDCLI: **Ativado**
2. Compensar crédito do cliente automaticamente - COMPENSACREDCLI: **Ativado**
3. Destacar financeiro pago por compensação no danfe? - DESFINPGCOMPDNF: **Ativado**
4. Top Baixa de Despesa de Compensação de Crédito - TOPBAIDESPCOMP: **Informado**
5. Top Baixa de Receita de Compensação de Crédito - TOPBAIRECCOMP: **Informado**
6. Tipo de título para compensação de Crédito - TIPTITCREDCLI: **Informado**
7. Avisar que o cliente possui Crédito? - AVISARCREDCLI: **Ativado**
8. Imprimir faturas no DANFE pelo xml - FINANCEXMLDANFE: **Desativado**

- Na tela [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o) deve-se possuir um tipo de negociação adequado que atenda ao processo de geração de Crédito para o cliente.

![Imagem 1: Na tela Tipos de Negociação deve-se possuir um tipo de negociação adequado que atenda ao processo de geração de Crédito…](https://ajuda.sankhya.com.br/hc/article_attachments/8444711105431)

- É necessário que o cliente possua um crédito para ele lançado. Por exemplo, o cliente realizou uma devolução e ficou com um crédito a ser compensado quando efetuar uma nova compra.
- Ao efetuar a venda para o cliente que possui o crédito a ser compensado, o sistema irá fazê-lo no financeiro da nota, baixando o título e modificando o Tipo de Título para a informação salva no parâmetro **"Tipo de título para compensação de Crédito - TIPTITCREDCLI"**.

Consideremos o exemplo de um Danfe impresso contendo a informação **"[pago]"**:

![Imagem 2: Consideremos o exemplo de um Danfe impresso contendo a informação "(pago)" :](https://ajuda.sankhya.com.br/hc/article_attachments/8444531261207)

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600454-Parcelas-pagas-por-compensa%C3%A7%C3%A3o-no-DANFE#top)
