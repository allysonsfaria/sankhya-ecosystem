---
id: "36069259293463"
titulo: "255 Rejeição: NF-e possui mais de uma NF referenciada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36069259293463-255-Rejei%C3%A7%C3%A3o-NF-e-possui-mais-de-uma-NF-referenciada"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-24T12:42:56Z"
rotulos: ["NF-e", "Retorno", "SEFAZ", "Crédito", "TOP", "Rejeição", "Multa e Juros", "Redução de valores", "NF-e possui mais de uma NF referenciada", "Tipo de crédito", "255 Rejeição", "Rejeição 255", "NF referenciada", "NF-e complementar", "NF-e de crédito", "Documentos Eletrônicos", "Comercial"]
---

# 255 Rejeição: NF-e possui mais de uma NF referenciada

**MENSAGEM**

255 Rejeição: NF-e possui mais de uma NF referenciada.

**SITUAÇÃO**

A mensagem de erro é apresentada ao tentar transmitir uma **NF-e complementar** ou **NF-e de crédito** no Sankhya OM, quando há mais de uma nota fiscal referenciada informada no documento.

**SOLUÇÃO**

Siga o passo a passo para corrigir a rejeição:

**(1)** Acesse a tela **''Central de Compras''** (Comercial » Rotinas » Central de Compras) e/ou **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

**(2)** Localize e selecione a nota fiscal que apresentou a rejeição.

**(3)** Na grade **''Cabeçalho''**, localize o campo **''Tipo Operação''** e identifique a TOP usada na nota.

**(4)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

**(5)** Busque e selecione o TOP identificado no passo 3.

**(6)** Na aba **"NF-e/NFC-e/CF-e"**, verifique se no campo **"NF-e"** está selecionada uma das opções abaixo:

- **Crédito**
- **Complementar**

**(1)** Se a nota for uma **NF-e de Crédito**, verifique no campo **“Tipo de Nota Fiscal de Crédito”** se está selecionada uma das seguintes opções:

- Multa e Juros;
- Retorno;
- Redução de valores.

**(7)** Feitas as verificações acima, caso a TOP usada seja **Complementar ou Crédito (do tipo Multa e Juros, Retorno ou Redução de valores)**, execute as ações abaixo:

- Retorne ao passo 1 e localize a nota que foi rejeitada;
- Na aba **"NF-e/NFS-e''**, verifique se o campo **"Chave NF-e referenciada"** tenha somente uma nota referenciada. Caso haja mais de uma, remova as demais até que permaneça somente uma nota referenciada.

**(8)** Clique em **"Salvar"** e, em seguida, transmita novamente a NF-e para a SEFAZ.

**(9)** Aguarde o retorno da SEFAZ e confirme a autorização da nota.

**CAUSA**

O erro ocorre porque, para **NF-e complementar** ou **NF-e de crédito** (do tipo Multa e Juros, Retorno ou Redução de valores), a legislação permite referenciar apenas uma nota fiscal. Ao informar mais de uma nota referenciada nesses casos, o sistema rejeita a transmissão.
