---
id: "18530761296279"
titulo: "Rejeição 269: CNPJ Emitente da NF Complementar difere do CNPJ da NF Referenciada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/18530761296279-Rejei%C3%A7%C3%A3o-269-CNPJ-Emitente-da-NF-Complementar-difere-do-CNPJ-da-NF-Referenciada"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:52:25Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "TOP", "Rejeição 269: CNPJ Emitente Diferente na NF Complementar", "Erro", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# Rejeição 269: CNPJ Emitente da NF Complementar difere do CNPJ da NF Referenciada

**269 - Rejeição: CNPJ/CPF emitente da NF-e complementar difere do CNPJ/CPF da NF referenciada**

### SITUAÇÃO

Esta rejeição ocorre ao tentar emitir uma **"NF-e complementar"** (tag: finNFe=2) ou uma **"NF-e de Crédito"** do tipo **"3-Retorno"** (tag: tpNFCredito=3) ou do tipo **"4-Redução de Valores"** (tag: tpNFCredito=4), quando o **"CNPJ/CPF do emitente"** da nota fiscal que está sendo emitida difere do **"CNPJ/CPF do emitente"** da nota fiscal referenciada.

### SOLUÇÃO

**(1)** Confira se realmente está emitindo uma **"NF-e complementar"**. Se não for o caso, acesse a tela **"Tipos de Operação - TOP"** (Comercial >> Arquivo >> Cadastros >> Tipos de Operação) e valide se o campo **"NF-e"** está configurado corretamente. Se realmente for uma **"NF-e complementar"**, prossiga para o passo seguinte.

**(2)** Baixe o XML da nota referenciada e valide se o **"CNPJ do emissor"** está igual ao **"CNPJ da empresa"** que está emitindo a nota. Se estiver diferente, valide com sua contabilidade o procedimento adequado.

 Caso o **"CNPJ do XML"** esteja correto, acesse a tela **"Empresa"** (Configurações >> Cadastros >> Empresas) para validar se os dados cadastrais estão corretos. Caso contrário, ajuste o cadastro, redigite alguma informação da nota para atualizar o lote e tente autorizar novamente.

**(3)** Certifique-se de que está vinculando a **"Nota fiscal referenciada"** correta. Caso tenha vinculado a nota fiscal incorreta, corrija a referência no campo **"NF Referenciada"** (tag: NFref), informando a chave de acesso correta.

**(4)** Após a correção, realize novamente a transmissão da **"NF-e complementar"** ou de **"NF-e de crédito"**.

### CAUSA

A rejeição ocorre porque, conforme a **"NT 2018.001"**, em **"NF-e complementares"** e **"NF-e de crédito"** dos tipos **"3-Retorno"** e **"4-Redução de Valores"**, o **"CNPJ/CPF do emitente"** da nota fiscal que está sendo emitida deve ser o mesmo da nota fiscal referenciada. Esta validação garante que apenas o emitente original possa emitir documentos complementares ou de crédito relacionados às suas próprias notas fiscais.
