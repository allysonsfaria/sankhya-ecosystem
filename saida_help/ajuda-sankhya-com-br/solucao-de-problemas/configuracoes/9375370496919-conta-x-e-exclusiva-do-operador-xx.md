---
id: "9375370496919"
titulo: "Conta x é exclusiva do operador XX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9375370496919-Conta-x-%C3%A9-exclusiva-do-operador-XX"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:08:20Z"
rotulos: ["Configuração", "Contas", "Segurança", "Movimentação Financeira", "Financeiro", "CORE_E01359"]
---

# Conta x é exclusiva do operador XX

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18588435918359) MENSAGEM:**

[CORE\_E01359]  Conta x é exclusiva do operador XX.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18588419318295) SITUAÇÃO:**

Ao tentar realizar a baixa de um título a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18588419323927) CAUSA:**

Usuário tentar usar conta caixa de outro usuário.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18588435934743) SOLUÇÃO:**

Quando de tratar de conta configurada como caixa (PDV) somente o operador exclusivo informado no cadastro dessa conta poderá utilizar a mesma. Para verificar se a conta utilizada é definida como conta caixa basta acessar a tela **Contas** (Configurações » Cadastros » Bancários » Contas) e verificar a configuração do campo "**Tipo de conta**".

Esse tipo de caixa Caixa (PDV) -  controla o "**Controle de Caixa**"

![Imagem 5: Esse tipo de caixa Caixa (PDV) - controla o " Controle de Caixa "](https://ajuda.sankhya.com.br/hc/article_attachments/18588435940631)

O campo **"Operador Exclusivo"** vincula um usuário à uma conta do Tipo **"Caixa (PDV)"**. Se informado, e o sistema for acessado por esse determinado usuário, o caixa será aberto automaticamente com a conta vinculada ao operador exclusivo e, ao sair do sistema, este emitirá uma mensagem perguntando se deseja fechar o caixa. Caso o usuário logado não possua nenhuma conta vinculada a ele, na abertura do caixa o campo para escolha da conta será apresentado desabilitado, porém com a tela de pesquisa para que o mesmo seja preenchido.

![Imagem 6: O campo "Operador Exclusivo" vincula um usuário à uma conta do Tipo "Caixa (PDV)" . Se informado, e o sistema for…](https://ajuda.sankhya.com.br/hc/article_attachments/9375383019159)

![Imagem 7: O campo "Operador Exclusivo" vincula um usuário à uma conta do Tipo "Caixa (PDV)" . Se informado, e o sistema for…](https://ajuda.sankhya.com.br/hc/article_attachments/9375413050775)

O usuário informado em Operador Exclusivo só poderá utilizar a conta a que estiver vinculado para fazer as movimentações de caixa. Cada usuário só poderá ser vinculado à uma conta.
