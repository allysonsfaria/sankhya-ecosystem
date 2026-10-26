---
id: "36397201069847"
titulo: "1164 Rejeição: Não informado tipo de nota de crédito"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36397201069847-1164-Rejei%C3%A7%C3%A3o-N%C3%A3o-informado-tipo-de-nota-de-cr%C3%A9dito"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:23:04Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "TOP", "Passos para resolver", "Erro", "1164 Rejeição", "Rejeição 1164", "Não informado tipo de nota de crédito", "Tipo de Nota Fiscal de Crédito", "Artigo atualizado KCS", "Como resolver", "Nota de Crédito", "Docs Eletrônicos - KCS"]
---

# 1164 Rejeição: Não informado tipo de nota de crédito

**MENSAGEM**

1164 Rejeição: Não informado tipo de nota de crédito

**SITUAÇÃO**

O usuário enfrenta rejeições pela SEFAZ ao emitir Notas Fiscais com finalidade 5 (Nota de Crédito) ou 6 (Nota de Débito) quando campos obrigatórios específicos (tpNFCredito ou tpNFDebito) não estão preenchidos no sistema.

**SOLUÇÃO**

**(1)** Acesse as telas **"Portal de Compras"** (Comercial >> Rotinas >> Portal de Compras) ou **"Portal de Vendas"** (Comercial >> Rotinas >> Portal de Vendas).

**(2)** Selecione a nota fiscal que apresentou a rejeição.

**(3)** Na Central, verifique o campo **"Tipo Operação"** e identifique a TOP utilizada na nota.

**(4)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial >> Arquivo >> Cadastros >> Tipos de Operação - TOP) e selecione a TOP identificada.

**(5)** Na aba **"NF-e/NFC-e/CF-e"**, verifique a configuração do campo **"NF-e"**:

Para Notas de Crédito: Se selecionada a opção **"Nota de Crédito"**, preencha o campo **"Tipo de Nota Fiscal de Crédito"** conforme o motivo (ex: Multa e juros, Apropriação de crédito presumido, Retorno).

Para Notas de Débito: Se selecionada a opção **"Nota de Débito"**, preencha o campo **"Tipo de Nota Fiscal de Débito"** corretamente.

![Imagem 1: Para Notas de Débito: Se selecionada a opção "Nota de Débito" , preencha o campo "Tipo de Nota Fiscal de Débito"…](https://ajuda.sankhya.com.br/hc/article_attachments/41842394218391)

**(6)** Salve as alterações.

**(7)**Após isso, exclua a nota anterior e gere uma nova.

**CAUSA**

A SEFAZ exige que, para as finalidades 5 (Nota de Crédito) e 6 (Nota de Débito), os respectivos campos complementares (tpNFCredito ou tpNFDebito) sejam informados no XML. A ausência de preenchimento, preenchimento indevido, datas de vigência desrespeitadas ou tipo de operação incorreto para o tipo de nota geram as rejeições validadas pela regra fiscal.
