---
id: "15273988694551"
titulo: "GTIN incompatível com a NCM [nItem:999; NCM esperada: 99999999] "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15273988694551-GTIN-incompat%C3%ADvel-com-a-NCM-nItem-999-NCM-esperada-99999999"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:57:19Z"
rotulos: ["Produtos", "NF-e", "SEFAZ", "Impostos", "NCM", "Rejeição 891", "Rejeição 891: GTIN e NCM", "Erro", "GTIN"]
---

# GTIN incompatível com a NCM [nItem:999; NCM esperada: 99999999] 

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16589298140823) MENSAGEM:**

[Rejeição 891]: GTIN incompatível com a NCM [nItem:999; NCM esperada: 99999999]

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16589312640919) SOLUÇÃO:**

Verifique se o GTIN informado para o produto está devidamente cadastrado e vinculado a um NCM ativo.

- Acesse a tela **"Cadastro de Produtos"**, veja o NCM que está cadastrado na aba **"Impostos".**

![Imagem 3: - Acesse a tela "Cadastro de Produtos" , veja o NCM que está cadastrado na aba "Impostos".](https://ajuda.sankhya.com.br/hc/article_attachments/15299305934359)

A SEFAZ disponibiliza no link abaixo o NCM correto de acordo com cada EAN/GTIN, copie o código de barras do Produto e consulte no link abaixo:

[- CONSULTA GTIN](https://dfe-portal.svrs.rs.gov.br/Nfe/Gtin)

Após a consulta, realize a correção do NCM no Cadastro do Produto e gere lote novamente.

<prod>

<cEAN>78983574100015</cEAN>
...
<NCM>02032900</NCM>
...
</prod>

![Imagem 4: <cEAN>78983574100015</cEAN> ... <NCM>02032900</NCM> ... </prod>](https://ajuda.sankhya.com.br/hc/article_attachments/15273936441879)

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16589298145175) CAUSA:**

A Regra da SEFAZ diz o seguinte :

- NCM informada na NF-e diferente da cadastrada no CCG Regra válida para documento fiscal modelo NF-e (55).

**![Imagem 6: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/16589298147735) OBSERVAÇÕES:**

**(2)** Todo GTIN(cEAN) é vinculado a um NCM, deve-se verificar se o GTIN informado está devidamente vinculado a um NCM válido no portal nacional;

**(2)** A regra estará disponível em ambiente de teste a partir de 06/03/2023 e em ambiente de produção a partir de 12/06/2023.
