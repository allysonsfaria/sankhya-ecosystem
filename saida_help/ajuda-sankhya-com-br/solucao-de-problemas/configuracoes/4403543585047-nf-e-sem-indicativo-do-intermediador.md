---
id: "4403543585047"
titulo: "NF-e sem indicativo do intermediador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4403543585047-NF-e-sem-indicativo-do-intermediador"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:23:49Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "Impostos", "TOP", "não apagar", "434", "Solução para Rejeição 434 na NF-e"]
---

# NF-e sem indicativo do intermediador

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16345126033687) MENSAGEM:**

[Rejeição 434]: NF-e sem indicativo do intermediador

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16345141271959) SOLUÇÃO:**

Nesse caso, primeiramente verifique se o indicativo de presença está correto ao informar o indicativo sendo 2, 3, 4 ou 9. Para este exemplo, o indPres estava correto, então deverá adicionar o campo inIntermed.

Abaixo exemplo de XML com a correção:

| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22 | `[...]`  `<``ide``>`  `<``cUF``>00</``cUF``>`  `<``natOp``>REVENDA DE MERCADORIAS SIMPLES NACIONAL - SC</``natOp``>`  `<``mod``>55</``mod``>`  `<``serie``>000</``serie``>`  `<``nNF``>11111</``nNF``>`  `<``dhEmi``>2021-02-04T13:56:56-03:00</``dhEmi``>`  `<``tpNF``>1</``tpNF``>`  `<``idDest``>1</``idDest``>`  `<``cMunFG``>000000</``cMunFG``>`  `<``tpImp``>1</``tpImp``>`  `<``finNFe``>1</``finNFe``>`  `<``indFinal``>1</``indFinal``>`    `<!--Indicativo de Presença -->`  `<``indPres``>0</``indPres``>`    `<!--Indicativo do Intermediador -->`  `<``indIntermed``>1</``indIntermed``>`  `</``ide``>`  `[...]` |
| --- | --- |

**![Imagem 3: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16345141274263) IMPORTANTE:**

Os códigos aceitos no campo indIntermed são **0** (Operação sem intermediador) e **1** (Operação em site ou Plataformas de Terceiros

O indicador de presença pode ser configurado no sistema no cadastro da TOP do lançamento: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP, campo: **"Indicador de Presença para NF-e/NFC-e"** para puxar automaticamente na inserção do cabeçalho da nota ou também pode ser informado manualmente no cabeçalho da nota fiscal (Indicador de Presença para NF-e/NFC-e).

![Imagem 4: O indicador de presença pode ser configurado no sistema no cadastro da TOP do lançamento: Comercial » Arquivo »…](https://ajuda.sankhya.com.br/hc/article_attachments/15081648671511)

![Imagem 5: O indicador de presença pode ser configurado no sistema no cadastro da TOP do lançamento: Comercial » Arquivo »…](https://ajuda.sankhya.com.br/hc/article_attachments/15081678907671)

Portanto, quando for informada uma venda com o indicador de presença como não presencial (2, 3, 4 ou 9) deverá ser indicado o indicativo do intermediador, campo é configurado na TOP:  **"Indicador de Intermediador/Marketplace"**, suas opções são:

**- 0:** Operação sem intermediador (em site ou plataforma própria) ;
**- 1:** Operação em site ou plataforma de terceiros (intermediadores/marketplace) ;

![Imagem 6: - 0: Operação sem intermediador (em site ou plataforma própria) ; - 1: Operação em site ou plataforma de terceiros…](https://ajuda.sankhya.com.br/hc/article_attachments/15081704130583)

**Referências**

- Nota Técnica 2020.006 - v 1.40  - <https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=tW+YMyk/50s=>

**\* Indicativo de Presença**

**0 =** Não se aplica (por exemplo, Nota Fiscal complementar ou de ajuste);
**1 =** Operação presencial;
**2 =** Operação não presencial, pela Internet;
**3 =**Operação não presencial, tele atendimento;
**4 =** NFC-e em operação com entrega a domicílio;
**5 =** Operação presencial, fora do estabelecimento
**9 =** Operação não presencial, outros.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16345141277463)CAUSA:**

Quando for emitida uma NF-e (modelo 55) ou NFC-e (modelo 65) informando o indicativo de presença (Campo: indPres) igual a 2, 3, 4 ou 9\* e não informado o indicativo do Intermediário (Campo: indIntermed), haverá a rejeição pelo motivo 434 - NF-e sem indicativo do intermediador.

**Exceções e Observações**

Quando informado o indicador de presença (Campo: **"indPres"**) igual a 1, 0 ou 5, não deve ser informado o indicativo do Intermediário.

Entrará em Vigor:

- **Homologação**: 03/05/2021
- **Produção**: 01/09/2021

**Exemplo:**

No exemplo abaixo, foi emitido uma NF-e com indicador de presença igual a 3, mas não foi passada a informação do indicativo do intermediador. Nessa situação a NF-e foi rejeitada pelo motivo 434.

Trecho do XML:

| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19 | `[...]`  `<``ide``>`  `<``cUF``>00</``cUF``>`  `<``natOp``>REVENDA DE MERCADORIAS SIMPLES NACIONAL - SC</``natOp``>`  `<``mod``>11</``mod``>`  `<``serie``>000</``serie``>`  `<``nNF``>00000</``nNF``>`  `<``dhEmi``>0000000000000</``dhEmi``>`  `<``tpNF``>1</``tpNF``>`  `<``idDest``>1</``idDest``>`  `<``cMunFG``>000000</``cMunFG``>`  `<``tpImp``>1</``tpImp``>`  `<``finNFe``>1</``finNFe``>`  `<``indFinal``>1</``indFinal``>`    `<!--Indicativo de Presença -->`  `<``indPres``>0</``indPres``>`  `</``ide``>`  `[...]` |
| --- | --- |
