---
id: "37095955639831"
titulo: "1104 Rejeição: Valor da Base de cálculo do IBS e CBS difere do somatório dos valores que a compõem [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37095955639831-1104-Rejei%C3%A7%C3%A3o-Valor-da-Base-de-c%C3%A1lculo-do-IBS-e-CBS-difere-do-somat%C3%B3rio-dos-valores-que-a-comp%C3%B5em-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-10-08T19:04:21Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "IBS", "CBS", "Reforma Tributária", "Artigo atualizado KCS", "NFC-e (modelo 65)", "NF-e (modelo 55)", "Tributação do IBS e CBS", "Valor da Base de cálculo do IBS e CBS", "Docs Eletrônicos - KCS"]
---

# 1104 Rejeição: Valor da Base de cálculo do IBS e CBS difere do somatório dos valores que a compõem [nItem: 999]

**MENSAGEM**

1104 Rejeição: Valor da Base de cálculo do IBS e CBS difere do somatório dos valores que a compõem [nItem: 999]

**SITUAÇÃO**

Ao emitir uma **NF-e (modelo 55)** ou **NFC-e (modelo 65)** com a **tributação do IBS e CBS**, o sistema está calculando incorretamente o valor da base de cálculo desses impostos, resultando em uma divergência entre o valor informado no campo vBC (Base de Cálculo) e o somatório dos componentes que deveriam formar essa base.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Verifique se os valores que compõem a base de cálculo do IBS e CBS estão corretos no documento fiscal.

A base de cálculo deve ser igual ao somatório de:

- (+) vProd (Valor do Produto)
- (+) vServ (Valor do Serviço)
- (+) vFrete (Valor do Frete)
- (+) vSeg (Valor do Seguro)
- (+) vOutro (Outros Valores)
- (+) vII (Valor do Imposto de Importação)
- (-) vDesc (Valor do Desconto)
- (-) vPIS (Valor do PIS)

**(2)** Acesse a tela de **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se a configuração da operação está correta para o cálculo do IBS e CBS.

**(3)** Na aba **"Impostos"**, verifique se os parâmetros relacionados à Reforma Tributária estão configurados corretamente.

**(4)** Acesse a tela **"Assistente de Configuração Integral da Reforma Tributária"** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária) e verifique se as configurações de tributação estão corretas.

**(5)** Verifique o **CST do IBS/CBS** utilizado no documento fiscal. Certifique-se de que o código está correto e compatível com a operação realizada.

**(6)** Recalcule os impostos do documento fiscal para garantir que a base de cálculo do IBS e CBS seja atualizada corretamente.

**(7)** Após realizar as correções necessárias, tente emitir o documento fiscal novamente. 

 **CAUSA**

Esta rejeição ocorre quando o valor informado no campo vBC (Base de Cálculo do IBS e CBS) não corresponde ao somatório dos componentes que devem formar essa base, conforme estabelecido no Art. 346 da LC 214/2025. A base de cálculo do IBS e CBS deve seguir uma fórmula específica, somando valores como o valor do produto, serviço, frete, seguro e outros valores, e subtraindo valores como descontos e PIS.
