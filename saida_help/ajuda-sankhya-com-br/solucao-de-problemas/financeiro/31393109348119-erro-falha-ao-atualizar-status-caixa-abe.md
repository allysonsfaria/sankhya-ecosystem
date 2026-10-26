---
id: "31393109348119"
titulo: "Erro: Falha ao atualizar status caixa aberto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31393109348119-Erro-Falha-ao-atualizar-status-caixa-aberto"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:33:16Z"
rotulos: ["Configuração", "Contas", "PDV", "Financeiro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Falha ao atualizar status caixa aberto", "Conta CAIXA", "Erro"]
---

# Erro: Falha ao atualizar status caixa aberto

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/31393109330327) **MENSAGEM:**

Erro: Falha ao atualizar status caixa aberto!

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31393125862423)SOLUÇÃO:**

Existem alguns motivos pelos quais o sistema pode não localizar uma conta durante o processo de abertura de caixa. Para identificar a causa, verifique os seguintes pontos:

#### **(1)** Configuração da Conta CAIXA (PDV)

- Certifique-se de que há uma conta cadastrada como **CAIXA (PDV);**
- A conta não deve ter um **Operador Exclusivo** ou, caso tenha, o usuário em questão deve estar vinculado como operador;
- Para verificar, acesse a tela **Contas** (Caminho: Configurações » Cadastros » Bancários » Contas) e confira os campos **Tipo de Conta** e **Operador Exclusivo**.

![Imagem 3: Para verificar, acesse a tela Contas ( Caminho: Configurações » Cadastros » Bancários » Contas ) e confira os campos…](https://ajuda.sankhya.com.br/hc/article_attachments/31393125863575)

#### **(1)** Vinculação da Empresa

- A empresa associada à conta **Caixa** do usuário deve ser a mesma vinculada ao seu cadastro e à operação de abertura do caixa;
- Para validar, acesse a tela **Contas** (Caminho: Configurações » Cadastros » Bancários » Contas) e confira os campos **Empresa** e **Exclusiva da Empresa**. Em seguida, acesse a tela **Usuários** (Configurações » Controle de Acesso » Usuários), selecione o usuário e verifique o campo **Empresa**.

![Imagem 4: Para validar, acesse a tela Contas ( Caminho: Configurações » Cadastros » Bancários » Contas ) e confira os campos…](https://ajuda.sankhya.com.br/hc/article_attachments/31393125864215)

![Imagem 5: Para validar, acesse a tela Contas ( Caminho: Configurações » Cadastros » Bancários » Contas ) e confira os campos…](https://ajuda.sankhya.com.br/hc/article_attachments/31393125867287)

#### **(1)** Restrições da Central de Certificações

- Verifique se há alguma regra na **Central de Certificações** que possa impedir a abertura do caixa, como bloqueio por empresa ou conta.

Se após essas verificações o problema persistir, recomenda-se acionar o suporte para uma análise mais detalhada.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/31393109337367)CAUSA:**

Ocorre quando há alguma restrição ou configuração pendente que impede a exibição de uma conta para seleção na abertura do CAIXA.
