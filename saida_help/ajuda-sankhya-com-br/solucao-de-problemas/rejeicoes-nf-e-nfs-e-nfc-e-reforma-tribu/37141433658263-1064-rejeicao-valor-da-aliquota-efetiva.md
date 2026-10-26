---
id: "37141433658263"
titulo: "1064 Rejeição: Valor da Alíquota Efetiva da CBS calculado incorretamente [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37141433658263-1064-Rejei%C3%A7%C3%A3o-Valor-da-Al%C3%ADquota-Efetiva-da-CBS-calculado-incorretamente-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:17Z"
rotulos: ["Configuração", "NF-e", "Portal de Vendas", "SEFAZ", "Impostos", "NFC-e (modelo 65)", "NF-e (modelo 55)", "Grupo de Redução de Alíquota da CBS (gCBS/gRed)", "Valor da Alíquota Efetiva (pAliqEfet)", "Redução de Alíquota (gCBS/gRed)", "Alíquota Efetiva", "Alíquotas de CBS"]
---

# 1064 Rejeição: Valor da Alíquota Efetiva da CBS calculado incorretamente [nItem: 999]

**MENSAGEM**

1064 Rejeição: Valor da Alíquota Efetiva da CBS calculado incorretamente [nItem: 999]

**SITUAÇÃO**

Ao emitir uma NF-e (modelo 55) ou NFC-e (modelo 65) com grupo de Redução de Alíquota da CBS (gCBS/gRed), o sistema está calculando incorretamente o valor da Alíquota Efetiva (pAliqEfet), resultando na rejeição do documento fiscal pela SEFAZ.

**SOLUÇÃO**

**(1)** Acesse a tela [**"Portal de Vendas"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) (Comercial » Consultas » Portal de Vendas).

**(2)** Localize a nota fiscal que apresenta a rejeição. Ao selecioná-la, o sistema redirecionará automaticamente para a tela [**“Central de Vendas”**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), onde será possível realizar as conferências e ajustes necessários antes de uma nova tentativa de envio.

**(3)** Clique no botão **''Outras Opções do Item''** (ícone de três pontos) localizado na parte superior da grade de itens.

**(4)** Selecione a opção "**Consultar/Alterar Dados do Imposto do Item**" e verifique se o item possui o grupo de Redução de Alíquota da CBS (gCBS/gRed).

**(5)** Acesse a tela "**Alíquotas de CBS**" (Fiscal » Cadastros » Alíquotas de CBS) e localize o código de alíquota utilizado no item.

**(6)** Na aba "**Tributação**", verifique se o campo **"% da Redução de Alíquota CBS"** está configurado corretamente para o CST informado.

**(7)** Caso seja necessário, ajuste o percentual de redução de alíquota de acordo com a classificação tributária do item.

**(8)** Verifique se há compra governamental envolvida na operação. Em caso positivo, certifique-se de que o campo **"% Redução Alíquota (Gov.)"** esteja corretamente preenchido.

**(9)** Após realizar os ajustes necessários, cancele a nota rejeitada e emita uma nova nota fiscal com os valores corrigidos.

**CAUSA**

A rejeição 1064 ocorre quando o valor da Alíquota Efetiva da CBS (pAliqEfet) informado no documento fiscal não corresponde ao valor calculado pela SEFAZ. Conforme a regra de validação UB66-10, quando informado o grupo de Redução de Alíquota (gCBS/gRed), a Alíquota Efetiva deve ser calculada considerando o percentual de redução aplicável à operação.

O cálculo da Alíquota Efetiva varia de acordo com o tipo de operação:

- Para operações normais: a Alíquota Efetiva é calculada aplicando-se o percentual de redução sobre a alíquota nominal da CBS (pAliqEfet = pCBS - (pCBS \* pRedAliq / 100)).
- Para compras governamentais: há regras específicas de cálculo que devem ser observadas conforme a Lei Complementar 214/2025.

A partir de 2026, a alíquota padrão da CBS deve ser de 0,9%, conforme estabelecido na Nota Técnica 2025.002-RTC - Versão 1.20, e qualquer divergência no cálculo da alíquota efetiva resultará nesta rejeição.
