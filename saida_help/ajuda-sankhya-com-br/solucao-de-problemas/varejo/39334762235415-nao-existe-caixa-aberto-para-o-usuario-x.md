---
id: "39334762235415"
titulo: "Não existe caixa aberto para o usuário XXXX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39334762235415-N%C3%A3o-existe-caixa-aberto-para-o-usu%C3%A1rio-XXXX"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-09-18T19:34:25Z"
rotulos: ["Configuração", "Contas", "Movimentação Financeira", "Financeiro", "PDV Web", "\"%T.Nat\" (contribuição) \"%T.Rec\" (receitas) \"%T.Desp\" (despesas)", "Artigo criado KCS", "Varejo - KCS"]
---

# Não existe caixa aberto para o usuário XXXX

**MENSAGEM**

[COM\_E00853]: Não existe caixa aberto para o usuário XXXX

**SOLUÇÃO**

A mensagem é apresentada quando o usuário que está tentando realizar a venda no PDV Web não possui permissão de caixa.

Para solucionar esta pendência, verifique as configurações abaixo, caso o usuário em questão deva ser do tipo **Caixa.**

Acesse a tela **“Usuários”** (Configurações >> Controle de Acesso)

Busque pelo usuário que utiliza o **PDV Web** e verifique, na aba **“Identificação”**, se a opção **“Caixa”** está marcada.

Após isso, acesse a aba **“Contas p/ Baixa”** e vincule uma conta ao usuário.

![Imagem 1: Após isso, acesse a aba “Contas p/ Baixa” e vincule uma conta ao usuário.](https://ajuda.sankhya.com.br/attachments/token/A3tWNZDwgCHhrpiNzw5U2PyvB/?name=image.png)

Em seguida, acesse as **Configurações do Usuário** por meio do botão **“Outras Opções”**.

![Imagem 2: Em seguida, acesse as Configurações do Usuário por meio do botão “Outras Opções” .](https://ajuda.sankhya.com.br/attachments/token/rpzVLGnRRQtNYKxrfLiooBAAU/?name=image.png)

Será aberto um pop-up chamado **“Configurações do Usuário”**. No campo **“Número da conta padrão na baixa”**, deve estar vinculada a mesma conta informada anteriormente na aba **“Contas p/ Baixa”**.

**Importante:**

Após realizar essas configurações, será possível efetuar a **abertura e fechamento de caixa no PDV Web** normalmente.

**CAUSA**

Isso ocorre porque o sistema exige que o usuário esteja configurado como “Caixa”, com uma conta vinculada para movimentação financeira.  Quando essa configuração não está completa, o sistema interpreta que não há um caixa válido aberto, bloqueando a operação de venda.
