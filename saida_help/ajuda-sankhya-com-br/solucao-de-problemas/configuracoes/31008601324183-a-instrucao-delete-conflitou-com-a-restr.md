---
id: "31008601324183"
titulo: "A instrução DELETE conflitou com a restrição do REFERENCE \"FK_XXXX_TSIUSU\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31008601324183-A-instru%C3%A7%C3%A3o-DELETE-conflitou-com-a-restri%C3%A7%C3%A3o-do-REFERENCE-FK-XXXX-TSIUSU"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:34:00Z"
rotulos: ["Configuração", "Segurança", "Cadastro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "delete", "reference", "FK", "TSIUSU", "Erro", "Integridade Referencial"]
---

# A instrução DELETE conflitou com a restrição do REFERENCE "FK_XXXX_TSIUSU"

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/31008601300247) **MENSAGEM:**

A instrução DELETE conflitou com a restrição do REFERENCE "FK\_XXXXX\_TSIUSU". O conflito ocorreu no banco de dados "XXXXX", tabela "SANKHYA.XXXXX", coluna "CODUSU.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31008627073943) SITUAÇÃO:**

Ao tentar excluir um usuário, a mensagem de erro acima é exibida.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31008627076375) SOLUÇÃO:**

O sistema não permite a exclusão de um usuário que tenha sido utilizado em movimentações. Para impedir novos acessos, sem removê-lo, siga a recomendação abaixo:

- - Acesse a tela **"Usuários";**
  - Localize o campo **"Data limite de acesso",** na aba **"Identificação";**
  - Defina uma data limite para esse usuário;
  - Salve as alterações.

Essa configuração garantirá que o usuário não possa mais acessar o sistema, sem comprometer a integridade dos dados históricos.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/31008627077271)CAUSA:**

Esse erro ocorre porque o usuário que se está tentando excluir já foi utilizado em alguma rotina do sistema. Por questões de integridade referencial do banco de dados, a exclusão não é permitida.
