---
id: "360042727554"
titulo: "Operação Interna e UF do emitente difere da UF do destinatário/remetente contribuinte do ICMS(NT2015/002)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042727554-Opera%C3%A7%C3%A3o-Interna-e-UF-do-emitente-difere-da-UF-do-destinat%C3%A1rio-remetente-contribuinte-do-ICMS-NT2015-002"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:36Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "SEFAZ", "ICMS", "TOP", "CFOP", "521", "Rejeição por Divergência de UF Interna", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# Operação Interna e UF do emitente difere da UF do destinatário/remetente contribuinte do ICMS(NT2015/002)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16513055583639) MENSAGEM:**

[521 - Rejeição]: Operação Interna e UF do emitente difere da UF do destinatário/remetente contribuinte do ICMS.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16513071302935) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/article_attachments/16513055593111) Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

Aba: **"Livro Fiscal"**

Campo **"Atualização de Livro ICMS":** Livro de Saída - Se Movimento de Venda, a atualização do Livro será Saída.

- CFOP's para FORA do Estado: Se Movimento de Venda, CFOP inicia com 6
- CFOP's para DENTRO do Estado: Se Movimento de Venda, CFOP inicia com 5

![Imagem 4: Caso as configurações acima estejam incorretas, realize os devidos ajustes, considere inutilizar numeração da nota e…](https://ajuda.sankhya.com.br/hc/article_attachments/16513055599255) Caso as configurações acima estejam incorretas, realize os devidos ajustes, considere inutilizar numeração da nota e realizar um novo lançamento/faturamento.

**![Imagem 5: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16513055605911) IMPORTANTE:**

Para os casos onde a UF do Emitente for diferente da UF do Destinatário, e definido um endereço de entrega dentro do Estado, atente-se as configurações abaixo:

A regra de validação 521 não se aplica se a operação é presencial (campo <indPres> igual a 1 - "Operação presencial") e não possui frete (o campo <modFrete> igual a 9 - "Sem frete"). (NT 2011/004).

![Imagem 6: Tela " Tipo de Operação - TOP" ( Comercial » Arquivo » Cadastros » Tipos de Operação - TOP )](https://ajuda.sankhya.com.br/hc/article_attachments/16513055593111) Tela **"[Tipo de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)

- Aba **"NF-e/NFC-e"**
- Campo **"Indicador de Presença para NF-e/NFC-e"**= 1 - Operação Presencial

![Imagem 7: Lançamento da nota, aba "Transporte" , campo "CIF/FOB": sem frete .](https://ajuda.sankhya.com.br/hc/article_attachments/16513055599255) Lançamento da nota, aba **"Transporte"**, campo **"CIF/FOB":** sem frete**.**

![Imagem 8: Se ajustada a informação do item 1, inutilize o lançamento e emita uma nova nota.](https://ajuda.sankhya.com.br/hc/article_attachments/16513071323159) Se ajustada a informação do item 1, inutilize o lançamento e emita uma nova nota.

![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16513071325591) **CAUSA:**

Quando for emitida uma NF-e com Indicador de Destino da Operação (idDest) igual a 1 - "Estadual" (Operação Interna) e a UF do Emitente da NF-e for diferente da UF do Destinatário, será retornado a rejeição.

(1)** Exceções a regra:**

1. A regra de validação 521 não se aplica se o campo <UFCons> (UF de Consumo) foi informada com a mesma UF do emitente. (NT 2010/007);
2. A regra de validação 521 não se aplica se a operação é presencial (campo <indPres> igual a 1 - "Operação presencial") e não possui frete (o campo <modFrete> igual a 9 - "Sem frete"). (NT 2011/004).

**![Imagem 10: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16513071336343) OBSERVAÇÃO:**

([NT2015/002](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=VNyyxYte6T4=)) - Nota técnica
