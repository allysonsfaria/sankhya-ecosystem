---
id: "37141291328535"
titulo: "745 Rejeição: NF-e sem grupo do PIS [nItem:nnn]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37141291328535-745-Rejei%C3%A7%C3%A3o-NF-e-sem-grupo-do-PIS-nItem-nnn"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:37Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "Alíquotas de COFINS", "Impostos", "Alíquotas de PIS", "Erro", "Código de Situação Tributária", "NF-e sem as informações do grupo do PIS", "NF-e sem grupo do PIS"]
---

# 745 Rejeição: NF-e sem grupo do PIS [nItem:nnn]

**MENSAGEM**

745 Rejeição: NF-e sem grupo do PIS [nItem:nnn]

**SITUAÇÃO**

Ao emitir uma Nota Fiscal Eletrônica (NF-e), o sistema não incluiu as informações do grupo do PIS para um ou mais itens da nota. A SEFAZ rejeitou o documento fiscal, indicando qual item específico está sem a informação necessária através do número informado após "nItem:".

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse as telas **''Alíquotas de PIS''** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de PIS) e **''Alíquotas de COFINS''** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de COFINS).

**(2)** Verifique no campo **''Cód. sit. tributária''**, se a alíquota de PIS no item rejeitado está corretamente configurada para a operação.

**(3)** Acesse a tela [**''Portal de Vendas''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) (Comercial » Consulta » Portal de Vendas) e identifique qual item está com problema.

**(4)** Selecione a nota rejeitada, clique no botão **"NF-e"** e selecione a opção **"Gerar XML da NF-e em arquivo para Conferência"**.

**(5)** Abra o XML gerado com o Internet Explorer ou Bloco de Notas e pressione **Ctrl+F** para buscar o número do item indicado na rejeição (nItem:nnn).

**(6)** Acesse a tela **''Produtos''** (Configurações » Cadastros » Produtos » Produtos).

**(7)** Na aba **''Impostos''** verifique se o campo **''Grupo PIS''** está configurado corretamente.

**(8)** Além disso, acesse a tela **''Tipos de Operação - TOP''** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se a TOP utilizada está com as opções **"Tem PIS"** e **"Tem COFINS"** devidamente habilitadas.

**(9)** Após os ajustes necessários, exclua o item da nota e faça o lançamento novamente ou fature o pedido novamente para gerar um novo lote.

**CAUSA**

Quando for emitida uma NF-e sem as informações do grupo do PIS para um ou mais itens, a SEFAZ rejeitará o documento. Esta rejeição ocorre porque, de acordo com a legislação fiscal, é **obrigatório** informar os dados de tributação do PIS para cada item da nota fiscal, mesmo que seja uma situação de isenção, não incidência ou suspensão. A ausência dessas informações impede a correta validação e processamento do documento fiscal pelos sistemas da SEFAZ.
