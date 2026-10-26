---
id: "360044608194"
titulo: "Filtro para cálculo CIP (Lanç. Contábeis)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608194-Filtro-para-c%C3%A1lculo-CIP-Lan%C3%A7-Cont%C3%A1beis"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:52:00Z"
rotulos: ["AJUDA DO SKW", "manual", "Custos", "Configuração", "Centro de Resultado", "PERMITCRFILTCIP", "Filtro para cálculo CIP (Lanç. Contábeis)", "br.com.sankhya.filtro.para.calculo.cip.contabil", "Filtro para cálculo CIP (Lanç. Contábeis) manual", "Produção", "Financeiro", "Lançamentos Contábeis Tarifas CIP", "Centro Resultado Projetos Contas Contábeis Tarifas", "13º férias depreciação impostos", "Cadastros"]
---

# Filtro para cálculo CIP (Lanç. Contábeis)

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312713047575) Módulo: Produção > Cadastros
```

---

Nesta tela serão cadastrados os pontos (Lançamentos Contábeis) que serão considerados no momento da realização do cálculo das devidas Tarifas; estes pontos podem ser adicionados à tela, por meio da criação de um filtro personalizado (aba **"Filtro"** - botão **"Construtor expressão"**), onde nos casos em que a empresa já trabalhava com esta rotina no MGE e já possuía um filtro cadastrado, este mesmo filtro poderá ser utilizado no Sankhya Om através do botão localizado no lado superior direito da aba.

![CIP3](https://ajuda.sankhya.com.br/hc/article_attachments/360061936273)

As indústrias possuem alguns custos indiretos que são registrados partindo-se de [Tarifas CIP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611074), tais como, 13º e férias de funcionário, depreciação de maquinário, crédito de impostos e provisões de investimentos. Ao final da produção, os custos gerados por estes aspectos são rateados entre o que foi produzido. Como alguns produtos (Produtos Acabados) precisam absorver uma parte maior do custo destes itens, se comparado à outros produtos acabados, informa-se no campo **"Perc. do valor a ser usado no custo"** o percentual do valor a ser utilizado no cálculo do custo de uma Tarifa CIP. A informação inserida neste campo, é comumente utilizada em casos onde duas ou mais tarifas possuem o mesmo filtro para cálculo de seu custo, porém, cada uma deve absorver uma determinada quantia desse valor.

Além da aba Filtro, a tela conta com as abas **"Centro Resultado"**, **"Projetos"** , **"Contas Contábeis"** e **"Tarifas"** que são de simples e semelhante preenchimento; nelas podem ser inseridos os [Centros de Resultado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606754-Centros-de-Resultado), os [Projetos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109073-Projetos), as [Contas Contábeis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116393) e [Tarifas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611074) que serão utilizadas para construção do Filtro em questão e, consequentemente, serão consideradas no cálculo.

**Observação:** Caso o parâmetro **"Permite vincular o CR em vários Filtros CIP - PERMITCRFILTCIP"** seja ativado, será possível realizar a inserção do mesmo Centro de Resultado em mais de um Filtro para cálculo CIP.
