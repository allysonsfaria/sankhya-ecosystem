---
id: "37227148228631"
titulo: "E0682 Rejeição: O valor BC do Pis/Cofins não pode ser informado quando o valor de CST for igual a 0, 8 ou 9."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37227148228631-E0682-Rejei%C3%A7%C3%A3o-O-valor-BC-do-Pis-Cofins-n%C3%A3o-pode-ser-informado-quando-o-valor-de-CST-for-igual-a-0-8-ou-9"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:30Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Alíquotas de PIS", "Erro", "Código de Situação Tributária", "Alíquota de COFINS", "Base de Cálculo de PIS/COFINS", "Cadastro da alíquota de PIS e COFINS"]
---

# E0682 Rejeição: O valor BC do Pis/Cofins não pode ser informado quando o valor de CST for igual a 0, 8 ou 9.

**MENSAGEM**

E0682 Rejeição: O valor BC do Pis/Cofins não pode ser informado quando o valor de CST for igual a 0, 8 ou 9.

**SITUAÇÃO**

A nota fiscal eletrônica (NF-e ou NFC-e) foi emitida com a informação de Base de Cálculo de PIS/COFINS em uma operação registrada com Código de Situação Tributária que não contempla a incidência desses tributos, resultando na rejeição do documento.

**SOLUÇÃO**

Para resolver esta rejeição, é necessário **ajustar o cadastro da alíquota de PIS e COFINS** utilizada na operação, garantindo que a configuração esteja **compatível com o CST informado**. Siga os passos abaixo:

**(1)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas) e confirme as informações do produto.

**(2)** Na grade **''Itens''**, clique em **''Outras opções''** (ícones de três pontos) e selecione **''Consultar/Alterar Dados do Imposto do Item''**.

**(3)** Nas abas **''PIS''** e **''COFINS''**, verifique quais alíquotas estão sendo utilizadas no lançamento da nota fiscal de acordo com os seguintes campos:

- **Alíquota:** O percentual aplicado.
- **CST:** O Código de Situação Tributária utilizado (que muitas vezes define a alíquota).
- **Valor:** O valor calculado do imposto.

**(4)** Acesse a tela **"Alíquota de PIS"** (Configurações » Impostos » Alíquota de PIS) e localize o cadastro identificado no passo anterior.

**(5)** Verifique no campo **"Cód. sit. Tributária''** o código cadastrado. Se o CST estiver configurado como **0, 8 ou 9**, prossiga para o próximo passo.

**(6)** Consulte o **contador responsável** pela empresa para confirmar qual é o **CST correto** a ser utilizado na operação, considerando a natureza da transação e a legislação vigente.

**(7)**  Realize o ajuste necessário:

- **Se a operação realmente não possui tributação de PIS/COFINS** (CST 0, 8 ou 9): certifique-se de que os campos **"Alíquota PIS"** e **"Alíquota COFINS"** estejam zerados e que **não haja valor de Base de Cálculo** sendo informado no lançamento da nota.
- **Se a operação possui tributação de PIS/COFINS**: altere o **"Código de Situação Tributária"** **(CST)** para o código correto que represente a tributação aplicável (por exemplo, CST 01 para operação tributável com alíquota básica).

**(8)** Repita o processo para a tela **"Alíquota de COFINS"** (Configurações » Impostos » Alíquota de COFINS), realizando os mesmos ajustes identificados para o PIS.

**(9)** Após realizar os ajustes nos cadastros de alíquotas, **cancele a nota rejeitada** (se necessário) e **emita novamente** o documento fiscal com as configurações corretas.

**CAUSA**

A rejeição ocorre quando o sistema **envia informações de Base de Cálculo do PIS/COFINS** para a SEFAZ em operações onde o **"Código de Situação Tributária - CST"** está configurado como **0 (operação não tributada), 8 (operação isenta) ou 9 (operação sem incidência)**. Nesses casos, **não deve haver Base de Cálculo nem valores de PIS/COFINS**, pois a operação não está sujeita à tributação desses impostos. A inconsistência entre o CST informado e a presença de valores tributáveis gera a rejeição pela validação fiscal da SEFAZ.
