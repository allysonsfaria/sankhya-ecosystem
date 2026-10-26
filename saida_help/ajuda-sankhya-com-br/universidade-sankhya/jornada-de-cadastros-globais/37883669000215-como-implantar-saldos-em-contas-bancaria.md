---
id: "37883669000215"
titulo: "Como implantar saldos em contas bancárias"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37883669000215-Como-implantar-saldos-em-contas-banc%C3%A1rias"
trilha: "Universidade Sankhya > Jornada de Cadastros Globais"
atualizado_em: "2026-08-09T20:55:12Z"
rotulos: ["Configuração", "Contas", "Movimentação Financeira", "Atualização", "Financeiro"]
---

# Como implantar saldos em contas bancárias

## Qual a importância da implantação de saldos em contas bancárias?

A implantação de saldos é necessária para iniciar as movimentações financeiras no sistema, informando os valores encontrados nas contas da empresa já cadastradas. Este processo serve como ponto de partida para o controle de saldos no sistema.
Após a implantação, o sistema começará a controlar os saldos, onde o saldo real será atualizado com as baixas e o saldo bancário com as conciliações.

**Boas Práticas:**

- Implante saldo inicial **0,00** para todas as contas antes do mês de início de uso.
- Para implantação de saldos, use a funcionalidade "Implantar Saldo Bancário" no menu "**Outras Opções**".
- Crie uma conta específica para implantação de saldos quando necessário.

#### Vídeo de demonstração prática no sistema de como implantar saldos nas contas bancárias

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/838797631)

#### Siga o passo a passo para implantar saldos nas contas bancárias em sua base

Tela **Implantação dos Saldos e Contas**

1. Acesse a tela **Implantação dos Saldos e Contas**

**Menu:** Financeiro » Arquivos » Cadastros » Implantação dos Saldos de Contas

2. Localize a conta bancária

- No modo **Grade**, selecione a conta bancária desejada para inserir o saldo.

3. Insira o saldo bancário

- Após selecionar a conta, dê um duplo clique sobre a linha correspondente.
- Preencha os seguintes campos:

  - **Referência p/ Aceitar Lançamentos**: data a partir da qual o sistema aceitará movimentações na conta.
  - **Saldo do Banco na Referência**: valor do saldo registrado no extrato bancário.
  - **Saldo Real na Referência**: valor real disponível da conta considerando movimentações já previstas.

4. Finalize o cadastro

- Clique no botão **Salvar** para concluir a implantação do saldo.

Tela **Contas**

1. Acesse a tela **Contas**

**Menu:** Configurações » Cadastros » Bancários » Contas

2. Localize a conta bancária

- Acesse o modo **Grade**.
- Clique em **Atualizar** para carregar as informações disponíveis.

3. Insira o saldo bancário

- Selecione a **conta bancária desejada**.
- Clique no botão **Outras opções** e selecione **Implanta Saldo Bancário**.
- Preencha os campos obrigatórios:

  - **Referência p/ Aceitar Lançamentos**: define a data inicial para início dos lançamentos.
  - **Saldo do Banco na Referência**: valor registrado conforme o extrato do banco.
  - **Saldo Real na Referência**: valor efetivo disponível, considerando previsões de movimentações.

4. Finalize o processo

- Clique no botão **Salvar** para concluir a implantação.

#### Observações importantes

- Os saldos informados não poderão ser alterados após salvos.
- O sistema aceita data retroativa máxima de 12 meses.
- Os saldos bancário e real devem ser iguais na implantação.
- Boa prática: implantar saldo 0,00 em data anterior ao mês inicial de uso.
- Ao salvar, o sistema sempre considerará o primeiro dia do mês escolhido.
