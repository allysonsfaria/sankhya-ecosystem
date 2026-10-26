---
id: "37098195306135"
titulo: "1146 Rejeição: NF-e referenciada de pagamento antecipado informada indevidamente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37098195306135-1146-Rejei%C3%A7%C3%A3o-NF-e-referenciada-de-pagamento-antecipado-informada-indevidamente"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:20:17Z"
rotulos: ["Configuração", "NF-e", "Central de Vendas", "SEFAZ", "TOP", "Financeiro", "Pagamento antecipado", "NF-e de pagamento antecipado", "Nota fiscal referenciada de pagamento antecipado", "finNFe diferente de 2", "Tipo complemento de preço"]
---

# 1146 Rejeição: NF-e referenciada de pagamento antecipado informada indevidamente

**MENSAGEM**

1146 Rejeição: NF-e referenciada de pagamento antecipado informada indevidamente

**SITUAÇÃO**

Ao emitir uma **NF-e**, o sistema retorna rejeição quando há **informação de nota fiscal referenciada de pagamento antecipado** vinculada ao documento fiscal.

**SOLUÇÃO**

**(1)** Acesse a tela [**"Tipos de Operação - TOP"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

**(2)** Selecione o tipo de operação utilizado na nota fiscal que está sendo rejeitada.

**(3)** Na aba **"NF-e/NFC-e/CF-e''**, verifique o campo **"NF-e"**.

**(4)** Caso a emissão seja de **NF-e de complemento de preço**, verifique se o campo **“NF-e”**, está configurado com a opção **“Complementar”**.

**(5)** Se **não** se tratar de uma nota fiscal complementar, acesse a tela [**“Central de Vendas”**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) (Comercial » Rotinas » Central de Vendas) e **remova a referência à nota fiscal de pagamento antecipado** informada no documento.

**(6)** Se a emissão for de **NF-e complementar**, confirme se a **nota fiscal referenciada** está informada corretamente e se corresponde, de fato, a uma **NF-e de pagamento antecipado**.

**(7)** Após realizar as correções, **gere um novo lote** e tente emitir a **NF-e novamente**.

**CAUSA**

Esta rejeição ocorre quando uma NF-e referenciada de pagamento antecipado é informada em uma nota fiscal que **não possui finalidade de complemento** (finNFe diferente de 2) ou quando a nota fiscal não é do **tipo complemento de preço**. De acordo com a legislação, as notas fiscais de pagamento antecipado só podem ser referenciadas em notas fiscais complementares específicas para complemento de preço.
