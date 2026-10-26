---
id: "43547972277911"
titulo: "Erro E160: Não foi possível resolver IBS/CBS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43547972277911-Erro-E160-N%C3%A3o-foi-poss%C3%ADvel-resolver-IBS-CBS"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-10-08T21:37:08Z"
rotulos: ["Artigo criado KCS", "Fiscal/Contábil - KCS"]
---

# Erro E160: Não foi possível resolver IBS/CBS

**MENSAGEM**

**Código: E160 – Descrição: Não foi possível resolver IBS/CBS: cliente, competência, CST e cClassTrib devem ser informados**

**SITUAÇÃO**

A mensagem de erro **"Código: E160 – Descrição: Não foi possível resolver IBS/CBS: cliente, competência, CST e cClassTrib devem ser informados"** ocorre durante o processo de emissão de notas fiscais eletrônicas no Sankhya, especialmente ao tentar calcular ou validar os tributos referentes à reforma tributária (IBS e CBS).

**SOLUÇÃO**

Para solucionar o erro, siga o passo a passo abaixo:

**(1)** Acesse a tela **"Serviços"** em **Configurações → Cadastros → Serviços**.

**(2)** Localize e acesse o cadastro do serviço utilizado na nota fiscal. Na aba **"Impostos"**, localize os campos **"Código de Tributação Nacional"** e **"Código Indicador de Operação"**.

**(3)** Preencha os campos de acordo com a tributação aplicável ao serviço e com o cenário da operação.

**(4)** Após realizar o preenchimento, retorne à **Central de Vendas** e redigite a quantidade do item do serviço para que as alterações realizadas no cadastro sejam atualizadas na nota.

**(5)** Em seguida, gere o lote novamente e utilize a opção **"Buscar Autorização"**.

Após a atualização das informações, a nota deverá ser processada novamente e, estando as demais configurações corretas, poderá ser autorizada normalmente.

> **Observação:** Os códigos devem ser informados conforme o enquadramento tributário do serviço e as regras vigentes para IBS/CBS. Em caso de dúvidas sobre qual código utilizar, valide a classificação tributária aplicável ao serviço antes de realizar o preenchimento.

**CAUSA**

O erro **E160** ocorre quando o sistema não consegue resolver as informações necessárias para o cálculo do **IBS/CBS** devido à ausência de dados tributários no cadastro do serviço.

Na maioria dos cenários, os campos **"Código de Tributação Nacional"** e **"Código Indicador de Operação"**, localizados na aba **Impostos** do cadastro do serviço, estão sem preenchimento.

A ausência dessas informações impede que o sistema identifique corretamente os dados necessários para a tributação de IBS/CBS, ocasionando a mensagem:

**"Código: E160 – Descrição: Não foi possível resolver IBS/CBS: cliente, competência, CST e cClassTrib devem ser informados."**

Após o preenchimento dos campos e a atualização do item na Central de Vendas, deve-se gerar o lote novamente e a ação **"Buscar Autorização"** resulta na **aprovação da nota**.
