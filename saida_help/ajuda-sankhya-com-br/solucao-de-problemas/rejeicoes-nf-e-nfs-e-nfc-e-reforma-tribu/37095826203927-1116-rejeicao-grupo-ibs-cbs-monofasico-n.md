---
id: "37095826203927"
titulo: "1116 Rejeição: Grupo IBS/CBS Monofásico não informado [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37095826203927-1116-Rejei%C3%A7%C3%A3o-Grupo-IBS-CBS-Monof%C3%A1sico-n%C3%A3o-informado-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:21:33Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Alíquota de IBS", "Classificação Tributária do IBS e da CBS", "Alíquotas de CBS", "Alíquotas de IBS", "Alíquota de CBS", "Tributação monofásica do IBS/CBS"]
---

# 1116 Rejeição: Grupo IBS/CBS Monofásico não informado [nItem: 999]

**MENSAGEM**

1116 Rejeição: Grupo IBS/CBS Monofásico não informado [nItem: 999]

**SITUAÇÃO**

Ao tentar emitir uma NF-e ou NFC-e com produtos sujeitos à tributação monofásica do IBS/CBS, o documento foi rejeitado pela SEFAZ porque o grupo de informações referente à tributação monofásica não foi informado, mesmo sendo obrigatório para o CST utilizado.

**SOLUÇÃO**

**(1)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique o CST do IBS/CBS utilizado no documento fiscal e confirme se ele exige a informação do grupo monofásico.

**(2)** Localize o CST utilizado na nota fiscal e verifique se ele possui o indicador que **exige informação do IBS/CBS Monofásico** (ind\_gIBSCBSMono = 1).

**(3)** Acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos) e verifique se o produto está configurado corretamente para a tributação monofásica.

**(4)** Na aba **"Tributação"** do cadastro do produto, configure a **"Classificação Tributária do IBS e da CBS"** (cClassTrib) com um código que permita a tributação monofásica (indicador INDMONO = S).

**(5)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se a TOP utilizada está configurada corretamente para operações com produtos monofásicos.

**(6)** Após realizar as configurações necessárias, tente emitir o documento fiscal novamente.

**CAUSA**

Esta rejeição ocorre quando o CST do IBS/CBS informado no documento fiscal possui um indicador que **exige a informação do grupo monofásico** (ind\_gIBSCBSMono = 1), mas este grupo não foi informado na nota fiscal.

De acordo com a regra de validação UB13-40, quando o CST do IBS/CBS informado possui indicador que exige informação do IBS/CBS Monofásico, o grupo gIBSCBSMono (id: UB84, grupo: imposto/IBSCBS/gIBSCBSMono) deve ser obrigatoriamente informado.

Esta validação está relacionada à tributação monofásica prevista na Lei Complementar 214/2025, onde determinados produtos estão sujeitos ao regime monofásico de tributação do IBS e da CBS, exigindo informações específicas no documento fiscal.
