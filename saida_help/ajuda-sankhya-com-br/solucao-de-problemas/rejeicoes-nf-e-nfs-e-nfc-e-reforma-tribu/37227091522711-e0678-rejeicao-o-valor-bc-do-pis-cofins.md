---
id: "37227091522711"
titulo: "E0678 Rejeição: O valor BC do Pis/Cofins deve ser informado quando o CST for diferente de 0, 8 ou 9."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37227091522711-E0678-Rejei%C3%A7%C3%A3o-O-valor-BC-do-Pis-Cofins-deve-ser-informado-quando-o-CST-for-diferente-de-0-8-ou-9"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:31Z"
rotulos: ["Configuração", "NF-e", "Central de Vendas", "SEFAZ", "Alíquotas de COFINS", "Impostos", "Alíquotas de PIS", "CST de PIS/COFINS for diferente de 0 8 ou 9", "Código de Situação Tributária de PIS/COFINS"]
---

# E0678 Rejeição: O valor BC do Pis/Cofins deve ser informado quando o CST for diferente de 0, 8 ou 9.

**MENSAGEM**

E0678 Rejeição: O valor BC do Pis/Cofins deve ser informado quando o CST for diferente de 0, 8 ou 9.

**SITUAÇÃO**

A NF-e ou NFC-e foi emitida com um Código de Situação Tributária de PIS/COFINS informado, sem o preenchimento do valor da base de cálculo correspondente no documento fiscal ou com esse valor registrado como zero.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

**(2)** Na grade **''Itens''**, clique em **''Outras Oções'' (ícone com três pontos)** e selecione **''Consultar/Alterar Dados do Imposto do Item''**.

**(3)** Nas abas **''PIS''** e **''COFINS''**, verifique o Código de Situação Tributária que está sendo utilizado no lançamento da nota fiscal.

**(4)** Confirme com o **setor fiscal ou contador** da empresa se o CST informado está correto para a operação que está sendo realizada.

**(5)** Caso o CST esteja correto e seja diferente de **0 (zero), 8 (oito) ou 9 (nove)**, certifique-se de que a **base de cálculo do PIS/COFINS** está sendo informada corretamente. Verifique se:

- O **valor da base de cálculo** foi preenchido nos campos de PIS e COFINS do item da nota;
- Acesse as telas **''Alíquotas de PIS''** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de PIS) e **''Alíquotas de COFINS''** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de COFINS) e verifique a configuração da alíquota de PIS/COFINS.
- Acesse a tela **''Empresa''** (Comercial » Preferências » Empresa), na aba **''Propriedades''** verifique se o cálculo de PIS/COFINS estão configuradas corretamente.

**(6)** Se o lançamento foi realizado **manualmente**, preencha todos os campos obrigatórios de PIS/COFINS, incluindo:

- **"CST de PIS"** e **"CST de COFINS"**;
- **"Base de Cálculo PIS"** e **"Base de Cálculo COFINS"**;
- **"Alíquota PIS"** e **"Alíquota COFINS"**;
- **"Valor PIS"** e **"Valor COFINS"**.

**(7)** Se o lançamento utiliza **configuração automática** de impostos, acesse as telas **''Alíquotas de PIS''** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de PIS) e **''Alíquotas de COFINS''** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de COFINS) e certifique-se de que:

- O **"Código de Situação Tributária"** (CST) está correto;
- Os campos **"Alíquota PIS"** e **"Alíquota COFINS"** estão preenchidos;
- O **"Tipo"** da alíquota (Entrada ou Saída) está compatível com a operação.

**(8)** Após realizar os ajustes necessários, **reemita a nota fiscal** para que as informações sejam enviadas corretamente à SEFAZ. 

**CAUSA**

A rejeição ocorre porque a **SEFAZ exige** que, quando o **CST de PIS/COFINS for diferente de 0, 8 ou 9**, o valor da **base de cálculo desses impostos seja obrigatoriamente informado** no documento fiscal. A ausência ou o preenchimento incorreto deste valor impede a validação e aprovação da nota fiscal eletrônica.
