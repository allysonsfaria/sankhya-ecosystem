---
id: "37099423495447"
titulo: "1085 Rejeição: Total do IBS difere da soma do vIBS dos itens"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37099423495447-1085-Rejei%C3%A7%C3%A3o-Total-do-IBS-difere-da-soma-do-vIBS-dos-itens"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-09-11T13:23:53Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "TOP", "Reforma Tributária", "Artigo atualizado KCS", "NF-e ou NFC-e", "Total do IBS", "Soma do vIBS dos itens", "Valor total do IBS de forma diferente do somatório", "NF-e ou NFC-e é diferente do somatório dos valores de IBS", "Docs Eletrônicos - KCS"]
---

# 1085 Rejeição: Total do IBS difere da soma do vIBS dos itens

[1085] Rejeição: Total do IBS difere da soma do vIBS dos itens. [vIBS informado: X.XX, vIBS calculado: X.XX]

### Situação

Ao emitir uma NF-e ou NFC-e, o sistema está calculando o **valor total do IBS de forma diferente do somatório dos valores de IBS de cada item** do documento fiscal, gerando uma inconsistência que resulta na rejeição pela SEFAZ.

### Solução

Para corrigir esta rejeição, siga as abordagens abaixo:

**(1)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

**(2)** Localize e selecione a TOP utilizada na nota fiscal rejeitada.

**(3)** Na aba **"Despesas Acessórias"** verifique e marque as seguintes opções:

- **"ICMS proporcional ao ICMS dos itens":** marque todas as opções
- **"PIS proporcional ao PIS dos itens":** marque todas as opções
- **"IPI proporcional ao IPI dos itens":** marque todas as opções
- **"COFINS proporcional ao COFINS dos itens":** marque todas as opções
- **"S.T. proporcional ao S.T. dos itens":** marque todas as opções

**(4)** Salve as alterações.

**(5)** Inutilize a NF-e rejeitada.

**(6)** Exclua a nota fiscal rejeitada.

**(7)** Realize um novo lançamento da nota fiscal utilizando a TOP ajustada.

### Causa

Esta rejeição ocorre quando o valor total do IBS (Imposto sobre Bens e Serviços) informado no grupo de totais da NF-e ou NFC-e é **diferente do somatório** dos valores de IBS de cada item do documento fiscal.

De acordo com as regras de validação da SEFAZ, o valor total do IBS deve ser **exatamente igual** à soma dos valores de IBS de todos os itens da nota fiscal. Esta validação faz parte das novas regras implementadas pela Reforma Tributária (Lei Complementar nº 214/2025), que introduziu o IBS como um dos novos tributos do sistema tributário brasileiro.
