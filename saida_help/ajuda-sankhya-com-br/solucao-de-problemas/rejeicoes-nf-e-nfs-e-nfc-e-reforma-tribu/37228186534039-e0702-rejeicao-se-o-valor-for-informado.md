---
id: "37228186534039"
titulo: "E0702 Rejeição: Se o valor for informado, então deve ser igual ou maior que 0 e menor ou igual o valor do serviço."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37228186534039-E0702-Rejei%C3%A7%C3%A3o-Se-o-valor-for-informado-ent%C3%A3o-deve-ser-igual-ou-maior-que-0-e-menor-ou-igual-o-valor-do-servi%C3%A7o"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:16Z"
rotulos: ["NF-e", "SEFAZ", "NFS-e", "Regra de validação", "Erro", "Valor que não atende aos critérios de validação", "Valor informado está fora do intervalo permitido", "Valor maior ou igual a zero (0)", "Valor informado não ultrapassa o valor total do serviço", "Documentos Eletrônicos"]
---

# E0702 Rejeição: Se o valor for informado, então deve ser igual ou maior que 0 e menor ou igual o valor do serviço.

**MENSAGEM**

E0702 Rejeição: Se o valor for informado, então deve ser igual ou maior que 0 e menor ou igual o valor do serviço.

**SITUAÇÃO**

Durante a emissão de um documento fiscal eletrônico (NF-e ou NFC-e) com itens de serviço, a nota foi apresentada com um valor informado fora do intervalo aceito para esse tipo de operação, resultando na rejeição do documento pelo sistema.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse o documento fiscal que foi rejeitado e localize o **campo de valor relacionado ao serviço** que gerou a rejeição.

**(2)** Verifique se o **valor informado é maior ou igual a zero** (0). Valores negativos não são permitidos.

**(3)** Certifique-se de que o **valor informado não ultrapassa o valor total do serviço** prestado. O valor deve ser menor ou igual ao valor do serviço.

**(4)** Corrija o valor conforme necessário, garantindo que ele esteja **dentro do intervalo permitido** (≥ 0 e ≤ valor do serviço).

**(5)** Salve as alterações realizadas no documento fiscal.

**(6)** Reenvie o documento fiscal eletrônico para a SEFAZ para validação.

**CAUSA**

Esta rejeição ocorre quando o **valor informado no campo relacionado ao serviço** não atende às regras de validação da SEFAZ. A validação exige que, caso um valor seja informado, ele deve ser **maior ou igual a zero (0)** e **menor ou igual ao valor total do serviço** prestado. Valores negativos ou superiores ao valor do serviço violam essa regra e resultam na rejeição do documento fiscal.
