---
id: "1500003158621"
titulo: "Código do meio de pagamento inexistente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003158621-C%C3%B3digo-do-meio-de-pagamento-inexistente"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T15:25:14Z"
rotulos: ["Configuração", "SEFAZ", "Financeiro", "436", "Código de pagamento", "Atualizar tipo correto", "Consultar tabela SEFAZ", "Erro", "Meio de Pagamento"]
---

# Código do meio de pagamento inexistente

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16334651391511) MENSAGEM:**

[436-Rejeição]: Código do meio de pagamento inexistente.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16334629836567)SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse o cadastro de "Tipos de Titulo" em: Financeiro » Arquivos » Cadastros » Tipos de Título » Tipos de Título ;](https://ajuda.sankhya.com.br/hc/article_attachments/16334651396503) Acesse o cadastro de **"Tipos de Titulo"** em: Financeiro » Arquivos » Cadastros » Tipos de Título » Tipos de Título;

![Imagem 4: Selecione o tipo de título utilizado na nota rejeitada (É possível conferir essa informação na aba "Financeiro" da…](https://ajuda.sankhya.com.br/hc/article_attachments/16334629838999) Selecione o tipo de título utilizado na nota rejeitada (É possível conferir essa informação na aba **"Financeiro"** da nota, campo **"Tipo de Título"**);

![Imagem 5: Na aba: "Geral" , selecione o campo: "Tipo de pgto para NFC-e / NF-e / CF-e"](https://ajuda.sankhya.com.br/hc/article_attachments/16334651398295) Na aba: **"Geral"**, selecione o campo: **"Tipo de pgto para NFC-e / NF-e / CF-e"**

![Imagem 6: Na aba: "Geral" , selecione o campo: "Tipo de pgto para NFC-e / NF-e / CF-e"](https://ajuda.sankhya.com.br/hc/article_attachments/15070615018647)

Defina o  tipo de pagamento correto (diferente de 99-Outros), considerando as seguintes opções:

**01-Dinheiro;**
**02-Cheque;**
**03-Cartão de Crédito;**
**04-Cartão de Débito;**
**05-Crédito Loja;**
**10-Vale Alimentação;**
**11-Vale Refeição;**
**12-Vale Presente;**
**13-Vale Combustível;**
**15-Boleto Bancário;
16-Deposito Bancário;
17-Pagamento Instantâneo (PIX);
18-Transferencia Bancaria, Carteira Digital;
19-Programa de Fidelidade, Cashback, Credito Virtual;
90-Sem pagamento;**

![Imagem 7: O Tipo de Título está vinculado ao cadastro de Tipos de Negociação ( Comercial » Arquivo » Cadastros » Tipos de…](https://ajuda.sankhya.com.br/hc/article_attachments/16334629841303) O Tipo de Título está vinculado ao cadastro de Tipos de Negociação (Comercial » Arquivo » Cadastros » Tipos de Negociação), aba: **"Parcelas";**

![Imagem 8: O Tipo de Título está vinculado ao cadastro de Tipos de Negociação ( Comercial » Arquivo » Cadastros » Tipos de…](https://ajuda.sankhya.com.br/hc/article_attachments/15070627475223)

![Imagem 9: Feito o ajuste, redigite o cabeçalho da nota e gere um novo lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16334629842839) Feito o ajuste, redigite o cabeçalho da nota e gere um novo lote.

**![Imagem 10: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16334651403543)CAUSA:**

Quando for emitida uma NF-e (modelo 55) ou NFC-e (modelo 65) e no Tipo de Pagamento um valor que não consta na tabela de meios de pagamento disponibilizada pela SEFAZ, haverá a rejeição pelo motivo

**Tabela** [Nota Tecnica: 2020.006 v1.40](https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=tW+YMyk/50s=)

![Imagem 11: Quando for emitida uma NF-e (modelo 55) ou NFC-e (modelo 65) e no Tipo de Pagamento um valor que não consta na tabela…](https://ajuda.sankhya.com.br/hc/article_attachments/1500008410522)
