---
id: "34316381239447"
titulo: "Para abrir um novo caixa no PDV Web, é necessário fechar o caixa atual. Deseja fechar este caixa agora?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34316381239447-Para-abrir-um-novo-caixa-no-PDV-Web-%C3%A9-necess%C3%A1rio-fechar-o-caixa-atual-Deseja-fechar-este-caixa-agora"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-07-22T14:27:17Z"
rotulos: ["Configuração", "Caixa", "Operação", "PDV Web", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "Deseja fechar este caixa agora", "Para abrir um novo caixa no PDV Web", "é necessário fechar o caixa atual"]
---

# Para abrir um novo caixa no PDV Web, é necessário fechar o caixa atual. Deseja fechar este caixa agora?

**MENSAGEM**

O PDV 'XXXXXXX' foi aberto em XXXX-XX-XX XX:XX:XX com a conta X pelo usuário XXXXX. Para abrir um novo caixa no PDV Web, é necessário fechar o caixa atual. Deseja fechar este caixa agora? 
**Atenção:** Caso selecione **'Não'**, a tela será fechada e a operação cancelada.

**SITUAÇÃO**

O sistema exibe esta mensagem quando identifica que já existe uma sessão de caixa aberta para o terminal de PDV utilizado. Isso ocorre ao tentar abrir um novo caixa no PDV Web sem que o caixa anterior tenha sido devidamente encerrado.

**SOLUÇÃO**

Para abrir um novo caixa, encerre a sessão anterior conforme o passo a passo:

**(1)**  Na tela do aviso, clique em **'Sim'**.

- Ao selecionar **'Sim'**, o sistema reconhece a intenção de fechar o caixa em aberto e direciona para a tela de **"Funções de Caixa".**

![Imagem 1: Na tela de "Funções de Caixa" , preencha os dados necessários para o fechamento.](https://ajuda.sankhya.com.br/hc/article_attachments/34316381216919)

**(2)**  Na tela de **"Funções de Caixa"**, preencha os dados necessários para o fechamento.

- Confirme o fechamento para encerrar a sessão anterior.
- O sistema exibirá a mensagem de confirmação do fechamento.

![Imagem 2: Após o fechamento, realize a abertura do novo caixa.](https://ajuda.sankhya.com.br/hc/article_attachments/34316381217943)

**(3)**  Após o fechamento, realize a abertura do novo caixa.

- O sistema apresentará um pop-up de **"Abertura de Caixa"**.

![Imagem 3: O sistema apresentará um pop-up de "Abertura de Caixa" .](https://ajuda.sankhya.com.br/hc/article_attachments/34316387316503)

- Clique no botão **"Abrir Caixa"** e siga o procedimento padrão para iniciar a nova sessão de caixa no PDV Web.

(1)** Importante:** se clicar em **'Não'** no aviso inicial, a tela de login será fechada e a operação cancelada. Será necessário tentar logar novamente para visualizar o aviso e seguir o procedimento de fechamento.

**CAUSA**

O aviso é apresentado porque já existe uma sessão de caixa aberta para o terminal de PDV utilizado. O sistema impede a abertura de duas sessões simultâneas para o mesmo PDV, garantindo a integridade financeira e evitando conflitos de operação.
