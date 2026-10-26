---
id: "37118339710743"
titulo: "Configuração da conta de baixa no processamento do arquivo de retorno."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37118339710743-Configura%C3%A7%C3%A3o-da-conta-de-baixa-no-processamento-do-arquivo-de-retorno"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-07-22T14:19:41Z"
rotulos: ["Configuração", "Contas", "Financeiro", "Arquivo de Retorno", "Processamento do Arquivo de Retorno", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Configuração da conta de baixa", "EDI Bancário"]
---

# Configuração da conta de baixa no processamento do arquivo de retorno.

Existem diferentes formas de definir a conta utilizada para a baixa durante o processamento do arquivo de retorno bancário, seguindo a seguinte hierarquia:

**1. Configuração via detalhe ou header no layout do arquivo de retorno**

A conta pode ser identificada diretamente no **header** ou no **detalhe** do arquivo, conforme as premissas e o layout definidos pelo banco, considerando as posições de agência e conta.

![Imagem 1: A conta pode ser identificada diretamente no header ou no detalhe do arquivo, conforme as premissas e o layout…](https://ajuda.sankhya.com.br/hc/article_attachments/37118339695767)

**2. Configuração pela tela de Contas**

**(1)** Acesse a tela [**''Contas''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas) (Configurações » Cadastros » Bancários » Contas).

**(2)** Na aba **''Intercâmbio Eletrônico de Dados (EDI)''**, no campo **''Conta p/ baixa (Processamento de Retorno)''** configure a conta de baixa.

![Imagem 2: (2) Na aba ''Intercâmbio Eletrônico de Dados (EDI)'' , no campo ''Conta p/ baixa (Processamento de Retorno)'' configure…](https://ajuda.sankhya.com.br/hc/article_attachments/37118367532055)

- Nesse cenário, todos os títulos vinculados a essa conta serão baixados exclusivamente na conta informada nesse campo, essa configuração sobrepõe a configuração acima.

**3. Configuração direta no layout do arquivo de retorno (prioritária)**

**(1)** Acesse a tela [**''Configuração Arquivo de Retorno''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111033-Configura%C3%A7%C3%A3o-Arquivo-de-Retorno) (Financeiro » EDI Bancário » Configuração Arquivo de Retorno).

**(2)** Clique em **''Outras Opções''** (ícone com três pontos) e selecione **''Configuração de Ocorrências de Retorno''**.

![Imagem 3: (2) Clique em ''Outras Opções'' (ícone com três pontos) e selecione ''Configuração de Ocorrências de Retorno'' .](https://ajuda.sankhya.com.br/hc/article_attachments/37278089601943)

**(3)** Marque a opção **''Alterar''**.

**(4)** No campo **''Conta Bancária''** informe o código da conta bancária que deverá ser utilizada na baixa

- Esta configuração tem prioridade sobre todas as anteriores.

![Imagem 4: Esta configuração tem prioridade sobre todas as anteriores.](https://ajuda.sankhya.com.br/hc/article_attachments/37118339699607)

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/37118339701783)CAUSA:**

O erro ocorre quando o sistema não consegue identificar automaticamente a conta bancária para a baixa durante o processamento do arquivo de retorno ou quando é necessária a alteração manual da conta de baixa informada.
