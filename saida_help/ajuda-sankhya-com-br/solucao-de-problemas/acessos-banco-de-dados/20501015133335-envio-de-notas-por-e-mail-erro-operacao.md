---
id: "20501015133335"
titulo: "Envio de notas por e-mail - Erro: Operação requer uma transação ativa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/20501015133335-Envio-de-notas-por-e-mail-Erro-Opera%C3%A7%C3%A3o-requer-uma-transa%C3%A7%C3%A3o-ativa"
trilha: "Solução de Problemas > Acessos/Banco de Dados"
atualizado_em: "2026-07-22T14:50:58Z"
rotulos: ["Configuração", "Cache", "NF-e", "Atualização", "e-mail", "driver oracle", "compatibilidade atualização reinicialização", "Erro", "Documentos Eletrônicos"]
---

# Envio de notas por e-mail - Erro: Operação requer uma transação ativa

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/20501000660887) **MENSAGEM:**

Ao realizar o envio de notas por e-mail, poderá ser apresentado o seguinte erro: Operação requer uma transação ativa.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/20501000662167) SOLUÇÃO:**

Quando for necessária a atualização do banco de dados, verifique a versão do Driver Oracle. Uma possível causa do erro pode ser a incompatibilidade entre as duas versões.

Siga as orientações abaixo para uma possível solução:

![Imagem 3: Compare as versões por meio da tela Administração do Servidor (Configurações » Avançado » Administração do Servidor)…](https://ajuda.sankhya.com.br/hc/article_attachments/20501015126551) Compare as versões por meio da tela **Administração do Servidor** (Configurações » Avançado » Administração do Servidor)  aba "Geral";

![Imagem 4: Compare as versões por meio da tela Administração do Servidor (Configurações » Avançado » Administração do Servidor)…](https://ajuda.sankhya.com.br/hc/article_attachments/20644579953047)

![Imagem 5: Atualize o Driver Oracle para garantir a compatibilidade com a versão mais recente do banco de dados (conforme item 1);](https://ajuda.sankhya.com.br/hc/article_attachments/20501000668055) Atualize o Driver Oracle para garantir a compatibilidade com a versão mais recente do banco de dados (conforme item 1);

![Imagem 6: Reinicie a aplicação e limpe o cache do navegador;](https://ajuda.sankhya.com.br/hc/article_attachments/20501000669591) Reinicie a aplicação e limpe o cache do navegador;

![Imagem 7: Em seguida, caso a solução seja efetiva, será possível realizar o envio dos e-mails novamente;](https://ajuda.sankhya.com.br/hc/article_attachments/20594874436503) Em seguida, caso a solução seja efetiva, será possível realizar o envio dos e-mails novamente;

**![Imagem 8: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/20595074097431) IMPORTANTE:**

Se o erro persistir, acione a equipe de atendimento do Service Desk para uma análise efetiva.
