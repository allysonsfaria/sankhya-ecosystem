---
id: "37141374193431"
titulo: "1007 Rejeição: CST do IBS/CBS informado não permite informação de redução de alíquota municipal [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37141374193431-1007-Rejei%C3%A7%C3%A3o-CST-do-IBS-CBS-informado-n%C3%A3o-permite-informa%C3%A7%C3%A3o-de-redu%C3%A7%C3%A3o-de-al%C3%ADquota-municipal-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:25Z"
rotulos: ["Configuração", "SEFAZ", "Impostos", "CST do IBS/CBS", "Alíquotas de CBS", "Alíquotas de IBS", "alíquota municipal para um CST", "Nota Fiscal (modelo 55)", "Nota Fiscal de Consumidor Eletrônica (modelo 65)", "Grupo de redução de alíquota municipal"]
---

# 1007 Rejeição: CST do IBS/CBS informado não permite informação de redução de alíquota municipal [nItem: 999]

**MENSAGEM**

1007 Rejeição: CST do IBS/CBS informado não permite informação de redução de alíquota municipal [nItem: 999]

**SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal (modelo 55) ou Nota Fiscal de Consumidor Eletrônica (modelo 65), o documento foi rejeitado porque foi informado o grupo de redução de alíquota municipal para um CST do IBS/CBS que não permite esse tipo de informação.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique o CST utilizado no item rejeitado.

**(2)** Verifique se o CST informado possui o indicador que **não permite** o uso de redução de alíquota (ind\_gRed = 0).

**(3)** Escolha uma das seguintes opções:

- Altere o CST para um que permita a informação de redução de alíquota municipal (ind\_gRed = 1).
- Remova o grupo de redução de alíquota municipal (gIBSMun/gRed) da nota fiscal.

**(4)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas) e localize a nota rejeitada.

**(5)** Edite a nota fiscal e ajuste o item com a rejeição, aplicando a correção escolhida no passo 3.

**(6)** Salve as alterações e tente emitir a nota fiscal novamente.

**CAUSA**

Esta rejeição ocorre quando é informado o grupo de redução de alíquota municipal (gIBSMun/gRed) para um CST do IBS/CBS que possui o indicador que não permite o uso de redução de alíquota (ind\_gRed = 0).

Cada CST possui indicadores específicos que determinam quais grupos de informações podem ou não ser utilizados na nota fiscal. Quando um grupo de informação é utilizado em desacordo com o que é permitido pelo CST, a Sefaz rejeita o documento fiscal.

De acordo com a regra de validação UB45-10, se o CST possui indicador que não permite o uso de Redução de Alíquota (ind\_gRed = 0), o grupo de Redução de Alíquota Municipal (gIBSMun/gRed) não deve ser informado, exceto em casos específicos previstos na legislação.
