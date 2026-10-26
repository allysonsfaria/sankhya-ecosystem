---
id: "37229558728343"
titulo: "E0427 Rejeição: O valor do serviço deve ser maior ou igual ao somatório dos valores informados para Desconto Incondicionado, Deduções/Reduções e Benefício Municipal."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37229558728343-E0427-Rejei%C3%A7%C3%A3o-O-valor-do-servi%C3%A7o-deve-ser-maior-ou-igual-ao-somat%C3%B3rio-dos-valores-informados-para-Desconto-Incondicionado-Dedu%C3%A7%C3%B5es-Redu%C3%A7%C3%B5es-e-Benef%C3%ADcio-Municipal"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:13:54Z"
rotulos: ["Fiscal", "Portal de Vendas", "SEFAZ", "NFS-e", "Erro", "valor total do serviço prestado", "Nota Fiscal de Serviço Eletrônica (NFS-e)", "emissão da Nota Fiscal de Serviço", "Desconto Incondicionado Deduções/Reduções ou Benefício Municipal", "valor do serviço seja maior ou igual"]
---

# E0427 Rejeição: O valor do serviço deve ser maior ou igual ao somatório dos valores informados para Desconto Incondicionado, Deduções/Reduções e Benefício Municipal.

**MENSAGEM**

E0427 Rejeição: O valor do serviço deve ser maior ou igual ao somatório dos valores informados para Desconto Incondicionado, Deduções/Reduções e Benefício Municipal.

**SITUAÇÃO**

Ao emitir uma **Nota Fiscal de Serviço Eletrônica (NFS-e)**, o usuário informou valores de **Desconto Incondicionado, Deduções/Reduções ou Benefício Municipal** que, somados, **ultrapassam o valor total do serviço prestado**. Com isso, a nota foi rejeitada pela Sefaz com a mensagem de erro E0427, impedindo a conclusão da emissão do documento fiscal.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse as telas [**''Portal de Vendas''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) (Comercial » Consulta » Portal de Vendas) e [**''Portal de Compras''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953-Portal-de-Compras) (Comercial » Consulta » Portal de Compras).

**(2)** Localize o documento fiscal que apresentou a rejeição.

**(3)** Verifique o **valor total do serviço prestado** informado no documento fiscal.

**(4)** Confira nos devidos campos os valores referentes a:

- **"Desconto Incondicionado"**
- **"Deduções/Reduções"**
- **"Benefício Municipal"**

**(4)**  Calcule o **somatório dos valores** de Desconto Incondicionado, Deduções/Reduções e Benefício Municipal.

**(5)** Certifique-se de que o **valor do serviço seja maior ou igual** ao somatório calculado no passo anterior.

**(6)** Caso o somatório seja maior que o valor do serviço, **ajuste os valores** dos campos de desconto, deduções ou benefício municipal, reduzindo-os para que fiquem dentro do limite permitido.

**(7)** Após realizar os ajustes necessários, **salve as alterações** no documento fiscal.

**(8)** Realize uma nova tentativa de **emissão da Nota Fiscal de Serviço**.

**CAUSA**

A rejeição ocorre porque a **Sefaz valida** que o valor total do serviço prestado deve ser **suficiente para cobrir** todos os descontos, deduções e benefícios municipais informados no documento fiscal. Quando o **somatório desses valores ultrapassa o valor do serviço**, a base de cálculo dos tributos ficaria negativa ou inconsistente, violando as regras fiscais estabelecidas. Por isso, o sistema rejeita automaticamente a nota com a mensagem E0427, impedindo a emissão até que os valores sejam corrigidos.
