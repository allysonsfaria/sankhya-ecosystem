---
id: "37096066960279"
titulo: "1032 Rejeição: CST do IBS/CBS informado não permite informação de redução de alíquota Estadual [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37096066960279-1032-Rejei%C3%A7%C3%A3o-CST-do-IBS-CBS-informado-n%C3%A3o-permite-informa%C3%A7%C3%A3o-de-redu%C3%A7%C3%A3o-de-al%C3%ADquota-Estadual-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-09-28T20:03:44Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Artigo atualizado KCS", "CST do IBS/CBS", "NF-e ou NFC-e", "Alíquotas de CBS", "Alíquotas de IBS", "Redução de alíquota Estadual", "CST do IBS/CBS que não permite a informação de redução de alíquota Estadual", "Docs Eletrônicos - KCS"]
---

# 1032 Rejeição: CST do IBS/CBS informado não permite informação de redução de alíquota Estadual [nItem: 999]

**MENSAGEM**

As seguintes mensagens de erro podem ser apresentadas durante a emissão de documentos fiscais:

**[1032]** Rejeição: CST do IBS/CBS informado não permite informação de redução de alíquota Estadual [nItem: 999]

**SITUAÇÃO**

A rejeição ocorre na autorização de NF-e ou NFC-e (modelos 55 e 65) quando o item da nota tem **redução de alíquota do IBS Estadual** (grupo "gIBSUF/gRed") informada, mas o **CST do IBS/CBS** usado no item não permite esse tipo de redução.

**SOLUÇÃO**

Identifique o item da nota indicado em **[nItem]** na mensagem de rejeição e anote qual Alíquota de IBS está vinculada a ele.

Acesse a tela **"Alíquotas de IBS"** (Livros Fiscais » Cadastros » Alíquotas de IBS), localize essa alíquota e abra a guia **"Tributação"**. Confira:

- o **CST do IBS/CBS** informado;
- se o campo **"% da Redução de Alíquota IBS Estadual"** está preenchido.

Corrija a configuração com uma das opções abaixo:

- **A operação tem direito à redução:** altere o "CST do IBS/CBS" da Alíquota de IBS para um CST que permita redução de alíquota, compatível com a operação e com o cClassTrib.
- **A operação não tem direito à redução:** mantenha o CST atual e deixe o campo "% da Redução de Alíquota IBS Estadual" zerado ou vazio.

Emita a nota fiscal novamente.

**CAUSA**

Cada CST do IBS/CBS tem indicadores que definem quais grupos podem ser informados no XML. O indicador **ind\_gRed** diz se o CST aceita redução de alíquota:

- **ind\_gRed = 1:** o CST permite informar redução de alíquota.
- **ind\_gRed = 0:** o CST não permite. Se o grupo "gIBSUF/gRed" for enviado mesmo assim, a SEFAZ rejeita a nota com o erro 1032.

Na prática, isso acontece quando a Alíquota de IBS usada no item tem o campo "% da Redução de Alíquota IBS Estadual" preenchido com um CST que não prevê redução, como um CST de tributação integral.

Essa validação corresponde à regra UB26-10 da documentação técnica da SEFAZ.
