---
id: "37095981518231"
titulo: "1029 Rejeição: CST do IBS/CBS informado não permite informação de diferimento Estadual [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37095981518231-1029-Rejei%C3%A7%C3%A3o-CST-do-IBS-CBS-informado-n%C3%A3o-permite-informa%C3%A7%C3%A3o-de-diferimento-Estadual-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:21:29Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Erro", "CST do IBS/CBS", "NF-e ou NFC-e", "Diferimento Estadual", "Benefício Fiscal", "CST compatível com diferimento"]
---

# 1029 Rejeição: CST do IBS/CBS informado não permite informação de diferimento Estadual [nItem: 999]

**MENSAGEM**

1029 Rejeição: CST do IBS/CBS informado não permite informação de diferimento Estadual [nItem: 999]

**SITUAÇÃO**

Rejeição apresentada na emissão de uma NF-e ou NFC-e quando é informado o grupo de **diferimento estadual do IBS (gIBSUF/gDif)** em conjunto com um CST que não permite a utilização desse tipo de benefício fiscal.

**SOLUÇÃO**

**(1)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique o tipo de operação utilizado na nota fiscal rejeitada.

**(2)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique o **CST** configurado para a operação.

**(3)** Verifique se o CST utilizado possui o indicador que **não permite** o uso de diferimento (ind\_gDif = 0). Neste caso, será necessário utilizar um CST compatível com diferimento ou remover o grupo de diferimento estadual.

**(4)** Para corrigir a situação, escolha uma das seguintes opções:

- Altere o CST para um que permita o uso de diferimento estadual (ind\_gDif = 1), caso a operação realmente necessite deste benefício fiscal, ou
- Remova o grupo de diferimento estadual (gIBSUF/gDif) da configuração da alíquota, caso o benefício fiscal não seja aplicável à operação.

**(5)** Após realizar as alterações, tente emitir a nota fiscal novamente.

**CAUSA**

A rejeição ocorre devido à regra de validação UB22-10 da Sefaz, que verifica se o CST do IBS/CBS informado no documento fiscal possui o indicador que permite o uso de diferimento estadual. Cada CST possui indicadores específicos que determinam quais benefícios fiscais podem ser aplicados.

Quando o indicador de diferimento (ind\_gDif) do CST é igual a 0, significa que este CST não permite a utilização do grupo de diferimento estadual. Se mesmo assim o grupo for informado, a nota será rejeitada com o código 1029.
