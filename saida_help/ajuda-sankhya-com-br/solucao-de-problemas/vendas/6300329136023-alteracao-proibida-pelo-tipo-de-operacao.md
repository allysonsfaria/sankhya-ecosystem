---
id: "6300329136023"
titulo: "Alteração proibida pelo Tipo de Operação (TOP) ou o usuário não tem autorização para alterar nota fiscal confirmada."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/6300329136023-Altera%C3%A7%C3%A3o-proibida-pelo-Tipo-de-Opera%C3%A7%C3%A3o-TOP-ou-o-usu%C3%A1rio-n%C3%A3o-tem-autoriza%C3%A7%C3%A3o-para-alterar-nota-fiscal-confirmada"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:16:54Z"
rotulos: ["Configuração", "Segurança", "NF-e", "TOP", "#publifercausaraiz", "CORE_E02722", "Permissão para usuário", "Erro: Alteração proibida", "Permissão em Tipo de Operação", "Erro"]
---

# Alteração proibida pelo Tipo de Operação (TOP) ou o usuário não tem autorização para alterar nota fiscal confirmada.

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16444339156375) MENSAGEM:**

[CORE\_E02722] Alteração proibida pelo Tipo de Operação (TOP) ou o usuário não tem autorização para alterar nota fiscal confirmada.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16444339158679) SOLUÇÃO:**

Para liberação de alteração de notas confirmadas em sua base, temos as restrições abaixo que precisam ser analisadas conforme sua necessidade:

![Imagem 3: Liberação por Tipo de Operação - TOP:](https://ajuda.sankhya.com.br/hc/article_attachments/16444358261399) Liberação por Tipo de Operação - TOP:

**(1)**Acesse a tela de cadastros de **"Tipos de Operação - TOP"** (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

**(1)**Selecione a TOP utilizada e na aba **"Geral"** marque a opção **"Permitir Alteração após confirmar"**.

![Imagem 4: (1) Selecione a TOP utilizada e na aba "Geral" marque a opção "Permitir Alteração após confirmar" .](https://ajuda.sankhya.com.br/hc/article_attachments/16444339163031)

![Imagem 5: Liberação por Usuário:](https://ajuda.sankhya.com.br/hc/article_attachments/16444358265751) Liberação por Usuário:

**(1)**Acesse a tela de **"Usuários"** (Caminho de acesso: Configurações >> Controle de Acesso) e na aba **"Segurança"** marque a opção **"Altera Nota Fiscal Confirmada"**.

![Imagem 6: (1) Acesse a tela de "Usuários" (Caminho de acesso: Configurações >> Controle de Acesso) e na aba "Segurança" marque a…](https://ajuda.sankhya.com.br/hc/article_attachments/16444358266519)

**![Imagem 7: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16444339166743)CAUSA**:

Ocorre quando a TOP do lançamento  e/ou o Usuário não possui permissões para alterar nota/pedido já confirmado.
