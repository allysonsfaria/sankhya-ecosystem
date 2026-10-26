---
id: "34455169335959"
titulo: "Aviso: Este caixa será aberto pelo Gerente XX-PDVID os movimentos serão registrados pelo gerente XX-PDVID"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34455169335959-Aviso-Este-caixa-ser%C3%A1-aberto-pelo-Gerente-XX-PDVID-os-movimentos-ser%C3%A3o-registrados-pelo-gerente-XX-PDVID"
trilha: "Melhores Práticas > Varejo"
atualizado_em: "2026-07-22T14:27:04Z"
rotulos: ["Configuração", "Segurança", "Financeiro", "PDV Web", "Erro", "Este caixa será aberto pelo Gerente XX-PDVID", "Abertura de Caixa", "os movimentos serão registrados pelo gerente XX-PDVID", "Gerente do Financeiro", "Gerente de Caixa"]
---

# Aviso: Este caixa será aberto pelo Gerente XX-PDVID os movimentos serão registrados pelo gerente XX-PDVID

**MENSAGEM**

Este caixa será aberto pelo Gerente XX-PDVID os movimentos serão registrados pelo gerente XX-PDVID

**SITUAÇÃO**

Ao acessar a tela **“PDV WEB”** e iniciar o processo de **“Abertura de Caixa”**, a mensagem é exibida quando o usuário está configurado simultaneamente como **“Gerente do Financeiro”** e **“Gerente de Caixa”**.

**SOLUÇÃO**

**(1)**  Acesse o cadastro do usuário **“Usuários”** (Configurações » Controle de Acesso » Usuários);

**(2)**  Localize a aba **“Segurança”** e as opções **“Gerente do Financeiro”** e **“Gerente de Caixa”;**

**(3)**  Desmarque as opções **“Gerente do Financeiro”** e **“Gerente de Caixa”;**

**(4)**  Salve as alterações e tente novamente abrir o caixa no **“PDV WEB”**. A mensagem não será mais apresentada.

![Imagem 1: (1) Acesse o cadastro do usuário “Usuários” (Configurações » Controle de Acesso » Usuários); (2) Localize a aba…](https://ajuda.sankhya.com.br/hc/article_attachments/35006570903575)

**CAUSA**

A mensagem é apresentada porque o sistema não permite que o mesmo usuário possua simultaneamente as permissões de **“Gerente do Financeiro”** e **“Gerente de Caixa”**, evitando conflitos de acesso e operação no processo de abertura de caixa.
