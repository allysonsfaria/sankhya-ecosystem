---
id: "360043118313"
titulo: "Valor do troco incorreto(NT2016/002)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043118313-Valor-do-troco-incorreto-NT2016-002"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:37Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "XML", "SEFAZ", "Financeiro", "869", "Valor do Troco Incorreto", "Erro"]
---

# Valor do troco incorreto(NT2016/002)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16086049845655) MENSAGEM:**

869-Rejeição: Valor do troco incorreto.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16086088244119) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Financeiro » Arquivos » Cadastros » Tipos de Título » Tipos de Título](https://ajuda.sankhya.com.br/hc/article_attachments/16086088246167) Acesse: Financeiro » Arquivos » Cadastros » Tipos de Título » Tipos de Título

- Aba: **"Geral"**
- Campo **"Tipo de pgto para NFC-e / NF-e / CF-e":** Confirme com opção diferente de 90-Sem pagamento

![Imagem 4: Considere analisar o XML, onde o vTroco = vPag - vNF](https://ajuda.sankhya.com.br/hc/article_attachments/16086049853207) Considere analisar o XML, onde o vTroco = vPag - vNF

![Imagem 5: Após os ajustes, acesse a opção 'Outras Opções>>Refazer Financeiro' e, posteriormente, gere o Lote da Nota.](https://ajuda.sankhya.com.br/hc/article_attachments/16086049858071) Após os ajustes, acesse a opção 'Outras Opções>>Refazer Financeiro' e, posteriormente, gere o Lote da Nota.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16086049860119) CAUSA:**

Quando for emitida uma NF-e (modelo 55) ou NFC-e (modelo 65) e o valor do troco calculado no grupo dos dados do pagamento for diferente do resultado da subtração entre o valor do pagamento e o valor da NF-e/NFC-e, haverá a rejeição.

![Imagem 7: OBSERVAÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16086049862423) **OBSERVAÇÃO**:

1- Nota Técnica(2016/002)

<http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=uvfnqOj%20spg=>
