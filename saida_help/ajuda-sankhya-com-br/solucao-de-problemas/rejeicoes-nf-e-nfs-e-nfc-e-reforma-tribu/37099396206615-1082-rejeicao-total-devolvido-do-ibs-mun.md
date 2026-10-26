---
id: "37099396206615"
titulo: "1082 Rejeição: Total Devolvido do IBS Municipal difere da soma dos itens"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37099396206615-1082-Rejei%C3%A7%C3%A3o-Total-Devolvido-do-IBS-Municipal-difere-da-soma-dos-itens"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:47Z"
rotulos: ["Configuração", "NF-e", "Impostos", "TOP", "Passos para resolver", "Erro", "Código de Situação Tributária", "Alíquotas de IBS", "IBS Municipal", "Como resolver", "Soma dos valores devolvidos", "Soma dos valores devolvidos de IBS Municipal", "Valor total devolvido de IBS Municipal"]
---

# 1082 Rejeição: Total Devolvido do IBS Municipal difere da soma dos itens

**MENSAGEM**

1082 Rejeição: Total Devolvido do IBS Municipal difere da soma dos itens

**SITUAÇÃO**

Foi identificada inconsistência entre o **valor total devolvido de IBS Municipal informado na NF-e** e a **soma dos valores devolvidos de IBS Municipal** nos respectivos itens do documento.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Tipos de Operação - TOP''** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

**(2)** Verifique a configuração do TOP utilizado na operação de devolução, garantindo que esteja corretamente configurado para operações de devolução

**(3)** Acesse a tela de **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e/ou **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

**(4)** Verifique se as alíquotas do **IBS Municipal** estão corretamente configuradas para os produtos envolvidos na operação de devolução.

**(5)** Confira se o **Código de Situação Tributária (CST)** utilizado para o **IBS** e a **CBS** é compatível com operações de devolução.

- Certifique-se de que o CST selecionado permite a devolução dos valores do **IBS Municipal**, conforme a natureza da operação.

**(6)** Verifique os valores do **IBS Municipal** informados em cada item da nota fiscal de devolução, garantindo que:

- A **base de cálculo** esteja corretamente definida;
- A **alíquota aplicada** corresponda à utilizada na operação original;
- O **valor do IBS Municipal** esteja corretamente calculado para cada item.

**(7)** Recalcule manualmente o valor total do **IBS Municipal** devolvido, realizando a soma dos valores apurados em cada item da nota fiscal, e compare o resultado com o valor total do imposto informado no documento.

**(8)** Após concluir as verificações e realizar as correções necessárias, gere novamente o documento fiscal para que o sistema recalcule automaticamente os valores do **IBS Municipal**, considerando as configurações atualizadas.

**CAUSA**

A rejeição ocorre devido a uma inconsistência no cálculo do valor total devolvido do IBS Municipal. Esta inconsistência pode ser causada por:

- Erro no cálculo automático do sistema ao somar os valores de IBS Municipal de cada item;
- Alteração manual dos valores de IBS Municipal em um ou mais itens sem atualização do valor total;
- Arredondamentos incorretos nos cálculos dos valores individuais ou do total;
- Configuração inadequada das alíquotas do IBS Municipal para operações de devolução;
- Utilização de CST incompatível com operações de devolução de valores do IBS Municipal;
- Divergência entre a base de cálculo utilizada na operação original e na devolução.
