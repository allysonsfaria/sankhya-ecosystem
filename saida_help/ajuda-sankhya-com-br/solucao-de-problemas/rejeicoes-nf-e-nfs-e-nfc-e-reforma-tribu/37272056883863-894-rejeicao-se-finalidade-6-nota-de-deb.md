---
id: "37272056883863"
titulo: "894 Rejeição: Se finalidade = 6 (Nota de Débito), não informado tipo de nota de débito (tpNFDebito)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37272056883863-894-Rejei%C3%A7%C3%A3o-Se-finalidade-6-Nota-de-D%C3%A9bito-n%C3%A3o-informado-tipo-de-nota-de-d%C3%A9bito-tpNFDebito"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:13:32Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "TOP", "tpNFDebito", "Nota de Débito (finNFe = 6)", "Nota de Débito", "Tipo de Nota Fiscal de Débito"]
---

# 894 Rejeição: Se finalidade = 6 (Nota de Débito), não informado tipo de nota de débito (tpNFDebito)

**MENSAGEM**

894 Rejeição: Se finalidade = 6 (Nota de Débito), não informado tipo de nota de débito (tpNFDebito)

**SITUAÇÃO**

A NF-e é rejeitada quando a finalidade da nota é **Nota de Débito** (`finNFe = 6`) e o **tipo da nota de débito** não é informado por meio da tag `<tpNFDebito>`.

**SOLUÇÃO**

Siga o passo a passo para corrigir a rejeição:

**(1)** Acesse a tela [**''Tipos de Operação''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

**(2)** **Selecione a TOP utilizada** para emitir a NF-e rejeitada.

**(3)** Na aba **''NF-e/NFC-e/CF-e''**, no campo **''NF-e''** confirme se está configurado como **''Nota de Débito''**.

- Esse ajuste habilita o campo **''Tipo de Nota Fiscal de Débito''**

**(4)** Configure o campo ''Tipo de Nota Fiscal de Débito'' e selecione o tipo adequado conforme a operação, por exemplo:

- Multa e juros
- Pagamento antecipado
- Débitos de notas não processadas
- Transferência de crédito
- Perda em estoque
- Outros (dependendo da UF)

Esse preenchimento determina o valor de `<tpNFDebito>` no XML.

![Imagem 1: Esse preenchimento determina o valor de <tpNFDebito> no XML.](https://ajuda.sankhya.com.br/hc/article_attachments/37272056877975)

**(5)** Salve as alterações na TOP e transmita novamente a NF-e.

**(6)** Aguarde o retorno da SEFAZ e confirme a autorização da nota.

**CAUSA**

A rejeição ocorre devido à **configuração incompleta na TOP**, na aba ''NF-e/NFC-e/CF-e''. 

Quando o campo **NF-e** está configurado como **Nota de Débito**, o sistema habilita o campo **Tipo de Nota Fiscal de Débito**; se este não for preenchido corretamente, a NF-e será rejeitada.
