---
id: "37228217300375"
titulo: "E0704 Rejeição: Se o valor for informado, então deve ser igual ou maior que 0 e menor ou igual o valor do serviço."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37228217300375-E0704-Rejei%C3%A7%C3%A3o-Se-o-valor-for-informado-ent%C3%A3o-deve-ser-igual-ou-maior-que-0-e-menor-ou-igual-o-valor-do-servi%C3%A7o"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:14Z"
rotulos: ["NF-e", "Central de Vendas", "SEFAZ", "Valor", "Valor Unitário", "Erro", "NF-e ou NFC-e", "Valor específico relacionado ao serviço", "Valor total", "Valor informado está fora do intervalo válido"]
---

# E0704 Rejeição: Se o valor for informado, então deve ser igual ou maior que 0 e menor ou igual o valor do serviço.

**MENSAGEM**

E0704 Rejeição: Se o valor for informado, então deve ser igual ou maior que 0 e menor ou igual o valor do serviço.

**SITUAÇÃO**

Ao emitir uma **NF-e** ou **NFC-e** contendo serviços, o usuário informou um **valor específico relacionado ao serviço** que está **fora do intervalo permitido** pela validação da Sefaz. Este valor pode estar **negativo** ou **superior ao valor total do serviço** prestado, gerando a rejeição do documento fiscal.

**SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas) e localize o documento fiscal rejeitado.

**(2)** Na grade **''Itens''**, verifique os valores informados para os serviços nos seguintes campos:

- **''Vlr. Unitário''**
- **''Vlr. Total''**

**(3)** Certifique-se de que o valor seja **maior ou igual a zero (0)** e seja **menor ou igual ao valor total do serviço** prestado.

**(4)** Corrija o valor informado, ajustando-o para que esteja **dentro do intervalo permitido** pela validação.

**(5)** Salve as alterações.

**(6)** Reenvie a **NF-e** ou **NFC-e** para a Sefaz para validação e autorização.

**CAUSA**

Esta rejeição ocorre quando um **valor relacionado ao serviço** informado no documento fiscal está **fora do intervalo válido** estabelecido pela Sefaz. A validação exige que, caso o valor seja informado, ele deve ser **maior ou igual a zero (0)** e **menor ou igual ao valor total do serviço** prestado. Valores negativos ou superiores ao valor do serviço violam essa regra e impedem a autorização do documento.
