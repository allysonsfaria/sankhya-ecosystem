---
id: "37141401468695"
titulo: "1044 Rejeição: CST do IBS/CBS informado obriga informação de diferimento Municipal [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37141401468695-1044-Rejei%C3%A7%C3%A3o-CST-do-IBS-CBS-informado-obriga-informa%C3%A7%C3%A3o-de-diferimento-Municipal-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:27Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Alíquotas de CBS", "Alíquotas de IBS", "Indicador de diferimento", "Grupo de divferimento para o IBS Municipal"]
---

# 1044 Rejeição: CST do IBS/CBS informado obriga informação de diferimento Municipal [nItem: 999]

**MENSAGEM**

1044 Rejeição: CST do IBS/CBS informado obriga informação de diferimento Municipal [nItem: 999]

**SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal (modelo 55) ou Nota Fiscal de Consumidor Eletrônica (modelo 65), o documento foi rejeitado pela SEFAZ porque foi utilizado um CST do IBS/CBS que exige a informação de diferimento Municipal, porém o grupo de diferimento não foi informado no documento fiscal.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique se o CST utilizado na operação que está gerando a rejeição.

**(2)** Confirme se o CST selecionado possui o **indicador de diferimento** (ind\_gDif) igual a 1, o que significa que este CST **exige a informação de diferimento**.

**(3)** Acesse a tela **''Produtos''** (Configurações » Cadastros » Produtos » Produtos) e verifique se o produto está configurado corretamente para a tributação do IBS Municipal.

**(4)** Acesse a tela de **"Tipos de Operação - TOP"** (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP) e verifique se a TOP utilizada na operação está configurada corretamente para o IBS Municipal.

**(5)** Na nota fiscal que está sendo emitida, acesse a aba "Impostos" e verifique se o grupo de IBS Municipal (gIBSMun) está sendo preenchido.

**(6)** Adicione o grupo de diferimento (gDif) dentro do grupo de IBS Municipal, informando:

- Percentual de diferimento (pDif): percentual do imposto que será diferido
- Valor do diferimento (vDif): valor calculado pela fórmula vDif = vBC x (pIBSMun / 100) x (pDif / 100)

**(7)** Verifique se o valor do diferimento (vDif) está sendo calculado corretamente, conforme a fórmula:

```
vDif = vBC x (pIBSMun / 100) x (pDif / 100).
```

**(8)** Após realizar as configurações necessárias, tente emitir a nota fiscal novamente.

**CAUSA**

Esta rejeição ocorre quando o CST do IBS/CBS utilizado na operação possui o **indicador de diferimento** (ind\_gDif) igual a 1, o que significa que este CST **exige a informação do grupo de diferimento** para o IBS Municipal, porém este grupo não foi informado no documento fiscal.

De acordo com a regra de validação UB40-10 da SEFAZ, quando o CST possui indicador que exige o uso de diferimento (ind\_gDif = 1), o grupo de Diferimento (gIBSMun/gDif) deve ser obrigatoriamente informado no documento fiscal. Caso contrário, a nota será rejeitada com o código 1044.

O diferimento é um mecanismo de postergação do pagamento do imposto para uma etapa posterior da cadeia de comercialização. Quando um CST exige diferimento, é necessário informar o percentual e o valor do diferimento para que a nota fiscal seja aceita pela SEFAZ.
