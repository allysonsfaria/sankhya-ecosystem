---
id: "37141414273687"
titulo: "1046 Rejeição: Percentual de redução de alíquota do Município não é válido para este cClassTrib [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37141414273687-1046-Rejei%C3%A7%C3%A3o-Percentual-de-redu%C3%A7%C3%A3o-de-al%C3%ADquota-do-Munic%C3%ADpio-n%C3%A3o-%C3%A9-v%C3%A1lido-para-este-cClassTrib-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:23Z"
rotulos: ["Configuração", "NF-e", "Cidades", "SEFAZ", "Impostos", "Alíquotas de CBS", "Alíquotas de IBS", "Redução de Alíquota", "Reforma Tributária (Lei Complementar nº 214/2025)", "Dados de Tributação", "Percentual de redução de alíquota do Município"]
---

# 1046 Rejeição: Percentual de redução de alíquota do Município não é válido para este cClassTrib [nItem: 999]

**MENSAGEM**

1046 Rejeição: Percentual de redução de alíquota do Município não é válido para este cClassTrib [nItem: 999]

**SITUAÇÃO**

Esta rejeição é apresentada durante a emissão do documento fiscal quando é informado um percentual de redução de alíquota municipal (pRedAliq) juntamente com a Classificação Tributária (cClassTrib) no IBS Municipal, e o sistema impede o processamento do documento devido à inconsistência entre essas informações.

**SOLUÇÃO**

**(1)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas  de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique o indicador de redução de alíquota (ind\_gRed) associado ao CST utilizado.

**(2)** Caso o CST utilizado não permita redução de alíquota (ind\_gRed = 0), remova o percentual de redução de alíquota municipal ou altere para um CST compatível com a redução desejada.

**(3)** Se o CST permitir redução de alíquota (ind\_gRed = 1), na aba **''Tributação''**, seção **''Dados de Tributação'',** no campo **''Cód''**, verifique se o percentual informado é válido para a Classificação Tributária (cClassTrib) utilizada na operação.

**(4)** Ajuste o documento fiscal com o percentual de redução de alíquota municipal correto para o CST e cClassTrib utilizados.

**(5)** Em caso de compra governamental, certifique-se de que o percentual de redução de alíquota está corretamente informado conforme a legislação aplicável.

**CAUSA**

A rejeição ocorre devido a uma das seguintes situações:

- O CST informado no documento possui um indicador que **exige o uso de Redução de Alíquota** (ind\_gRed = 1), mas o percentual de redução informado (pRedAliq) não é válido para a Classificação Tributária (cClassTrib) utilizada.
- O CST informado possui um indicador que **veda o uso de Redução de Alíquota** (ind\_gRed = 0), mas foi informado um percentual de redução de alíquota municipal maior que zero.
- Em operações de compra governamental, o percentual de redução de alíquota municipal não foi informado corretamente conforme as regras específicas para este tipo de operação.

Esta validação faz parte das regras implementadas pela Reforma Tributária (Lei Complementar nº 214/2025) para garantir a correta aplicação das alíquotas do IBS Municipal de acordo com a classificação tributária e o CST utilizados na operação.
