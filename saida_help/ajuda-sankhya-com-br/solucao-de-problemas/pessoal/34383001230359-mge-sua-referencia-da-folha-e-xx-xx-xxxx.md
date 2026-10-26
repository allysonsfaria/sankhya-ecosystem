---
id: "34383001230359"
titulo: "MGE: Sua referência da folha é XX/XX/XXXX, não é permitido alterar dados do contrato com data inferior à da referência."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34383001230359-MGE-Sua-refer%C3%AAncia-da-folha-%C3%A9-XX-XX-XXXX-n%C3%A3o-%C3%A9-permitido-alterar-dados-do-contrato-com-data-inferior-%C3%A0-da-refer%C3%AAncia"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-08-18T19:55:11Z"
rotulos: ["Histórico", "Folha de Pagamento", "Configuração Funcionários", "Configurações Funcionários", "Erro", "Sua referência da folha", "não é permitido alterar dados do contrato", "data inferior à da referência", "tentar realizar alteração no cadastro do funcionário", "por meio do \"MGE\"", "Cadastro de Funcionários"]
---

# MGE: Sua referência da folha é XX/XX/XXXX, não é permitido alterar dados do contrato com data inferior à da referência.

**MENSAGEM**

Sua referência da folha é XX/XX/XXXX, não é permitido alterar dados do contrato com data inferior à da referência.

**SITUAÇÃO**

O erro é apresentado ao tentar realizar alteração no cadastro do funcionário por meio do **"MGE"**.

**SOLUÇÃO**

**(1)**  Acesse o cadastro do funcionário e verifique, na aba **"Histórico"**, se existe registro gravado na referência em que deseja realizar o ajuste.

**(2)**  Se existir, exclua o registro na tela **"Configurações Funcionários"** (Configurações » Cadastros » Pessoal » Configuração Funcionários), no **"Sankhya W"**.

**(3)**  Para isso, acesse a tela indicada, localize o funcionário e, na aba **"Histórico"**, exclua a informação gravada na referência em questão.

**Observação:**  essa tela está liberada caso tenha o **"Sankhya W"**.

**CAUSA**

O erro ocorre quando existe histórico registrado no cadastro do funcionário para a mesma referência utilizada no ajuste. Esse histórico é gravado automaticamente no fechamento da folha, mesmo que o funcionário não tenha cálculo na referência.
