---
id: "37096425191831"
titulo: "1028 Rejeição: CST do IBS/CBS informado não permite informação de redução de alíquota da CBS [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37096425191831-1028-Rejei%C3%A7%C3%A3o-CST-do-IBS-CBS-informado-n%C3%A3o-permite-informa%C3%A7%C3%A3o-de-redu%C3%A7%C3%A3o-de-al%C3%ADquota-da-CBS-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:21:21Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Tabela de Indicadores de CST do IBS e da CBS", "Alíquotas de CBS", "Alíquotas de IBS", "Alíquota de CBS", "grupo: gCBS/gRed", "Grupo de redução de alíquota da CBS"]
---

# 1028 Rejeição: CST do IBS/CBS informado não permite informação de redução de alíquota da CBS [nItem: 999]

**MENSAGEM**

1028 Rejeição: CST do IBS/CBS informado não permite informação de redução de alíquota da CBS [nItem: 999]

**SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal Eletrônica (NF-e) ou Nota Fiscal de Consumidor Eletrônica (NFC-e), o sistema apresenta a rejeição acima, indicando que foi informado um grupo de redução de alíquota da CBS para um CST que não permite esse tipo de informação.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique o CST do IBS/CBS utilizado no item da nota fiscal que está gerando a rejeição.

**(2)** Identifique o **CST do IBS/CBS** que está sendo utilizado no item rejeitado e verifique se este CST permite a informação de redução de alíquota da CBS. Consulte a **Tabela de Indicadores de CST do IBS e da CBS** para confirmar.

**(3)** Se o CST utilizado não permitir redução de alíquota da CBS (indicador ind\_gRed = 0), você tem duas opções:

- Remova a informação de redução de alíquota da CBS no cadastro da alíquota utilizada
- Altere para um CST que permita a informação de redução de alíquota da CBS.

**(4)** Para remover a informação de redução de alíquota retorne o passo 1, localize a alíquota utilizada e remova as informações do grupo **''% da Redução de Alíquota CBS''** (grupo: gCBS/gRed).

**(5)** Caso opte por alterar o CST, selecione um que possua o indicador ind\_gRed = 1, que permite a informação de redução de alíquota da CBS.

**(6)** Após realizar as alterações necessárias, tente emitir a nota fiscal novamente. 

**CAUSA**

A rejeição ocorre porque foi informado o grupo de Redução de Alíquota da CBS (grupo: gCBS/gRed) para um CST do IBS/CBS que possui o indicador que não permite o uso de redução de alíquota (ind\_gRed = 0). Cada CST do IBS/CBS possui indicadores específicos que determinam quais informações podem ou não ser utilizadas com ele.

Quando um CST tem o indicador ind\_gRed = 0, significa que ele não permite a utilização do grupo de redução de alíquota da CBS, e qualquer tentativa de informar esse grupo resultará na rejeição 1028.
