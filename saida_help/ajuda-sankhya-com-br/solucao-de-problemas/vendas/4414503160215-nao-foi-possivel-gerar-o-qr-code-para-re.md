---
id: "4414503160215"
titulo: "Não foi possível gerar o Qr code para recebimento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4414503160215-N%C3%A3o-foi-poss%C3%ADvel-gerar-o-Qr-code-para-recebimento"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:20:27Z"
rotulos: ["Configuração", "Contas", "Financeiro", "#validadoHugo", "PIX", "CORE_E06643", "Erro na autenticação do cliente Pix", "Preencha \"Senha do Cliente Pix\" e \"ID do Cliente Pix\"", "Verifique campos na tela \"Contas\"", "Erro"]
---

# Não foi possível gerar o Qr code para recebimento

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16203750656279) MENSAGEM:**

[CORE\_E06643] Não foi possível gerar o QR code para recebimento. Veja o erro. Erro ao realizar autenticação do cliente com a API 400 - Requisição com formato inválido.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16203750660119) SOLUÇÃO:**

Para a resolução do erro, preencha os campos **"Senha do Cliente Pix"** (CLIENT SECRET) e **"ID do Cliente Pix"** (CLIENTE ID), da aba **"Pix",** da tela **"Contas"** (Caminho de acesso: Configurações >> Cadastros >> Bancários >> Contas)**.**

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16203728066071) CAUSA:**

A não informação dos valores corretos para os campos Senha do Cliente Pix (CLIENT SECRET) e ID do Cliente Pix (CLIENTE ID), da aba Pix, da tela Configurações >> Cadastros >> Bancários >> Contas, ocasiona o erro mostrado acima, quando o usuário clica no botão Receber com Pix, da tela de baixa da Movimentação Financeira.
