---
id: "360043192373"
titulo: "GTIN informado, mas não informado o GTIN da unidade tributável [nItem:999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043192373-GTIN-informado-mas-n%C3%A3o-informado-o-GTIN-da-unidade-tribut%C3%A1vel-nItem-999"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:57Z"
rotulos: ["ERRONF", "#criadoRoger", "#RevisadoClaudio", "Produtos", "Configuração", "NF-e", "Impostos", "885", "Erro: GTIN tributável ausente", "Solução: Ajustar GTIN válido", "Ajuste: Atualizar cadastro refaturar", "Erro", "GTIN"]
---

# GTIN informado, mas não informado o GTIN da unidade tributável [nItem:999]

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16513402612631) MENSAGEM:**

[885 - Rejeição]: GTIN informado, mas não informado o GTIN da unidade tributável [nItem:999].

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16513427146519) SOLUÇÃO:**

Antes de iniciar os ajustes cadastrais no sistema, compreenda o conceito de EAN/GTIN:

- O GTIN, sigla de “Global Trade Item Number” é um identificador para itens comerciais. Os GTIN, anteriormente chamados de códigos EAN, são atribuídos para qualquer item (produto ou serviço) que pode ser precificado, pedido ou faturado em qualquer ponto da cadeia de suprimentos. O GTIN é utilizado para recuperar informação pré-definida e abrange desde as matérias primas até produtos acabados.
- Os GTINs podem ter o tamanho de 8, 12, 13 ou 14 dígitos e podem ser construídos utilizando qualquer uma das quatro estruturas de numeração dependendo da aplicação.
- O Cadastro Centralizado de GTIN (CCG) é um banco de dados contendo um conjunto reduzido de informações dos produtos que possuem o código de barras GTIN em suas embalagens e funciona de forma integrada com o CNP (Cadastro Nacional de Produtos da GS1), que é o cadastro mantido pela organização legalmente responsável pelo licenciamento do respectivo código de barras. Os produtos em circulação no mercado que possuem GTIN e que são informados nos documentos fiscais eletrônicos, NF-e e NFC-e, terão suas informações validadas no CCG, de acordo com o cronograma previsto na legislação.

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: " Produtos " ( Configurações » Cadastros » Produtos )](https://ajuda.sankhya.com.br/hc/article_attachments/16513427149591) Acesse: **"[Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)"** (Configurações » Cadastros » Produtos)

Aba: **"Impostos"**
Campo: **"EAN/GTIN Produto p/ NF-e":**

- Se para o respectivo item NÃO deverão ser enviadas informações de EAN/GTIN, ajuste esse campo para 'Não Informar':

![Imagem 4: Se para o respectivo item NÃO deverão ser enviadas informações de EAN/GTIN, ajuste esse campo para 'Não Informar':](https://ajuda.sankhya.com.br/hc/article_attachments/14635400995351)

Realizado o ajuste, realize a inutilização e posterior exclusão da NF-e 'Aguardando Correção', em seguida realize um novo faturamento.

![Imagem 5: Caso essa informação seja necessária, de acordo com a opção definida, verifique o respectivo cadastro e ajuste o…](https://ajuda.sankhya.com.br/hc/article_attachments/16513427152279) Caso essa informação seja necessária, de acordo com a opção definida, verifique o respectivo cadastro e ajuste o EAN/GTIN para um código válido.

- Aba: "**Geral"** , Campo "**Referência"**' : use um EAN válido;
- Aba: "**Unidade** **Alternativa"**, Campo "**Cód. de Barras da Unid. Alternativa":** use um EAN válido, atente-se à unidade marcada como 'Unid.Tributável';
- Aba: "**Estoque",** Campo: "**Código de Barras Estoque"** : use um EAN válido.

Realizados os ajustes, faça a inutilização e posterior exclusão da NF-e 'Aguardando Correção', em seguida, execute um novo faturamento.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16513402630423) CAUSA:**

Quando na emissão de uma NF-e/NFC-e for informado o GTIN e no GTIN da unidade tributável estiver nulo ou igual a "SEM GTIN", haverá a rejeição.

**![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16513402636183) OBSERVAÇÃO:**

([NT2017/001](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=xOi0MNXspSM=)) - Nota técnica
