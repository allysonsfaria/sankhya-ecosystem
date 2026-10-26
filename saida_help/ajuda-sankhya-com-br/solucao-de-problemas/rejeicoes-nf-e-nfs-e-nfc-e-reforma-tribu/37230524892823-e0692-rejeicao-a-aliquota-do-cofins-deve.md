---
id: "37230524892823"
titulo: "E0692 Rejeição: A alíquota do Cofins deve ser igual ou maior que 0 e menor ou igual a 100%."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37230524892823-E0692-Rejei%C3%A7%C3%A3o-A-al%C3%ADquota-do-Cofins-deve-ser-igual-ou-maior-que-0-e-menor-ou-igual-a-100"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:13:46Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "Impostos", "Código de Situação Tributária (CST)", "Valor de alíquota do COFINS", "Alíquota COFINS", "Deve ser igual ou maior que 0 e menor ou igual a 100%"]
---

# E0692 Rejeição: A alíquota do Cofins deve ser igual ou maior que 0 e menor ou igual a 100%.

**MENSAGEM**

E0692 Rejeição: A alíquota do Cofins deve ser igual ou maior que 0 e menor ou igual a 100%.

**SITUAÇÃO**

Ao emitir uma Nota Fiscal Eletrônica (NF-e), o sistema retorna uma rejeição relacionada ao valor da **alíquota do COFINS** informado no documento fiscal.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Alíquotas de COFINS''** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de COFINS) e localiza a rega de alíquota que está sendo utilizada na operação fiscal.

**(2)** Verifque se o campo **''Alíquota''** está informado com **valores entre 0 e 100**. Caso o valor esteja incorreto, ajuste para um percentual válido conforme a legislação vigente:

- Para operações com **incidência cumulativa**, a alíquota padrão é **3,00%**.
- Para operações com **incidência não-cumulativa**, a alíquota padrão é **7,60%**.
- Para operações **sem incidência** ou com **alíquota zero**, informe **0%**.

**(3)** Caso a operação seja **isenta, não tributada ou com suspensão**, verifique se o campo **"Cód. sit. tributária"** está configurado corretamente.

**(4)** Mesmo que a incidência seja **zero**, é necessário criar uma alíquota com **valor 0%** para que os dados de COFINS sejam gerados corretamente no XML da NF-e no momento da confirmação/aprovação.

**(5)** Após realizar os ajustes **salve as alterações.**

**(6)** Retorne à **Nota Fiscal** e **redigite os itens** ou **relance a nota** para que as novas configurações sejam aplicadas.

**(7)** Gere novamente o **lote de transmissão** e busque a **autorização da SEFAZ**.

**CAUSA**

A rejeição ocorre porque o sistema enviou para a SEFAZ um **valor de alíquota do COFINS inválido**, ou seja, **menor que 0% ou maior que 100%**. Isso pode acontecer devido a:

- **Erro no cadastro de alíquotas:** o campo **"Alíquota COFINS (%)"** foi preenchido com um valor fora do intervalo permitido.
- **Configuração incorreta do CST:** o **Código de Situação Tributária** do COFINS não está adequado à operação fiscal.
- **Falta de alíquota cadastrada:** não existe uma alíquota de COFINS configurada para a operação, fazendo com que o sistema envie um valor nulo ou inválido.
- **Inconsistência nos cálculos:** problemas no rateio proporcional ou na base de cálculo podem gerar valores incorretos de alíquota.
