---
id: "360042651514"
titulo: "Item com CSOSN indevido(NT2015/002)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042651514-Item-com-CSOSN-indevido-NT2015-002"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:09Z"
rotulos: ["ERRONF", "#RevisadoBraga", "Configuração", "SEFAZ", "Impostos", "383", "Correção do CSOSN Indevido na NFC-e"]
---

# Item com CSOSN indevido(NT2015/002)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16086252077591) MENSAGEM:**

383-Rejeição: Item com CSOSN indevido.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16086252081815) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Comercial » Rotinas » Central de Vendas](https://ajuda.sankhya.com.br/hc/article_attachments/16086284468375) Acesse: Comercial » Rotinas » Central de Vendas

Verifique a NFC-e e na grade de itens identifique o campo "**CSOSN"** (se o campo estiver oculto, configure-o através do Configurador de Layout).

![Imagem 4: Verifique a NFC-e e na grade de itens identifique o campo " CSOSN" (se o campo estiver oculto, configure-o através do…](https://ajuda.sankhya.com.br/hc/article_attachments/14559742480535)

![Imagem 5: Após isso, identifique se o CSOSN está na lista de CSOSN's que são aceitos:](https://ajuda.sankhya.com.br/hc/article_attachments/16086252087191) Após isso, identifique se o CSOSN está na lista de CSOSN's que são aceitos:

- **102** - Tributada pelo Simples Nacional sem permissão de crédito;
- **103**- Isenção do ICMS no Simples Nacional para faixa de receita bruta;
- **300**- Imune;
- **400** -  Não tributada pelo Simples Nacional;
- **500**- ICMS cobrado anteriormente por substituição tributária (substituído) ou por antecipação;
- **900**- Outros (**a critério da UF**);

![Imagem 6: Para efetuar o ajuste do CSOSN acesse o cadastro de Alíquotas de ICMS (Comercial » Arquivo » Cadastros » Alíquotas),…](https://ajuda.sankhya.com.br/hc/article_attachments/16086252090775) Para efetuar o ajuste do CSOSN acesse o cadastro de Alíquotas de ICMS (Comercial » Arquivo » Cadastros » Alíquotas), identifique a regra de ICMS que a NFC-e se enquadrou e na aba **"Simples Nacional"** efetue os ajustes devidos.

Para mais informações de como localizar a regra de ICMS que está sendo utilizada, consulte: [Como identificar qual a alíquota/exceção de ICMS utilizada no lançamento?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043050753)

- Dúvidas sobre qual o CSOSN a ser utilizado: acione o contador da empresa.

![Imagem 7: Após os ajustes, redigite o parceiro ou empresa na NFC-e e gere um novo lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16086252094231) Após os ajustes, redigite o parceiro ou empresa na NFC-e e gere um novo lote.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16086252100503) CAUSA:**

Quando for emitida uma NFC-e com Código de Situação da Operação – Simples Nacional (CSOSN) diferente da lista abaixo, será retornado a rejeição.

- **102** - Tributada pelo Simples Nacional sem permissão de crédito;
- **103**- Isenção do ICMS no Simples Nacional para faixa de receita bruta;
- **300**- Imune;
- **400** -  Não tributada pelo Simples Nacional;
- **500**- ICMS cobrado anteriormente por substituição tributária (substituído) ou por antecipação;
- **900**- Outros (a critério da UF);

**Exceção a regra:**

1. A critério da UF, aceitar CSOSN igual a 900-Outros;
2. A regra de validação 383 não se aplica, em produção, para Nota Fiscal com Data de Emissão anterior a 01/04/2016.

**![Imagem 9: Observação:](https://ajuda.sankhya.com.br/hc/article_attachments/16086284481047) Observação:**

1- **Nota Técnica** (2015/002)

<http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=v9JbkEY7evI=>
