---
id: "360045118873"
titulo: "Filtro para cálculo CIP (Financeiros)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118873-Filtro-para-c%C3%A1lculo-CIP-Financeiros"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:54:58Z"
rotulos: ["AJUDA DO SKW", "manual", "Custos", "Configuração", "Centro de Resultado", "PERMITCRFILTCIP", "Financeiros", "CIP", "Financeiro", "Natureza", "Centro Resultado", "Construtor expressão", "Converter expressão", "PERMITNTFILTCIP", "Tarifas", "Filtro para cálculo CIP (Financeiros)", "br.com.sankhya.mgecom.cad.filtrocalccustofinanceiro", "Filtro para cálculo CIP (Financeiros) manual", "Tarifas CIP custos indiretos", "Apropriação de Custos Indiretos Movimentação Financeira", "Construtor expressão reutilização"]
---

# Filtro para cálculo CIP (Financeiros)

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312812138007) Módulo: Produção > Cadastro
```

---

Nesta tela serão cadastrados os pontos (Financeiros) que serão considerados no momento da realização do cálculo das devidas Tarifas; estes pontos podem ser adicionados à tela, por meio da criação de um filtro personalizado (aba **"Filtro"** - botão **"Construtor expressão"**), onde nos casos em que a empresa já trabalhava com esta rotina no MGE e já possuía um filtro cadastrado, este mesmo filtro poderá ser utilizado no Sankhya Om através do botão localizado no lado superior direito da aba.

![Imagem 2: Nesta tela serão cadastrados os pontos ( Financeiros ) que serão considerados no momento da realização do cálculo das…](https://ajuda.sankhya.com.br/hc/article_attachments/360099954374)

As indústrias possuem alguns custos indiretos que são registrados partindo-se de [Tarifas CIP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611074), tais como, energia elétrica e/ou materiais de consumo. Ao final da produção, os custos gerados por estes aspectos são rateados entre o que foi produzido. Como alguns produtos (Produtos Acabados) precisam absorver uma parte maior do custo destes itens, se comparado à outros produtos acabados, informa-se no campo **"Perc. do valor a ser usado no custo"** o percentual do valor a ser utilizado no cálculo do custo de uma Tarifa CIP. A informação inserida neste campo, é comumente utilizada em casos onde duas ou mais tarifas possuem o mesmo filtro para cálculo de seu custo, porém, cada uma deve absorver uma determinada quantia desse valor.

Na tela teremos a marcação **"Apropriação de Custos Indiretos de Produção (CIP)"**, que quando selecionada, irá considerar as regras de rateio cadastradas na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira). Ao desmarcar este, o cálculo dos custos indiretos de produção na tela [Apropriação de Custos Indiretos de Produção (CIP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611094-Apropria%C3%A7%C3%A3o-de-Custos-Indiretos-de-Produ%C3%A7%C3%A3o-CIP-) não considera as regras de rateio feitas na tela Movimentação Financeira.

Além da aba Filtro, a tela conta com as abas **"Centro Resultado"**, **"Natureza"** e **"Tarifas"** que são de simples e semelhante preenchimento; nelas podem ser inseridos os [Centros de Resultado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606754), as [Naturezas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774) e [Tarifas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611074) que serão utilizadas para construção do Filtro em questão e consequentemente, serão consideradas no cálculo.

**Observação:** para que não sejam considerados no Cálculo da tarifa CIP os lançamentos provisionados, informe na aba **"Filtro"** a expressão **"ViewFinanceiro.PROVISAO = 'N'"**.

![Imagem 3: Informações adicionais:](https://ajuda.sankhya.com.br/hc/article_attachments/16649249772823)**Informações adicionais:**

- Caso o parâmetro **"Permite vincular o CR em vários Filtros CIP - PERMITCRFILTCIP"** seja ativado, será possível realizar a inserção do mesmo Centro de Resultado em mais de um Filtro para cálculo CIP;
- De forma similar, se o parâmetro **"Permite vincular a Natureza em vários Filtros CIP - PERMITNTFILTCIP"** for ativado, será permitida a inclusão da mesma Natureza em mais de um Filtro para cálculo CIP.
