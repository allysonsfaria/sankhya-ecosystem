---
id: "37141617558807"
titulo: "1176 Rejeição: Total do IBS estornado difere da soma dos itens"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37141617558807-1176-Rejei%C3%A7%C3%A3o-Total-do-IBS-estornado-difere-da-soma-dos-itens"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:57Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "TOP", "IBS", "Reforma Tributária", "NFC-e (modelo 65)", "NF-e (modelo 55)", "valores de IBS estornados em cada item da nota", "valor total do IBS estornado", "IBS estornado"]
---

# 1176 Rejeição: Total do IBS estornado difere da soma dos itens

**MENSAGEM**

1176 Rejeição: Total do IBS estornado difere da soma dos itens

**SITUAÇÃO**

Ao emitir uma NF-e (modelo 55) ou NFC-e (modelo 65) com estorno de IBS, o sistema identificou que o valor total do IBS estornado informado no grupo de totais da nota fiscal é diferente do somatório dos valores de IBS estornados em cada item da nota.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas) e localize a nota rejeitada.

**(2)** Na grade **''Itens''**, aperte em **''Outras Opções'' (ícone de três pontos)**, e selecione **''Consultar/Alterar Dados do Imposto do Item''.**

**(3)** Na seção **''IBS''**, confira os valores de estornados para cada item. Certifique-se de que os valores estão corretos conforme a legislação.

**(4)** Verifique se o "**Tipo de Operação - TOP**" (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) está configurado corretamente para calcular o IBS estornado.

**(5)** Na aba **''Impostos''**, seção "**Reforma Tributária**", verifique se o campo **''Tem IBS''** está habilitado.

**(6)** Caso esteja realizando o cálculo manual do IBS estornado, some corretamente os valores de IBS estornados de cada item e informe o total exato no rodapé da nota fiscal.

**(7)** Após realizar as correções, inutilize a NF-e rejeitada, exclua-a e emita uma nova nota fiscal com os valores corretos. 

**CAUSA**

Esta rejeição ocorre quando, ao emitir uma **NF-e (modelo 55)** ou NFC-e (modelo 65), o valor total do IBS estornado informado no grupo de totais da nota fiscal é diferente do somatório dos valores de IBS estornados em cada item da nota.

De acordo com as regras de validação da Sefaz, o valor total do IBS estornado deve corresponder exatamente à soma dos valores de IBS estornados de todos os itens da nota fiscal, conforme estabelecido pela Lei Complementar nº 214/2025 que implementa a Reforma Tributária.
