---
id: "37096015764759"
titulo: "1030 Rejeição: CST do IBS/CBS informado obriga informação de diferimento Estadual [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37096015764759-1030-Rejei%C3%A7%C3%A3o-CST-do-IBS-CBS-informado-obriga-informa%C3%A7%C3%A3o-de-diferimento-Estadual-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:21:27Z"
rotulos: ["Fiscal", "NF-e", "SEFAZ", "Impostos", "Alíquotas de CBS", "Alíquotas de IBS", "1030 Rejeição", "Rejeição 1030", "CST do IBS/CBS informado obriga informação de diferimento Estadual"]
---

# 1030 Rejeição: CST do IBS/CBS informado obriga informação de diferimento Estadual [nItem: 999]

**MENSAGEM**

1030 Rejeição: CST do IBS/CBS informado obriga informação de diferimento Estadual [nItem: 999]

**SITUAÇÃO**

Ao tentar emitir uma NF-e ou NFC-e, o documento foi rejeitado pela SEFAZ porque o CST do IBS/CBS utilizado exige a informação de diferimento Estadual, porém este grupo de informações não foi preenchido no documento fiscal.

**SOLUÇÃO**

**(1)** Acesse a tela [**''Portal de Vendas''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) (Comercial » Consultas » Portal de Vendas).

**(2)** Localize a ''**NF-e''** que apresentou a rejeição.

(Ao selecionar o documento, a Central de Vendas será aberta automaticamente) 

**(3)**  Na [''**Central de Vendas''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) (Comercial » Rotinas),  **selecione o item** que recebeu a rejeição. Depois clique no botão **''Outras Opções do Item''** (ícone de três pontos). Em seguida, selecione a opção **''Consultar/Alterar Dados do Imposto do Item''** e identifique o código da alíquota utilizada.

**(4)** Acesse a tela **"Alíquotas IBS e ou CBS"** (Livros Fiscais » Cadastros » Alíquotas IBS e CBS). Pesquise e selecione a alíquota identificada no passo 3. Na alíquota, verifique o **CST do IBS/CBS** que está sendo utilizado na operação.

**(5)**  Caso esteja sendo usado o CST **'510 - Diferimento'** se torna obrigatório o preenchimento do grupo de diferimento Estadual.

![Imagem 1: (4) Acesse a tela "Alíquotas IBS e ou CBS" (Livros Fiscais » Cadastros » Alíquotas IBS e CBS). Pesquise e selecione a…](https://ajuda.sankhya.com.br/hc/article_attachments/37962663429271)

**(6)** Assim, preencha o campo **"Percentual de Diferimento"** (pDif) com as informações de diferimento Estadual. O sistema calculará automaticamente o **"Valor do Diferimento"** (vDif) com base na fórmula: vDif = vBC x (pIBSUF / 100) x (pDif / 100) 

**(7)** Por outro lado, se não for aplicável o diferimento para esta operação, você pode alterar o **CST do IBS/CBS** para um código que não exija diferimento (com ind\_gDif = 0).

**(8)** Após realizar as configurações necessárias, gere o lote e envie novamente.

**CAUSA**

A rejeição ocorre porque o **Código de Situação Tributária (CST)** do IBS/CBS utilizado na nota fiscal possui um indicador que exige a informação de diferimento Estadual (ind\_gDif = 1), conforme regra de validação UB22-20. Quando este indicador está ativo, é obrigatório informar o grupo de diferimento (gIBSUF/gDif) com os dados necessários para o cálculo do valor diferido do IBS Estadual. O diferimento é um mecanismo de postergação do pagamento do imposto, transferindo a responsabilidade para outra etapa da cadeia produtiva. Quando um CST com indicador de diferimento é utilizado, o sistema precisa das informações completas sobre o percentual e valor do diferimento para realizar corretamente os cálculos tributários exigidos pela Reforma Tributária.
