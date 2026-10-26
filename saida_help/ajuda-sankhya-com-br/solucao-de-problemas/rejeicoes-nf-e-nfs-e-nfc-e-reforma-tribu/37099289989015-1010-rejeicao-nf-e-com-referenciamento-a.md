---
id: "37099289989015"
titulo: "1010 Rejeição: NF-e com referenciamento a nível de nota e item [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37099289989015-1010-Rejei%C3%A7%C3%A3o-NF-e-com-referenciamento-a-n%C3%ADvel-de-nota-e-item-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-10-05T20:53:48Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "TOP", "Financeiro", "Erro", "NF-e com referenciamento", "Nível de nota (cabeçalho)", "presença de documentos fiscais referenciados", "Referenciamento de documentos fiscais", "Nível de item"]
---

# 1010 Rejeição: NF-e com referenciamento a nível de nota e item [nItem: 999]

**MENSAGEM**

1010 Rejeição: NF-e com referenciamento a nível de nota e item [nItem: 999]

**SITUAÇÃO**

Ao emitir uma NF-e, o sistema retorna uma rejeição ao identificar a presença de documentos fiscais referenciados no cabeçalho da nota e também nos itens do documento.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo

**(1)** Acesse a tela **''Tipos de Operação - TOP''** (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

**(2)** Verifique a configuração da TOP utilizada na nota fiscal rejeitada.

**(3)** Na aba **“NF-e/NFC-e/CF-e”**, verifique se existe alguma configuração de **referenciamento de documentos fiscais** definida no nível da nota fiscal.

**(4)** Acesse a nota fiscal que apresentou a rejeição e confirme se há **documentos fiscais referenciados**, tanto no **cabeçalho** da nota quanto nos **itens**, removendo qualquer referência indevida, se necessário.

**(5)** Escolha **apenas um nível** para referenciar os documentos fiscais: Se optar pelo referenciamento no nível da nota (cabeçalho), remova todos os referenciamentos nos itens. Se optar pelo referenciamento no nível dos itens, remova todos os referenciamentos no cabeçalho da nota.

**(6)** Após realizar as alterações necessárias, gere novamente a NF-e para transmissão à Sefaz.

**CAUSA**

Esta rejeição ocorre devido a uma regra de validação da Sefaz que impede o referenciamento simultâneo de documentos fiscais em dois níveis diferentes na mesma NF-e. De acordo com as especificações técnicas, o referenciamento de documentos fiscais deve ser feito **exclusivamente** em um dos níveis:

- **Nível de nota (cabeçalho)**: quando o referenciamento se aplica a toda a nota fiscal.
- **Nível de item**: quando o referenciamento é específico para determinados itens da nota fiscal.

Quando o sistema detecta referenciamentos nos dois níveis simultaneamente, a validação falha e a nota é rejeitada com o código 1010.
