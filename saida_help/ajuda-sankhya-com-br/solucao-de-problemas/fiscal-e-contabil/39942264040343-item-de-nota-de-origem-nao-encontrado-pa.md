---
id: "39942264040343"
titulo: "Item de nota de origem não encontrado para NUNOTA:x   SEQUENCIA: x"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39942264040343-Item-de-nota-de-origem-n%C3%A3o-encontrado-para-NUNOTA-x-SEQUENCIA-x"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T13:27:57Z"
rotulos: ["NF-e", "Impostos", "TOP", "Estoque", "Erro", "Alíquotas de CBS", "Alíquotas de IBS", "impostos nota de perda"]
---

# Item de nota de origem não encontrado para NUNOTA:x   SEQUENCIA: x

**MENSAGEM**

Item de nota de origem não encontrado para NUNOTA: x SEQUENCIA: x

**SITUAÇÃO**

A mensagem é apresentada ao tentar adicionar um item em uma nota fiscal de perda de estoque utilizando uma **"TOP"** (Comercial Arquivo Cadastros Tipos de Operação - TOP) de baixa de estoque que contempla os novos impostos da reforma tributária (IBS e CBS). O sistema não consegue localizar o item de origem referenciado pela nota fiscal, impedindo a conclusão da operação.

**SOLUÇÃO**

**(1)**
Verifique se a nota fiscal de origem está devidamente confirmada no sistema.
Acesse a tela **"Central de Vendas"** (Comercial » Consulta) e localize
a nota referenciada pelo número único.

**(2)**
Confirme se o item de sequência citada existe na nota de origem e se está com o status
correto. Verifique se não houve exclusão ou alteração do item após o lançamento
inicial.

**(3)**
Valide as configurações da **"TOP"** (Comercial Arquivo Cadastros
Tipos de Operação - TOP) utilizada na operação de perda de estoque. Verifique:

- Se a aba **"NF-e/NFC-e/CF-e"** está configurada corretamente.
- Se os campos de cálculo de impostos (ICMS, PIS, COFINS, IBS, CBS) estão habilitados.
- Se a TOP está configurada para operações de baixa de estoque.

**(4)**
Verifique se os valores de IBS e CBS do item na nota de perda não excedem os valores
informados na nota de origem. O sistema valida se o valor de IBS e CBS da operação
não é maior que o valor do item na nota de origem.

**(5)**
Se o produto possui controle de estoque por lote, confirme se os lotes estão corretamente
informados e se há saldo disponível no lote referenciado.

**(6)**
Caso o erro persista, realize uma nova tentativa de lançamento da nota fiscal.

**(7)**
Se necessário, consulte o setor fiscal da empresa para validar se a operação de
perda de estoque está sendo realizada conforme as regras da reforma tributária.

**CAUSA**

O erro ocorre quando o sistema não consegue localizar o item de origem referenciado na operação de perda de estoque. As principais causas são:

**1. Nota de origem não confirmada:** A nota fiscal que originou o item não está devidamente confirmada no sistema ou foi excluída.
**2. Item inexistente ou alterado:** O item de sequência informado não existe na nota de origem ou foi modificado após o lançamento inicial.
**3. Configuração inadequada da TOP:** A **"TOP"** (Comercial Arquivo Cadastros Tipos de Operação - TOP) utilizada não está configurada corretamente para operações de baixa de estoque com os novos impostos IBS e CBS.
**4. Validação de impostos IBS/CBS:** Os valores de IBS e CBS informados na operação de perda excedem os valores registrados na nota de origem.
**5. Inconsistência no controle de lotes:** Pode haver inconsistência entre os lotes informados e os lotes disponíveis no estoque de origem.
