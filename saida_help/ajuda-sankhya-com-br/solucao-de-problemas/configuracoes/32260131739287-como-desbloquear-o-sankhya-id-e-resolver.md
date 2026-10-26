---
id: "32260131739287"
titulo: "Como desbloquear o Sankhya ID e resolver o erro \"GTW3500\" \"Erro na comunicação com o SankhyaId\"?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32260131739287-Como-desbloquear-o-Sankhya-ID-e-resolver-o-erro-GTW3500-Erro-na-comunica%C3%A7%C3%A3o-com-o-SankhyaId"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:31:46Z"
rotulos: ["Segurança", "Integração", "Sankhya ID", "desbloquear Sankhya ID", "bloqueado", "error", "''codigo'': ''GTW3500''", "''descricao'': ''Erro na comunicação com o SankhyaId.''   }", "''error'': {", "API do Gateway", "Erro no Login do Gateway \"GTW3500\"", "\"Erro na comunicação com o SankhyaId.\"", "bloqueio Sankhya ID", "Sankhya ID bloqueado", "Erro", "Artigo atualizado KCS", "Plataforma - KCS"]
---

# Como desbloquear o Sankhya ID e resolver o erro "GTW3500" "Erro na comunicação com o SankhyaId"?

Este artigo tem como objetivo auxiliar na resolução do erro **“GTW3500 - Erro na comunicação com o SankhyaID”**, apresentado no endpoint **/login** do Gateway, cuja causa está relacionada ao bloqueio do Sankhya ID. Além disso, será demonstrado como realizar o desbloqueio

 **MENSAGEM:**

```
''error'': {
''codigo'': ''GTW3500'',
''descricao'': ''Erro na comunicação com o SankhyaId.''
}
```

![Imagem 1: Este artigo tem como objetivo auxiliar na resolução do erro “GTW3500 - Erro na comunicação com o SankhyaID” ,…](https://ajuda.sankhya.com.br/hc/article_attachments/32260148282903)

**SITUAÇÃO:**

O erro é exibido ao tentar realizar login na API do Gateway.

**Observação:** O login é realizado por meio de credenciais de e-mail vinculado ao Sankhya ID.

![Imagem 2: Observação: O login é realizado por meio de credenciais de e-mail vinculado ao Sankhya ID.](https://ajuda.sankhya.com.br/hc/article_attachments/33349781329431)

**SOLUÇÃO:**

**(1)** Acesse o **Sankhya Om** utilizando o Sankhya ID que se encontra bloqueado.

![Imagem 3: (1) Acesse o Sankhya Om utilizando o Sankhya ID que se encontra bloqueado.](https://ajuda.sankhya.com.br/hc/article_attachments/33349781332759)

**(2)** Esse acesso irá gerar automaticamente um e-mail com as instruções para o desbloqueio da conta.

![Imagem 4: (2) Esse acesso irá gerar automaticamente um e-mail com as instruções para o desbloqueio da conta.](https://ajuda.sankhya.com.br/hc/article_attachments/32260148284695)

**(3)** Verifique sua caixa de entrada e siga as orientações enviadas no e-mail para realizar o desbloqueio da conta.

![Imagem 5: (3) Verifique sua caixa de entrada e siga as orientações enviadas no e-mail para realizar o desbloqueio da conta.](https://ajuda.sankhya.com.br/hc/article_attachments/33349781335959)

**(4)** Após concluir o desbloqueio, realize uma nova tentativa de login na integração.

![Imagem 6: (4) Após concluir o desbloqueio, realize uma nova tentativa de login na integração.](https://ajuda.sankhya.com.br/hc/article_attachments/40324042858263)

Após realizar os passos anteriores, a comunicação com o Gateway será restabelecida com sucesso. Em seguida, realize uma nova tentativa de login e o erro não deverá mais ocorrer.

**CAUSA:**

O erro ocorre quando o Sankhya ID utilizado na integração é bloqueado devido ao excesso de tentativas de login com senha incorreta. Após 3 tentativas inválidas, o Sankhya ID é bloqueado automaticamente, impedindo a geração do token necessário para autenticação no Gateway e ocasionando o erro apresentado.
