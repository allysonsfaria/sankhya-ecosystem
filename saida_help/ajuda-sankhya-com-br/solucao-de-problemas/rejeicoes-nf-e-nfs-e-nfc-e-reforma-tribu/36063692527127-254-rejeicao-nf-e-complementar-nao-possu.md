---
id: "36063692527127"
titulo: "254 Rejeição: NF-e complementar não possui NF referenciada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36063692527127-254-Rejei%C3%A7%C3%A3o-NF-e-complementar-n%C3%A3o-possui-NF-referenciada"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-30T13:27:12Z"
rotulos: ["Configuração", "NF-e", "Retorno", "SEFAZ", "Crédito", "Erro", "254 Rejeição", "Rejeição 254", "NF-e complementar não possui NF referenciada", "Nota Fiscal Referenciada", "eferência à nota original.", "Multa e Juros", "Redução de valores", "Documentos Eletrônicos"]
---

# 254 Rejeição: NF-e complementar não possui NF referenciada

**MENSAGEM**

254 Rejeição: NF-e complementar não possui NF referenciada

**SITUAÇÃO**

A mensagem de erro é apresentada ao tentar transmitir uma **NF-e** marcada como **"Complementar"** ou de **"Crédito"** no sistema, sem informar uma **"Nota Fiscal Referenciada"** ou seja não foi preenchida a referência à nota original.

**SOLUÇÃO**

Siga o passo a passo para corrigir a rejeição:

**(1)** Acesse a tela **''Central de Compras''** (Comercial » Rotinas » Central de Compras) e **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

**(2)** Localize e selecione a nota fiscal que apresentou a rejeição.

**(3)** Na grade **''Cabeçalho''**, verifique o campo **''Tipo Operação''** e identifique a TOP usada na nota.

**(4)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e busque a TOP identificada no passo anterior.

**(5)** Na aba **"NF-e/NFC-e/CF-e"**, verifique se o campo **"NF-e"** está selecionada uma das opções abaixo:

- **''Crédito''**, ou
- **''Complementar''.**

**(1)** Se for uma **NF-e de Crédito**, verifique no campo **"Tipo de Nota Fiscal de Crédito"** se está selecionada uma das opções abaixo:

- **''Multa e Juros''**
- **''Retorno''**
- **''Redução de valores''**

**(6)** Feitas as verificações acima, caso a TOP usada seja **Complementar ou Crédito (do tipo Multa e Juros, Retorno ou Redução de valores)**, adicione uma **Chave NF-e Referenciada.** Para isso:

- Retorne no passo 1.
- Na aba **"NF-e/NFS-e"**, informe no campo **"Chave NF-e referenciada"** a chave de acesso da **NF-e original.**

**(7)**  Clique em **"Salvar"** e, em seguida, transmita novamente a NF-e para a SEFAZ.

**(8)** Aguarde o retorno da SEFAZ e confirme a autorização da nota.

**CAUSA**

A rejeição ocorre porque toda **NF-e complementar** ou de **crédito** (do tipo Multa e Juros, Retorno ou Redução de valores) deve obrigatoriamente referenciar a nota fiscal original que está sendo complementada. Quando a **"Nota Fiscal Referenciada"** não é informada, o sistema impede a transmissão da NF-e.
