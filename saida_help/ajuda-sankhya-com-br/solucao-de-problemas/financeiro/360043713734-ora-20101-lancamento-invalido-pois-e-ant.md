---
id: "360043713734"
titulo: "ORA-20101: Lançamento inválido, pois é anterior à data de partida do controle de saldos da conta."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043713734-ORA-20101-Lan%C3%A7amento-inv%C3%A1lido-pois-%C3%A9-anterior-%C3%A0-data-de-partida-do-controle-de-saldos-da-conta"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-10-02T15:51:58Z"
rotulos: ["Configuração", "Contas", "Movimentação Financeira", "Financeiro", "ORA-20101", "Lançamento anterior à data", "Movimentações financeiras inválidas", "Atualizar referência em Contas", "Erro"]
---

# ORA-20101: Lançamento inválido, pois é anterior à data de partida do controle de saldos da conta.

**![Imagem 1: MENSAGEM](https://ajuda.sankhya.com.br/hc/article_attachments/16201004191383) MENSAGEM**

ORA-20101: Lançamento inválido, pois é anterior à data de partida do controle de saldos da conta.

**![Imagem 2: SITUAÇÃO](https://ajuda.sankhya.com.br/hc/article_attachments/16200959123735) SITUAÇÃO**

Ao tentar efetuar um lançamento bancário, baixar um titulo financeiro, ocorre a mensagem.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16201004197655) CAUSA:**

Ocorre ao tentar realizar movimentações financeiras e bancárias para determinada conta, com data anterior a **"Referência para aceitar lançamentos"**.

**![Imagem 4: SOLUÇÃO](https://ajuda.sankhya.com.br/hc/article_attachments/16201004194455) SOLUÇÃO**

Acesse a  tela **Contas** (Configurações » Cadastros » Bancários » Contas), selecione a conta utilizada na movimentação, botão: **"Outras Opções"** » "**Implanta Saldo Bancário"** deverão ser inseridos os saldos bancário e Real e sua respectiva Referência:

![Imagem 5: Acesse a tela Contas (Configurações » Cadastros » Bancários » Contas), s elecione a conta utilizada na movimentação,…](https://ajuda.sankhya.com.br/hc/article_attachments/14625848511255)

A Referência inserida nessa implantação será utilizada para permitir as movimentações dessa conta bancária.

- Com a implantação do saldo feita em **01/03/2023**, os lançamentos só serão aceitos a partir desta data, onde ao informar um período anterior o erro será apresentado.

Caso a referência ou saldo foram inseridos incorretamente, uma nova implantação pode ser realizada, contudo na aba **Saldos** a 'Correção Saldo Banco' deverá ser realizada, de forma a  recompor os saldos, considerando a referência mais antiga.  Esse procedimento deve ser realizado por um usuário com conhecimento sobre a rotina.
