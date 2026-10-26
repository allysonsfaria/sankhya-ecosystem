---
id: "360045119153"
titulo: "Filtro para cálculo CIP (Requisições)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119153-Filtro-para-c%C3%A1lculo-CIP-Requisi%C3%A7%C3%B5es"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:55:41Z"
rotulos: ["AJUDA DO SKW", "manual", "Custos", "Configuração", "Requisições", "PERMITCRFILTCIP", "CIP", "Produção", "Natureza", "Centro Resultado", "Construtor expressão", "Converter expressão", "PERMITNTFILTCIP", "Tarifas", "Filtro para cálculo CIP (Requisições)", "br.com.sankhya.mgecom.cad.filtrocadastrocip", "Filtro para cálculo CIP (Requisições) manual", "Cadastro de Pontos: Requisições Tarifas CIP", "Custos Indiretos: Energia elétrica materiais consumo", "Filtros e Abas: Centro Resultado Natureza Tarifas"]
---

# Filtro para cálculo CIP (Requisições)

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312801790999) Módulo: Produção > Cadastros
```

---

Nesta tela serão cadastrados os pontos (Requisições) que serão considerados no momento da realização do cálculo das devidas Tarifas; estes pontos podem ser adicionados à tela, por meio da criação de um filtro personalizado (aba **"Filtro"** - botão **"Construtor expressão"**), onde nos casos em que a empresa já trabalhava com esta rotina no MGE e já possuía um filtro cadastrado, este mesmo filtro poderá ser utilizado no Sankhya Om através do botão localizado no lado superior direito da aba.

**Observação:** os filtros baseados em requisições irão considerar os documentos do tipo Q - Requisições e L - Devolução de Requisição.

![CIP2](https://ajuda.sankhya.com.br/hc/article_attachments/360061940613)

As indústrias possuem alguns custos indiretos que são registrados partindo-se de [Tarifas CIP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611074), tais como, energia elétrica e/ou materiais de consumo. Ao final da produção, os custos gerados por estes aspectos são rateados entre o que foi produzido. Como alguns produtos (Produtos Acabados) precisam absorver uma parte maior do custo destes itens, se comparado à outros produtos acabados, informa-se no campo **"Perc. do valor a ser usado no custo"** o percentual do valor a ser utilizado no cálculo do custo de uma Tarifa CIP. A informação inserida neste campo, é comumente utilizada em casos onde duas ou mais tarifas possuem o mesmo filtro para cálculo de seu custo, porém, cada uma deve absorver uma determinada quantia desse valor.

Além da aba Filtro, a tela conta com as abas **"Centro Resultado"**, **"Natureza"** e **"Tarifas"** que são de simples e semelhante preenchimento; nelas podem ser inseridos os [Centros de Resultado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606754), as [Naturezas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774) e [Tarifas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611074) que serão utilizadas para construção do Filtro em questão e consequentemente, serão consideradas no cálculo.

![Imagem 3: Informações adicionais:](https://ajuda.sankhya.com.br/hc/article_attachments/16649354415511)**Informações adicionais:**

- Caso o parâmetro **"Permite vincular o CR em vários Filtros CIP - PERMITCRFILTCIP"** seja ativado, será possível realizar a inserção do mesmo Centro de Resultado em mais de um Filtro para cálculo CIP;
- De forma similar, se o parâmetro **"Permite vincular a Natureza em vários Filtros CIP - PERMITNTFILTCIP"** for ativado, será permitida a inclusão da mesma Natureza em mais de um Filtro para cálculo CIP.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119153-Filtro-para-c%C3%A1lculo-CIP-Requisi%C3%A7%C3%B5es#top)
