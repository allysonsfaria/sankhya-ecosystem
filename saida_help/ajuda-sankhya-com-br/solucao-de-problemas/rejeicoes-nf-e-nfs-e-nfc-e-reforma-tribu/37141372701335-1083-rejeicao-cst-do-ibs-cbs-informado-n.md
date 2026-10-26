---
id: "37141372701335"
titulo: "1083 Rejeição: CST do IBS/CBS informado não permite informação de diferimento Municipal [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37141372701335-1083-Rejei%C3%A7%C3%A3o-CST-do-IBS-CBS-informado-n%C3%A3o-permite-informa%C3%A7%C3%A3o-de-diferimento-Municipal-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:26Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "CST do IBS/CBS", "NF-e ou NFC-e", "Não permite informação de diferimento Municipal", "Grupo de diferimento municipal para um CST do IBS/CBS", "Não permite o uso de diferimento (ind_gDif = 0)", "Alíquotas de CBS", "Alíquotas de IBS"]
---

# 1083 Rejeição: CST do IBS/CBS informado não permite informação de diferimento Municipal [nItem: 999]

**MENSAGEM**

1083 Rejeição: CST do IBS/CBS informado não permite informação de diferimento Municipal [nItem: 999]

**SITUAÇÃO**

Ao emitir um documento fiscal (NF-e ou NFC-e), o sistema está rejeitando a nota fiscal porque foi informado um grupo de diferimento municipal para um CST do IBS/CBS que não permite a utilização deste tipo de informação.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

**(2)** Verifique o CST configurado para o item que está gerando a rejeição.

**(3)** Verifique se o CST configurado possui o indicador que **não permite** o uso de diferimento municipal (ind\_gDif = 0).

**(4)** Escolha uma das seguintes opções para corrigir o problema:

- **Altere o CST** do IBS/CBS para um código que **permita a utilização de diferimento municipal** (com indicador ind\_gDif = 1), caso seja necessário **manter o diferimento**; ou
- **Remova o grupo de diferimento municipal** (gIBSMun/gDif) da nota fiscal, **caso o diferimento não seja aplicável** para a operação.

**(5)** Após realizar as alterações necessárias, tente emitir o documento fiscal novamente.

**CAUSA**

Esta rejeição ocorre porque a regra de validação UB40-20 da SEFAZ verifica se o CST do IBS/CBS informado possui indicador que não permite o uso de diferimento (ind\_gDif = 0), mas mesmo assim foi informado o grupo de diferimento municipal (grupo: gIBSMun/gDif) no documento fiscal.

Cada CST do IBS/CBS possui indicadores específicos que determinam quais grupos de informações podem ou não ser utilizados na nota fiscal. Quando um CST com indicador que não permite diferimento municipal é utilizado, mas o grupo de diferimento é informado, a SEFAZ rejeita o documento fiscal com o código 1083.
