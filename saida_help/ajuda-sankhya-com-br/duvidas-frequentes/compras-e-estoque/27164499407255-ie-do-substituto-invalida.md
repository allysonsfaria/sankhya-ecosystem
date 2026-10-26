---
id: "27164499407255"
titulo: "IE do substituto inválida"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27164499407255-IE-do-substituto-inv%C3%A1lida"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-07-22T14:39:57Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "Impostos", "Passos para resolver", "Razão do erro", "Detalhe do erro", "IE do substituto inválida", "Rejeição 211", "Erro"]
---

# IE do substituto inválida

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/27164499382039) **MENSAGEM:**

[Rejeição 211] IE do substituto inválida

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/27164499384983)SOLUÇÃO:**

Verifique no XML a tag <IEST> e, se realmente estiver divergente, faça o ajuste na tela  **"Empresa"** (Comercial » Preferências » Empresa) aba **"Insc. Estadual Contribuinte ST no Estado Dest".**

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/27164475796887)CAUSA:**

A Inscrição Estadual do Substituto Tributário é única para cada UF. Na validação da IEST são consideradas as regras da UF do Local de Entrega para operação de Faturamento, direto de veículos novos ou as regras da UF do destinatário, nos demais casos.

Regra de validação da Sefaz Nota Técnica 2015/003 (v. 1.30):

![Imagem 4: Regra de validação da Sefaz Nota Técnica 2015/003 (v. 1.30):](http://www.oobj.com.br/bc/assets/Articles/45/Rej211_NFE.PNG)

**Observação**

- Somente é indicado o preenchimento do parâmetro Inscrição Estadual quando a filial (emitente) tem no estado do destinatário uma IE válida;
- A IE do Substituto Tributário deve ser diferente da IE do Emitente e do Destinatário, porém a IEST deverá estar cadastrada na UF do Destinatário;
- É possível validar a IE do emitente na UF do destinatário, através do o Portal do Sintegra ou do Cadastro Centralizado de Contribuintes.
- Caso seja uma Operação de Faturamento Direto de veículos novos, deve-se informar IEST cadastrada na UF do Local de Entrega do veículo.
