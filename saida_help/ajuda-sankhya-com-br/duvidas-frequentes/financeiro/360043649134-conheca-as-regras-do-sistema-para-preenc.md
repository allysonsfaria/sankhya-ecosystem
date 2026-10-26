---
id: "360043649134"
titulo: "Conheça as regras do sistema para preenchimento da informação 'Conta Bancária' da aba 'Financeiro' das centrais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043649134-Conhe%C3%A7a-as-regras-do-sistema-para-preenchimento-da-informa%C3%A7%C3%A3o-Conta-Banc%C3%A1ria-da-aba-Financeiro-das-centrais"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-07-22T16:01:03Z"
rotulos: ["#PUBLIFER", "Configuração", "Contas", "Parceiro", "Preferências", "Financeiro", "Tipo de Negociação: Verifique banco e conta", "Parceiros: Verifique conta bancária empresa", "Preferências: Confira conta padrão", "Artigo atualizado KCS", "Financeiro - KCS"]
---

# Conheça as regras do sistema para preenchimento da informação 'Conta Bancária' da aba 'Financeiro' das centrais

**(1)** Verifique se existe conta bancária vinculada na aba parcelas do tipo de negociação utilizado:

- Tela [**"Tipos de Negociação"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173) (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipo de Negociação), aba **Parcelas**:
  Campo **"Banco"**
  Campo **"Conta Bancária"**

![Imagem 1: Tela "Tipos de Negociação" (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipo de Negociação), aba Parcelas :…](https://ajuda.sankhya.com.br/hc/article_attachments/14556449271319)

Caso as informações acima não estejam preenchidas, siga para a próxima análise:

**(2)** Tela **"Preferências"** (Configurações >> Avançado >> Preferências):

- Chave **"CONTAPADRAOFIN"**

![Imagem 2: Chave "CONTAPADRAOFIN"](https://ajuda.sankhya.com.br/hc/article_attachments/12299566695703)

Caso a informação acima não esteja preenchida, siga para a próxima análise:

**(3)** Tela **"Parceiros"** (Configurações » Cadastros » Parceiros), aba **Identificação**:

- Campo **"Conta bancária empresa"**

Caso a informação acima não esteja preenchida, siga para a próxima análise:

**(4)** Verifique se existe **'Banco'** vinculado na aba parcelas do tipo de negociação.
Em caso positivo, verifique na tela [**"Contas"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113) se existe alguma conta vinculada para esse banco marcada como **"Conta padrão para emissão"**. Quando existir mais de uma conta nessa situação, para esse banco, será utilizada a de menor código, preferindo a conta que seja exclusiva da empresa, mas aceitando contas não exclusivas.

**OBSERVAÇÃO:**

**(2)** Caso a conta esteja marcada para emitir boleto (**Configurações » Cadastros » Bancários » Contas, aba Boleto(s)/Duplicatas,**campo **"Emite"** = SIM, o sistema somente seguirá essa regra caso o tipo de negociação esteja marcado o campo **"Imprimir boleto/duplicata?"** disponível no tipo de negociação esteja como: manual ou na confirmação.

**(2)** Se no tipo de negociação estiver proibido, a conta bancária deverá estar com o campo: 'emite' = desmarcado.

**(5)** Se a conta não for preenchida pelos requisitos acima o sistema verifica na tela Contas se existe alguma conta marcada como **"Exclusiva da empresa"** e vinculada para a respectiva empresa do lançamento.

**(6)** Se nenhuma das opções acima atender o preenchimento, o financeiro da nota não terá informações bancárias.
