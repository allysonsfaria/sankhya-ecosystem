---
id: "25140318105239"
titulo: "652 Rejeição: informado indicador de desoneração inválido para a ZFM [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25140318105239-652-Rejei%C3%A7%C3%A3o-informado-indicador-de-desonera%C3%A7%C3%A3o-inv%C3%A1lido-para-a-ZFM-nItem-999"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:46:04Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "ICMS", "Impostos", "652 Rejeição", "Rejeição 652", "informado indicador de desoneração inválido para a ZFM [nItem: 999]"]
---

# 652 Rejeição: informado indicador de desoneração inválido para a ZFM [nItem: 999]

Essa rejeição ocorre quando uma NF-e for emitida com o tag: **<motDesICMS>** igual a 7 (desoneração Suframa) e não for informada a tag **<indDeduzDeson>** igual a 1 - Conforme validação da [Nota Técnica 2023.004 - v.1.11](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=eWTd1q6pRMM=) - Publicada em 19/03/2024.

![Imagem 1: Essa rejeição ocorre quando uma NF-e for emitida com o tag: <motDesICMS> igual a 7 (desoneração Suframa) e não for…](https://ajuda.sankhya.com.br/hc/article_attachments/25140318086039)

No sistema Sankhya para geração da TAG: **<indDeduzDeson>** é necessário que a NT 2023.004 -v1.11 esteja ativada na tela **"Preferência da Empresa"** (Caminho: Comercial >> Preferências >> Empresa), aba **"Documentos Fiscais"**, sub-aba **"NF-e/NFC-e"** e **"sub-aba Nota Técnica NF-e"**, conforme imagem abaixo: 

![Imagem 2: No sistema Sankhya para geração da TAG: <indDeduzDeson> é necessário que a NT 2023.004 -v1.11 esteja ativada na tela…](https://ajuda.sankhya.com.br/hc/article_attachments/25140325679127)

Além disso para que a TAG: **<indDeduzDeson>**seja gerada igual a 1, na tela de alíquotas de ICMS referente a regra que foi estabelecida no produto da NF-e, o campo: "**Forma de Repasse Desoneração**" tem que está selecionado com a opção: "**Destacar valores e deduzir do total da nota**" , ao contrário dessa opção essa TAG será gerada com o valor igual a 0. 

Já o valor na TAG: **<motDesICMS>** é referente ao campo: **"Cód.Mot.Desoneração ICMS"** da tela: **"[Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS)"** da regra de ICMS que foi atribuído ao produto na Nota Fiscal. 

Para mais informações referente a Nota Técnica 2023.004 - v.1.11, acesse o manual: [Nota Técnica 2023.004 - v.1.11](https://ajuda.sankhya.com.br/hc/pt-br/articles/24258905713815)
