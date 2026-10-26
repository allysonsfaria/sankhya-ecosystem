---
id: "1500000482862"
titulo: "Informado incorretamente o campo meio de pagamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500000482862-Informado-incorretamente-o-campo-meio-de-pagamento"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T15:26:14Z"
rotulos: ["#criadoRoger", "Configuração", "XML", "SEFAZ", "Financeiro", "899", "Tipo de pagamento incorreto ou empresa discrepante", "Rejeição [899] - Meio de pagamento incorreto", "Ajuste tipo de pagamento no cadastro", "Erro"]
---

# Informado incorretamente o campo meio de pagamento

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16275679327255) MENSAGEM**:

[899-Rejeição] Informado incorretamente o campo meio de pagamento.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16275633371927) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse o Tipos de Título em: Financeiro » Arquivos » Cadastros » Tipos de Título » Tipos de Título Aba: "Geral" Campo…](https://ajuda.sankhya.com.br/hc/article_attachments/16275633373847) Acesse o Tipos de Título em: Financeiro » Arquivos » Cadastros » Tipos de Título » Tipos de Título
Aba: **"Geral"**
Campo **"Tipo de pgto para NFC-e / NF-e / CF-e":** configurar, observando as opções abaixo

Para NFC-e considere as seguintes formas de pagamento:

- 01-Dinheiro;
- 02-Cheque;
- 03-Cartão de Crédito;
- 04-Cartão de Débito;
- 05-Crédito Loja;
- 10-Vale Alimentação;
- 11-Vale Refeição;
- 12-Vale Presente;
- 13-Vale Combustível;
- 15 - Boleto Bancário;
- 99 - Outros

![Imagem 4: Após os ajustes, acesse novamente a nota, redigite o tipo de negociação ou fature novamente e gere lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16275633375127) Após os ajustes, acesse novamente a nota, redigite o tipo de negociação ou fature novamente e gere lote.

**![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16275633376407) OBSERVAÇÃO:**

Pode causar rejeição também quando a empresa informada no cabeçalho for diferente da empresa informada no financeiro. Pois, o sistema busca os dados dos títulos e liga a empresa do financeiro com a empresa do cabeçalho.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16275679337623) CAUSA:**

Ocorre quando quando for emitida uma NFC-e (modelo 65) e no Tipo de Pagamento for informado sem pagamento, acontece a rejeição.

Trecho de XML: [tPag 90-Sem pagamento - Incorreto.]

![Imagem 7: Trecho de XML: (tPag 90-Sem pagamento - Incorreto.)](https://lh3.googleusercontent.com/-ypVypwAMoX0/X9tzoVBMqcI/AAAAAAAAIGw/Q89BGEZOhQAr0R6eeSkjJLKmkXxOScarQCK8BGAsYHg/s0/2020-12-17.png)

**Nota técnica:** [Nota Técnica 2016.002](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=XPcFD/sRNlQ=)
