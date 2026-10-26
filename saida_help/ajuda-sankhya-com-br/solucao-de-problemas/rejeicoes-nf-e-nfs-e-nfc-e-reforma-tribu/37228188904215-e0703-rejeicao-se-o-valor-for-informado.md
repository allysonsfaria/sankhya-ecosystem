---
id: "37228188904215"
titulo: "E0703 Rejeição: Se o valor for informado, então deve ser igual ou maior que 0 e menor ou igual o valor do serviço."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37228188904215-E0703-Rejei%C3%A7%C3%A3o-Se-o-valor-for-informado-ent%C3%A3o-deve-ser-igual-ou-maior-que-0-e-menor-ou-igual-o-valor-do-servi%C3%A7o"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-09-30T20:46:25Z"
rotulos: ["NF-e", "SEFAZ", "Impostos", "NFS-e", "Erro", "Valor informado deve ser igual ou maior que 0", "maior ou igual a 0 (zero)", "emissão de uma NF-e ou NFC-e", "Nota fiscal rejeitada", "valor deve ser menor ou igual ao valor total do serviço", "Valor não atende os critérios de validação", "Documentos Eletrônicos"]
---

# E0703 Rejeição: Se o valor for informado, então deve ser igual ou maior que 0 e menor ou igual o valor do serviço.

**MENSAGEM**

E0703 Rejeição: Se o valor for informado, então deve ser igual ou maior que 0 e menor ou igual o valor do serviço.

**SITUAÇÃO**

A rejeição ocorre durante a **emissão de uma NF-e ou NFC-e** quando o valor informado relacionado ao serviço está fora do intervalo permitido, sendo menor que zero ou maior que o valor total do serviço prestado.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a **nota fiscal rejeitada** e identifique o campo relacionado ao **valor do serviço** que está gerando a rejeição.

**(2)** Verifique se o **valor informado** está dentro do intervalo permitido:

- O valor deve ser **maior ou igual a 0 (zero)**.
- O valor deve ser **menor ou igual ao valor total do serviço** prestado.

**(3)** Caso o valor esteja **incorreto**, corrija-o informando um valor que atenda aos critérios de validação estabelecidos.

**(4)** Certifique-se de que o **valor total do serviço** está corretamente calculado e informado na nota fiscal.

**(5)** Após realizar as correções necessárias, **salve as alterações** e tente **transmitir novamente** a nota fiscal para a SEFAZ.

**CAUSA**

A rejeição **E0703** é gerada quando o sistema da SEFAZ identifica que um **valor relacionado ao serviço** foi informado na nota fiscal, mas este valor **não atende aos critérios de validação** estabelecidos. Especificamente, o valor informado é **menor que zero** ou **maior que o valor total do serviço**, violando as regras de validação que exigem que o valor esteja dentro do intervalo permitido (maior ou igual a 0 e menor ou igual ao valor do serviço).
